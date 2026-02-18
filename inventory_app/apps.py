from django.apps import AppConfig


class InventoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory_app'

    def ready(self):
        from django.db.utils import OperationalError
        from .models import Category, Product

        try:
            if not Category.objects.exists():

                # ================= CATEGORIES =================
                electronics = Category.objects.create(name="Electronics")
                groceries = Category.objects.create(name="Groceries")
                fashion = Category.objects.create(name="Fashion")
                appliances = Category.objects.create(name="Home Appliances")
                books = Category.objects.create(name="Books")
                sports = Category.objects.create(name="Sports")

                # ================= ELECTRONICS =================
                Product.objects.bulk_create([
                    Product(name="Laptop", sku="ELEC001", category=electronics, price=55000, current_stock=12, reorder_level=5),
                    Product(name="Smartphone", sku="ELEC002", category=electronics, price=25000, current_stock=20, reorder_level=8),
                    Product(name="Bluetooth Speaker", sku="ELEC003", category=electronics, price=3000, current_stock=15, reorder_level=5),
                    Product(name="Wireless Mouse", sku="ELEC004", category=electronics, price=800, current_stock=30, reorder_level=10),
                    Product(name="Gaming Keyboard", sku="ELEC005", category=electronics, price=2500, current_stock=18, reorder_level=6),
                ])

                # ================= GROCERIES =================
                Product.objects.bulk_create([
                    Product(name="Rice 5kg", sku="GROC001", category=groceries, price=400, current_stock=50, reorder_level=20),
                    Product(name="Cooking Oil 1L", sku="GROC002", category=groceries, price=150, current_stock=40, reorder_level=15),
                    Product(name="Sugar 1kg", sku="GROC003", category=groceries, price=50, current_stock=60, reorder_level=25),
                    Product(name="Wheat Flour 5kg", sku="GROC004", category=groceries, price=300, current_stock=35, reorder_level=15),
                    Product(name="Tea Powder 500g", sku="GROC005", category=groceries, price=200, current_stock=28, reorder_level=10),
                ])

                # ================= FASHION =================
                Product.objects.bulk_create([
                    Product(name="Men T-Shirt", sku="FASH001", category=fashion, price=700, current_stock=35, reorder_level=10),
                    Product(name="Women Handbag", sku="FASH002", category=fashion, price=2000, current_stock=18, reorder_level=5),
                    Product(name="Jeans", sku="FASH003", category=fashion, price=1500, current_stock=22, reorder_level=8),
                    Product(name="Sneakers", sku="FASH004", category=fashion, price=3000, current_stock=14, reorder_level=5),
                ])

                # ================= HOME APPLIANCES =================
                Product.objects.bulk_create([
                    Product(name="Refrigerator", sku="HOME001", category=appliances, price=30000, current_stock=5, reorder_level=2),
                    Product(name="Washing Machine", sku="HOME002", category=appliances, price=22000, current_stock=7, reorder_level=3),
                    Product(name="Microwave Oven", sku="HOME003", category=appliances, price=12000, current_stock=10, reorder_level=4),
                ])

                # ================= BOOKS =================
                Product.objects.bulk_create([
                    Product(name="Python Programming", sku="BOOK001", category=books, price=500, current_stock=25, reorder_level=10),
                    Product(name="Data Science Guide", sku="BOOK002", category=books, price=650, current_stock=20, reorder_level=8),
                    Product(name="Django Mastery", sku="BOOK003", category=books, price=700, current_stock=15, reorder_level=5),
                ])

                # ================= SPORTS =================
                Product.objects.bulk_create([
                    Product(name="Cricket Bat", sku="SPORT001", category=sports, price=1500, current_stock=12, reorder_level=5),
                    Product(name="Football", sku="SPORT002", category=sports, price=900, current_stock=18, reorder_level=7),
                    Product(name="Yoga Mat", sku="SPORT003", category=sports, price=800, current_stock=20, reorder_level=8),
                ])

                print("✅ Full professional product database seeded!")

        except OperationalError:
            pass
