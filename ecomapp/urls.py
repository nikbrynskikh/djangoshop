from django.conf.urls import url
from ecomapp.views import base_view, product_view, category_view
urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^$', base_view, name='base' )
]