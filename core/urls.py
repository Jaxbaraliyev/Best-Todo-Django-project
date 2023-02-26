"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TodoView.as_view(), name='home'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
    path('todo/<int:pk>/important/', todo_important, name='todo_important'),
    path('todo/<int:pk>/active/', todo_active, name='todo_active'),
    path('todo/delete/',todo_all_delete, name='todo_all_delete')
]
