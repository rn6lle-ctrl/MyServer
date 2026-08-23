from django.contrib import admin
from django.urls import path, include  # <-- добавили include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # <-- добавили эту строку
]