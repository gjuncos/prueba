from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'proyecto_prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^noticia/(?P<Noticia_id>[0-9]+)','Noticias.views.noticia_detalle'),
    url(r'^contacto','contacto.views.Contacto')
]
