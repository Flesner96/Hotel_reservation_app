"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from reservation_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.lista_sal, name='lista_sal'),
    path('room/new/', views.add_room, name='add_room'),
    path('room/<int:id>/', views.sala_detail, name='sala_detail'),
    path('room/<int:id>/delete/', views.delete_room, name='delete_room'),
    path('room/<int:id>/modify/', views.modify_room, name='modify_room'),
    path('room/reserve/<int:id>/', views.reserve_room, name='reserve_room'),
    path('admin/', admin.site.urls),
]
