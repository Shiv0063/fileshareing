"""
URL configuration for files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from main import views
from main.views import mainview,home,dlt,filedlt,myfiles
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(template_name='home.html'),name='login'),
    path('file',home),
    # url(r'^workers/$', mainview.as_view())
    # path('home',login_required(mainview.as_view()),name="file"),
    path('home',mainview,name="file"),
    path('upload/',myfiles,name='upload-view'),
    path('fdlt',dlt,name='filedelete'),
    path("filedlt/<int:id>",filedlt),
    path('admin/', admin.site.urls),
    path('afterlogin',home,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='home.html'),name='logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)