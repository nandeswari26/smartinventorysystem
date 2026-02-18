from django.urls import path
from . import views

urlpatterns = [

    # =============================
    # Authentication
    # =============================
    path('', views.login_view, name='home'),   # default route
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # =============================
    # Dashboard
    # =============================
    path('dashboard/', views.dashboard, name='dashboard'),

    # =============================
    # Products
    # =============================
    path('products/', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),

    # =============================
    # Categories
    # =============================
    path('categories/', views.category_list, name='category_list'),

    # =============================
    # Suppliers
    # =============================
    path('suppliers/', views.supplier_list, name='supplier_list'),

    # =============================
    # Stock Management
    # =============================
    path('stock-in/', views.stock_in, name='stock_in'),
    path('stock-out/', views.stock_out, name='stock_out'),

    # =============================
    # Sales
    # =============================
    path('add-sale/', views.add_sale, name='add_sale'),
    path('sale-history/', views.sale_history, name='sale_history'),

    # =============================
    # Reports & Alerts
    # =============================
    path('reports/', views.reports, name='reports'),
    path('low-stock/', views.low_stock, name='low_stock'),

    # =============================
    # User Management
    # =============================
    path('users/', views.user_list, name='user_list'),
    path('settings/', views.settings_view, name='settings'),
]
