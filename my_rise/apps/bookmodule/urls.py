from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('', views.index, name='index'),  # عندما يكون المسار فارغًا، قم بعرض صفحة الفهرس
]
