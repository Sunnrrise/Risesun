from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('prose/', views.prose, name='prose'),
    path('save_prose/', views.save_prose, name='save_prose'),  # تأكد من وجود هذا المسار
]
