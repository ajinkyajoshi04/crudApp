from django.contrib import admin
from django.urls import path
from crudApp import views

urlpatterns = [
    path('display/', views.display, name = 'display'),
    path('form/', views.form, name = 'form'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]
