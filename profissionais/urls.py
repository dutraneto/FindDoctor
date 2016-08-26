from django.conf.urls import url, include
from profissionais import views
from django.contrib import admin
from profissionais.views import  BuscarProfissionalView, BuscarEspecilidadeView, BuscarLocaisView



urlpatterns = [
    
	url(r'^$', views.index, name= 'index' ),
	url(r'^especialidade$', views.especialidade, name= 'especialidade' ),
	url(r'^cidade$', views.cidade, name= 'cidade' ),
	#url(r'^busca/$', views.busca, name= 'busca' ),
	
	url(r'^resultado-busca$', BuscarProfissionalView.as_view()  , name= 'buscar-profissionais'),
	url(r'^profissional/(?P<id>\d+)/detalhe$', views.detalhe , name= 'detalhe'),
	url(r'^resultado-busca-especialidade$', BuscarEspecilidadeView.as_view()  , name= 'buscar-por-especialiade'),
	url(r'^resultado-busca-cidade$', BuscarLocaisView.as_view()  , name= 'buscar-por-cidade'),
	url(r'^local/(?P<id>\d+)/profissional$', views.prof_locais , name= 'local-prof'),
	
]