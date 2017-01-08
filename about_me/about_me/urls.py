"""about_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import main
from mainapp.views import about
from mainapp.views import my_study
from mainapp.views import my_work
from mainapp.views import my_project
from mainapp.views import about_mir
from mainapp.views import about_pil
from mainapp.views import about_urion
from mainapp.views import about_alfa
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^about/$', about, name='about'),
    url(r'^my_study/$', my_study, name='my_study'),
    url(r'^my_work/$', my_work, name='my_work'),
    url(r'^my_project/$', my_project, name='my_project'),
    url(r'^my_work/about_mir/$', about_mir, name='about_mir'),
    url(r'^my_work/about_pil/$', about_pil, name='about_pil'),
    url(r'^my_work/about_urion/$', about_urion, name='about_urion'),
    url(r'^my_work/about_alfa/$', about_alfa, name='about_alfa')
]
