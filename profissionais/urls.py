from django.conf.urls import url, include
from profissionais import views
from django.contrib import admin
from profissionais.views import  BuscarProfissionalView, BuscarEspecilidadeView, BuscarLocaisView
from django.contrib.auth import views as auth_views



urlpatterns = [
    
	url(r'^$', views.index, name= 'index' ),
	url(r'^especialidade$', views.especialidade, name= 'especialidade' ),
	url(r'^cidade$', views.cidade, name= 'cidade' ),
	url(r'^a-admin$', views.administracao, name= 'a-admin' ),
	#url(r'^busca/$', views.busca, name= 'busca' ),
	url(r'^login/$', auth_views.login, {'template_name' : 'login.html'}, name="login"),
   	url(r'^logout/$', auth_views.logout_then_login, {'login_url' : '/login/'}, name="logout"),
	
	url(r'^resultado-busca$', BuscarProfissionalView.as_view()  , name= 'buscar-profissionais'),
	url(r'^profissional/(?P<id>\d+)/detalhe$', views.detalhe , name= 'detalhe'),
	url(r'^resultado-busca-especialidade$', BuscarEspecilidadeView.as_view()  , name= 'buscar-por-especialiade'),
	url(r'^resultado-busca-cidade$', BuscarLocaisView.as_view()  , name= 'buscar-por-cidade'),
	url(r'^local/(?P<id>\d+)/profissional$', views.prof_locais , name= 'local-prof'),
	
]