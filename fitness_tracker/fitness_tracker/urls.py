"""fitness_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('api.urls')),
]

# Регистрация
# http://127.0.0.1:8000/auth/users/ ->  username password email


# http://127.0.0.1:8000/auth/users/activation/ uid token
# на почту придет http://127.0.0.1:8000/#/activate/MjM/arixce-345e3218b3b256bc879c64e101131c93
# uid = MjM
# token = arixce-345e3218b3b256bc879c64e101131c93

# Авторизация
# http://127.0.0.1:8000/auth/token/login/->  username password
