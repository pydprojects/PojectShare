"""AccSales URL Configuration

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
from django.conf import settings
from django.urls import path, include

from home.views import e_handler404, e_handler500

handler404 = 'home.views.e_handler404'
handler500 = 'home.views.e_handler500'

urlpatterns = [
    path('', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('messenger/', include('messenger.urls')),
]

# Added to make possible load image in templates by image.url from ImageField
if settings.DEBUG is True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
