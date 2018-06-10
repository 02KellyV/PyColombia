

from django.conf.urls import url

from .views import List, Detail, Creation, Update, Delete

urlpatterns = [

    url(r'^$', List, name='list'),
    url(r'^(?P<pk>\d+)$', Detail, name='detail'),
    url(r'^nuevo$', Creation, name='new'),
    url(r'^editar/(?P<pk>\d+)$', Update, name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', Delete, name='delete'),

]