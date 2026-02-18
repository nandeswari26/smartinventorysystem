# 🚀 Smart Inventory Management System

> A modern, enterprise-ready inventory management web application built with Django.

---

## 📌 Overview

The **Smart Inventory Management System** is a full-featured web application designed to help businesses efficiently manage:

- Products  
- Categories  
- Suppliers  
- Stock movements  
- Sales  
- Revenue analytics  

The system includes a modern glass UI, responsive design, and scalable backend architecture suitable for small to medium-sized businesses.

---

## 🎯 Business Problem

Manual inventory management often leads to:

- Stock mismanagement  
- Revenue leakage  
- Lack of real-time insights  
- Poor supplier coordination  
- No automated low-stock alerts  

---

## 💡 Solution

This system solves these challenges by providing:

- ✅ Centralized product tracking  
- ✅ Automated stock calculations  
- ✅ Real-time reporting  
- ✅ Data-driven decision support  
- ✅ Low stock monitoring system  

---

## ✨ Key Features

### 🔐 Authentication & Security
- User Login & Signup
- Role-based access (Admin / Staff / User)
- Secure session handling
- CSRF protection

---

### 📦 Inventory Management
- Add / Update / Delete Products
- Category Management
- Supplier Tracking
- SKU Management
- Price & Reorder Level Control

---

### 📊 Stock Management
- Stock In
- Stock Out
- Automatic stock updates
- Low stock alerts (Dynamic detection)

---

### 🛒 Sales Module
- Record sales transactions
- Automatic stock deduction
- Revenue calculation
- Sales history tracking

---

### 📈 Dashboard & Analytics
- Total products overview
- Total sales quantity
- Revenue calculation
- Monthly sales insights
- Top-selling products
- Low stock monitoring

---

## 🏗 System Architecture

### Backend
- Python 3.12
- Django 6
- Django ORM
- Aggregations & F Expressions
- SQLite (Development)

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Glass UI Design
- Responsive Sidebar Layout

---

## 🛠 Technology Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Python, Django |
| Database     | SQLite3 |
| Frontend     | HTML, CSS, Bootstrap |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
smartinventorysystem/
│
├── inventory_app/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/smartinventorysystem.git
cd smartinventorysystem
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate (Windows):

```bash
venv\Scripts\activate
```

Activate (Mac/Linux):

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Security

- CSRF Protection Enabled
- Django Authentication System
- ORM-based Queries (SQL Injection Safe)
- Form Validation

---

## 🚀 Future Enhancements

- Django REST API Integration
- PostgreSQL Production Database
- Email Notifications for Low Stock
- Export Reports (PDF / Excel)
- Docker Support
- Cloud Deployment (AWS / Render)

---

## 💼 Resume Description (For Interviews)

Developed a full-stack inventory management system using Django with automated stock tracking, revenue analytics, supplier management, and real-time dashboard visualization. Implemented ORM aggregations and optimized database queries for performance and scalability.

---

## 👩‍💻 Author

**MOCHI NAGA NANDESWARI**  
SAP Certified | Python Developer | Django Developer  

---

## 📜 License

This project is developed for educational and portfolio purposes.
