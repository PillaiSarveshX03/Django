# Django REST Framework (DRF) — Complete Step-by-Step Guide
> README & Architecture Reference (AI Generated)

---

## 📌 Table of Contents
1. [Architecture & Concept Overview](#1-architecture--concept-overview)
2. [Environment Setup](#2-environment-setup)
3. [Project & App Initialization](#3-project--app-initialization)
4. [Configuring Project Settings](#4-configuring-project-settings)
5. [Building REST API Components](#5-building-rest-api-components)
   - [Step 5.1: Create Models (`models.py`)](#51-creating-models-apimodelsy)
   - [Step 5.2: Create Serializers (`serializers.py`)](#52-creating-serializers-apiserializerspy)
   - [Step 5.3: Define Views (`views.py`)](#53-defining-views-apiviewspy)
   - [Step 5.4: App URL Routing (`api/urls.py`)](#54-app-url-routing-apiurlspy)
   - [Step 5.5: Project-Level URL Routing (`backend/urls.py`)](#55-project-level-url-routing-backendurlspy)
6. [Database Migrations & ORM](#6-database-migrations--orm)
7. [Authentication, Permissions & Security](#7-authentication-permissions--security)
8. [Running the Development Server](#8-running-the-development-server)

---

## 1. Architecture & Concept Overview

In traditional web applications, Django uses the **MVT (Model-View-Template)** pattern. When building RESTful APIs, Django transforms into a **Model-View-Generics (MVGenerics)** architecture where templates are replaced by serialized JSON data.

```
       ┌───────────────────────────────┐
       │      Database (SQLite)        │
       └──────────────┬────────────────┘
                      │ (Django ORM)      <-- Python Equivalent oF SQL
                      ▼
       ┌───────────────────────────────┐
       │     Models (`models.py`)      │  <-- Defines DB Schema & Tables
       └──────────────┬────────────────┘
                      │
                      ▼
       ┌───────────────────────────────┐
       │  Serializers(`serializers.py`)│  <-- Converts Complex Data <-> JSON & Validates
       └──────────────┬────────────────┘
                      │
                      ▼
       ┌───────────────────────────────┐
       │       Views (`views.py`)      │  <-- Business Logic, Generic Views, ViewSets
       └──────────────┬────────────────┘
                      │
                      ▼
       ┌───────────────────────────────┐
       │      Routing (`urls.py`)      │  <-- API Endpoints (e.g., `/api/items/`)
       └──────────────┬────────────────┘
                      │ (HTTP Requests/Responses)
                      ▼
                Client / Frontend (React, Vue, Mobile App, Postman)
```

> [!NOTE]
> **Django ORM (Object-Relational Mapping):** Instead of writing raw SQL queries, Django provides an intuitive Python API to query, filter, create, and update records across any supported database engine.

---

## 2. Environment Setup

### 2.1 Create Virtual Environment (Windows)
```bash
# Create a virtual environment named 'venv'
py -m venv venv
```

### 2.2 Activate Virtual Environment
```bash
# Command Prompt
venv\Scripts\activate.bat

# PowerShell
.\venv\Scripts\Activate.ps1

# Git Bash
source venv/Scripts/activate
```

### 2.3 Install Required Dependencies
```bash
# Install Django and Django REST Framework
pip install django djangorestframework
pip install django_rest_framework

# (Optional dependencies if needed for your specific services)
# pip install django-cors-headers
```

---

## 3. Project & App Initialization

### 3.1 Create Django Project
```bash
# Initialize project named 'backend'
django-admin startproject backend
```

### 3.2 Navigate into Project Directory & Run Initial Migrations
```bash
cd backend
py manage.py migrate
```

### 3.3 Create the API Application
```bash
# Create an app dedicated to handling API logic
py manage.py startapp api
```

This creates a modular structure:
```
backend/
├── manage.py
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    └── tests.py
```

---

## 4. Configuring Project Settings

Open `backend/settings.py` and register `rest_framework` and your `api` app in `INSTALLED_APPS`:

```python
# backend/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',

    # Local apps
    'api',
]
```

---

## 5. Building REST API Components

### 5.1 Creating Models (`api/models.py`)
Define database tables using Django's ORM:

```python
# api/models.py
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

### 5.2 Creating Serializers (`api/serializers.py`)
Create a new file `api/serializers.py`. Serializers convert complex Model instances into native Python datatypes that can easily be rendered into JSON/XML, and deserialize incoming JSON payloads back into validated objects.

```python
# api/serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  
        
        # Or specify: ['id', 'title', 'description', 'completed', 'created_at']
```

---

### 5.3 Defining Views (`api/views.py`)
Django REST Framework provides powerful generic class-based views for CRUD operations:

```python
# api/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Item
from .serializers import ItemSerializer

# List all items or create a new item (GET / POST)
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

# Retrieve, update or delete a specific item (GET / PUT / PATCH / DELETE)
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
```

---

### 5.4 App URL Routing (`api/urls.py`)
Create `api/urls.py` to route requests to the respective views:

```python
# api/urls.py
from django.urls import path
from .views import ItemListCreateView, ItemDetailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
```

---

### 5.5 Project-Level URL Routing (`backend/urls.py`)
Include your app's URLs inside the root `backend/urls.py`:

```python
# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Mounts all API endpoints under /api/
]
```

---

## 6. Database Migrations & ORM

Whenever you create or modify models in `api/models.py`, generate and apply database migrations:

```bash
# 1. Create migration files based on detected model changes
py manage.py makemigrations

# 2. Apply migrations to the database
py manage.py migrate

# (Optional) Apply migrations specifically to the api app:
# py manage.py migrate api
```

---

## 7. Authentication, Permissions & Security

### 7.1 Create an Admin / Superuser
```bash
py manage.py createsuperuser
```
Follow the prompts to enter username, email, and password.

### 7.2 Secure API Endpoints
To restrict endpoints to authenticated users only, update `permission_classes` in your views:

```python
# In api/views.py
from rest_framework.permissions import IsAuthenticated

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]  # Requires token/session authentication
```

You can also set default global permission policies in `backend/settings.py`:
```python
# backend/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```

---

## 8. Running the Development Server

Start the local Django server:
```bash
py manage.py runserver
```

### 🌐 Access Points:
- **API Endpoints:** [http://127.0.0.1:8000/api/items/](http://127.0.0.1:8000/api/items/) *(DRF interactive Browsable API)*
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
