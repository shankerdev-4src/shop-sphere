# 🛒 ShopSphere

ShopSphere is a full-stack e-commerce web application built using Django and Django REST Framework.  
The project includes both a template-based frontend and a REST API for product management.

It demonstrates authentication, cart functionality, product management, and API development in a modular Django structure.

---

## 🚀 Features

### 👤 Authentication System
- User Registration
- Login & Logout
- Profile Page
- Change Password
- Secure session handling

### 🛍️ Product Management
- Product listing on homepage
- Product images support
- Admin product management
- Default image handling

### 🛒 Cart System
- Add products to cart
- View cart page
- Cart model stored in database

### 🔌 REST API (Django REST Framework)
- Product serializers
- API endpoints for products
- Structured API responses

### 🎨 Frontend
- Django Templates
- Base layout (main.html, nav.html)
- Static CSS styling
- Image uploads support

---

##  Project Architecture

The project is divided into multiple Django apps for clean separation of concerns:

- `authen` → Handles user authentication and profile management
- `base` → Core e-commerce logic (products, cart, homepage)
- `products_api` → REST API for products
- `myproject` → Main Django project settings
- `static/` → CSS and images
- `templates/` → Global template files

---


