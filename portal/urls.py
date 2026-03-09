from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),
    
    path('delete/<int:resource_id>/', views.delete_resource, name='delete_resource'),

    path('download/<int:resource_id>/', views.download_resource, name='download_resource'),

]