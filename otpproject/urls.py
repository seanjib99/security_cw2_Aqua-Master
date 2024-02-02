from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import StaticSitemap, ProductSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticSitemap,
    'product':ProductSitemap
}

admin.site.site_header = 'Aqua ADMIN'
admin.site.site_title = 'Aqua! ADMIN PANEL'
admin.site.index_title = 'WELCOME TO Aqua! ADMIN PANEL'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('registration.urls')),
    path('sitemap.xml/', sitemap,{'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)