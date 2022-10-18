"""untirta2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from tirtayasa.views import proditirtayasa
from bangunruang.views import bangunruang
from belahketupat.views import belahketupat
from jajargenjang.views import jajargenjang
from layanglayang.views import layanglayang
from lingkaran.views import lingkaran
from persegi.views import persegi
from persegipanjang.views import persegipanjang
from segitiga.views import segitiga
from trapesium.views import trapesium

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tirtayasa/', proditirtayasa),
    path('bangunruang/', bangunruang),
    path('belahketupat/', belahketupat),
    path('jajargenjang/', jajargenjang),
    path('layanglayang/', layanglayang),
    path('lingkaran/', lingkaran),
    path('persegi/', persegi),
    path('persegipanjang/', persegipanjang),
    path('segitiga/', segitiga),
    path('trapesium/', trapesium),
]
