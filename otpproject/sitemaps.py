from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from home.models import Product

class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'products', 'search', 'orders', 'wishlist', 'cart', 'change_password', 'password_reset']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.modified_date

    def location(self, obj):
        return f'/productdetail/{obj.slug}'