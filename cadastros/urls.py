from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.index, name='index'),  # Home or list view
    path('produto/add/', views.produto_create, name='produto_add'),
    path('produto/<int:pk>/edit/', views.produto_update, name='produto_edit'),
    path('produto/<int:pk>/delete/', views.produto_delete, name='produto_delete'),
    path('cliente/add/', views.cliente_create, name='cliente_add'),
    path('cliente/<int:pk>/edit/', views.cliente_update, name='cliente_edit'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    path('search/', views.search, name='search'),
]
