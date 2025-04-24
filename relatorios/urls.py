from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('', views.relatorio, name='relatorio'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export/xls/', views.export_xls, name='export_xls'),
]
