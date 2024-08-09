"""
URL configuration for blogproject project.

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
from blogapp import views
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.land,name='land'),
    path('home/', views.home,name='home'),
    path('add/',views.add,name='addblog'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>', views.update,name="update"),
    path('delete/<int:id>', views.destroy,name="delete"),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
