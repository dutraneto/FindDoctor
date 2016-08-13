from django.conf.urls import url, include
from profissionais import views
from django.contrib import admin


urlpatterns = [
    
	url(r'^$', views.index, name= 'index' ),
	url(r'^busca/$', views.busca, name= 'busca' ),
	url(r'^especialidade_detalhe/(?P<pk>\d+)/$', views.especialidade_detalhe, name= 'especialidade_detalhe' ),
	#url(r'^admin/', admin.site.urls, name='admin'),
]