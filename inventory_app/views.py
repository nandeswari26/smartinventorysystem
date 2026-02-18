from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Count, Q
from django.db.models.functions import TruncMonth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json

from .models import Product, Sale, Category
from .forms import ProductForm, SaleForm


# ===================== LOGIN =====================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


# ===================== SIGNUP =====================
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


# ===================== LOGOUT =====================
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# ===================== DASHBOARD =====================
@login_required
def dashboard(request):
    total_products = Product.objects.count()
    total_sales = Sale.objects.aggregate(total=Sum('quantity_sold'))['total'] or 0

    revenue_expression = ExpressionWrapper(
        F('quantity_sold') * F('product__price'),
        output_field=DecimalField()
    )

    total_revenue = Sale.objects.aggregate(
        revenue=Sum(revenue_expression)
    )['revenue'] or 0

    top_product = (
        Sale.objects
        .values('product__name')
        .annotate(total_sold=Sum('quantity_sold'))
        .order_by('-total_sold')
        .first()
    )

    monthly_sales = (
        Sale.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('quantity_sold'))
        .order_by('month')
    )

    months = []
    sales_data = []

    for item in monthly_sales:
        if item['month']:
            months.append(item['month'].strftime("%b %Y"))
            sales_data.append(item['total'])

    product_sales = (
        Sale.objects
        .values('product__name')
        .annotate(total=Sum('quantity_sold'))
    )

    product_labels = [item['product__name'] for item in product_sales]
    product_values = [item['total'] for item in product_sales]

    low_stock_products = Product.objects.filter(
        current_stock__lte=F('reorder_level')
    )

    context = {
        'total_products': total_products,
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'top_product': top_product,
        'low_stock_products': low_stock_products,
        'months': json.dumps(months),
        'sales_data': json.dumps(sales_data),
        'product_labels': json.dumps(product_labels),
        'product_values': json.dumps(product_values),
    }

    return render(request, 'dashboard.html', context)


# ===================== PRODUCT LIST =====================
@login_required
def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'product_list.html', {'products': products})


# ===================== ADD PRODUCT =====================
@login_required
def add_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {
        'form': form,
        'categories': categories
    })


# ===================== UPDATE PRODUCT =====================
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'add_product.html', {
        'form': form,
        'categories': categories
    })


# ===================== DELETE PRODUCT =====================
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('product_list')


# ===================== ADD SALE =====================
@login_required
def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Sale recorded successfully!")
                return redirect('dashboard')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = SaleForm()

    return render(request, 'add_sale.html', {'form': form})


# ===================== SALE HISTORY =====================
@login_required
def sale_history(request):
    sales = Sale.objects.all().order_by('-date')
    return render(request, 'sale_history.html', {'sales': sales})


# ===================== CATEGORY PAGE =====================
@login_required
def category_list(request):
    categories = (
        Product.objects
        .values('category__id', 'category__name')
        .annotate(
            total_products=Count('id'),
            low_stock_count=Count(
                'id',
                filter=Q(current_stock__lte=F('reorder_level'))
            )
        )
        .order_by('category__name')
    )

    return render(request, 'categories.html', {
        'categories': categories
    })


# ===================== SUPPLIER PAGE =====================
@login_required
def supplier_list(request):
    suppliers = (
        Product.objects
        .values('supplier')
        .annotate(
            total_products=Count('id'),
            low_stock_count=Count(
                'id',
                filter=Q(current_stock__lte=F('reorder_level'))
            )
        )
        .order_by('supplier')
    )

    return render(request, 'suppliers.html', {
        'suppliers': suppliers
    })


# ===================== STOCK IN =====================
@login_required
def stock_in(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = int(request.POST.get("quantity", 0))

        product = get_object_or_404(Product, id=product_id)
        product.current_stock += quantity
        product.save()

        messages.success(request, f"{quantity} items added to {product.name}.")
        return redirect('stock_in')

    return render(request, 'stock_in.html', {'products': products})


# ===================== STOCK OUT =====================
@login_required
def stock_out(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST.get("product")
        quantity = int(request.POST.get("quantity", 0))

        product = get_object_or_404(Product, id=product_id)

        if product.current_stock >= quantity:
            product.current_stock -= quantity
            product.save()
            messages.success(request, f"{quantity} items removed from {product.name}.")
        else:
            messages.error(request, "Not enough stock available!")

        return redirect('stock_out')

    return render(request, 'stock_out.html', {'products': products})


# ===================== REPORTS =====================
@login_required
def reports(request):
    total_products = Product.objects.count()
    total_sales = Sale.objects.aggregate(total=Sum('quantity_sold'))['total'] or 0

    revenue_expression = ExpressionWrapper(
        F('quantity_sold') * F('product__price'),
        output_field=DecimalField()
    )

    total_revenue = Sale.objects.aggregate(
        revenue=Sum(revenue_expression)
    )['revenue'] or 0

    sales = Sale.objects.all().order_by('-date')

    return render(request, 'reports.html', {
        'total_products': total_products,
        'total_sales': total_sales,
        'total_revenue': total_revenue,
        'sales': sales,
    })


# ===================== LOW STOCK =====================
@login_required
def low_stock(request):
    low_stock_products = Product.objects.filter(
        current_stock__lte=F('reorder_level')
    )

    return render(request, 'low_stock.html', {
        'low_stock_products': low_stock_products
    })


# ===================== USERS =====================
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


# ===================== SETTINGS =====================
@login_required
def settings_view(request):
    return render(request, 'settings.html')
