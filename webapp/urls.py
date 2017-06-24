from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^produkt/(?P<name>.+)/$', views.product_detail, name='product_detail'),
    url(r'^kategoria/(?P<name>.+)/$', views.get_product, name='get_product'),
    url(r'^szkoly/$', views.szkoly, name='szkoly'),
    url(r'^firmy/$', views.firmy, name='firmy'),
    url(r'^uslugi/$', views.uslugi, name='uslugi'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^szukaj/?(.*)/$', views.search, name='search'),

]