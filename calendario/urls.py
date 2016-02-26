from django.conf.urls import include, url
from django.contrib import admin
from mesas import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.principal, name = 'principal'),
    url(r'^buscar/$', views.buscar, name ='buscar'),
    url(r'(?P<pk>[0-9]+)/$', views.mostrar_materias, name = 'mostrar_materias'),

]
