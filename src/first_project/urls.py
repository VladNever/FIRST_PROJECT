"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from profiles.auth_views import MyLogin, MyLogout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ref_books/', include('ref_books.urls', namespace="ref_books")),
    path('books/', include('books.urls', namespace="books")),
    path('', include('homepage.urls', namespace="homepage")),
    path('profiles/', include('profiles.urls', namespace="profile")),
    path('login/', MyLogin.as_view(), name="login"),
    path('logout/', MyLogout.as_view(), name="logout"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
