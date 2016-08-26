from django.shortcuts import render
from especialidades.models import  Especialidade
from profissionais.models import  Profissional
from profissionais.forms import  BuscarProfissionalForm, BuscarCidadeProfForm
from django.views.generic.base import View
from estabelecimentos.models import Cidade, Local
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	dados = {}
	dados['lista_profissionais'] = Profissional.objects.order_by('nome')
	dados['lista_especialidades'] = Especialidade.objects.order_by('nomeEspecialidade')
	return render(request, 'index.html', dados)

def especialidade(request):

	return render(request, 'especialidades.html', {"especialidade":Especialidade.objects.all()} )
def cidade(request):

	return render(request, 'cidades.html', {"cidade":Cidade.objects.all()} )

@login_required
def administracao(request):
	user = get_cliente_logado(request)
	return render(request, 'pagina-administrativa.html', {'user': user} )

def get_cliente_logado(request):
	return request.user


def detalhe(request, id):
	prof = Profissional.objects.get(id=id);
	return render(request, 'detalhes.html', {"objects": prof, "especialidade": Especialidade.objects.all()})

class BuscarProfissionalView(View):



	def post(self, request):
		form = BuscarProfissionalForm(request.POST or None)
		if form.is_valid():
			dados_form = form.data
			prof = Profissional.objects.filter(nome__icontains= dados_form['busca'] )
			sob = Profissional.objects.filter(sobrenome__icontains= dados_form['busca'] )

			return render(request, 'busca.html', {'profissionais': prof or sob})
		else:
			return render(request, 'msg_erro.html')

class BuscarEspecilidadeView(View):

	def get(self, request):
		q_especialidade = request.GET.get('especialidade', '')
		if q_especialidade:
			esp = Especialidade.objects.filter(id = q_especialidade)
			prof = Profissional.objects.filter(especialidade= esp)
			paginator = Paginator(prof, 10)

			try:
				page = int(request.GET.get('page', '1')) 
			except ValueError:
				page = 1
			try: 
				p = paginator.page(page) 
			except (EmptyPage, InvalidPage):
				p = paginator.page(paginator.num_pages)
			return render(request, 'busca-especialidade.html', {'profissionais': p, 'especialidade': esp})	

	def post(self, request):
		form = BuscarProfissionalForm(request.POST)
		if form.is_valid():
			dados_form = form.data
			if int(dados_form['busca']) > 0:
				esp = Especialidade.objects.filter(id= dados_form['busca'])
				prof = Profissional.objects.filter(especialidade= esp)
				paginator = Paginator(prof, 10)

				try:
					page = int(request.GET.get('page', '1')) 
				except ValueError:
					page = 1
				try: 
					p = paginator.page(page) 
				except (EmptyPage, InvalidPage):
					p = paginator.page(paginator.num_pages)
				return render(request, 'busca-especialidade.html', {'profissionais': p, 'especialidade': esp})
			else:
				return render(request, 'especialidades.html', {"especialidade":Especialidade.objects.all()} )

			#return render(request, 'busca.html', {'profissionais': prof})

class BuscarLocaisView(View):


	def get(self, request):
		q_cidade = request.GET.get('cidade','')
		if q_cidade:
			cid = Cidade.objects.filter(id = q_cidade)
			local = Local.objects.filter(cidade=cid);
			#prof = Profissional.objects.filter(local=local)
			paginator = Paginator(local, 10)
			try:
				page = int(request.GET.get('page', '1')) 
			except ValueError:
				page = 1
			try: 
				p = paginator.page(page) 
			except (EmptyPage, InvalidPage):
				p = paginator.page(paginator.num_pages)
			return render(request, 'busca-cidade.html', {'locais': p, 'cidade': cid})
			
			#return render(request, 'teste.html', {'loc': local} )
	def post(self, request):
		form = BuscarCidadeProfForm(request.POST)
		if form.is_valid():
			dados_form = form.data
			if int(dados_form['busca']) > 0:
				cid = Cidade.objects.filter(id = dados_form['busca'])
				loc = Local.objects.filter(cidade=cid);
				
					
				#prof = Profissional.objects.filter(local=loc)
				

				paginator = Paginator(loc, 10)

				try:
					page = int(request.GET.get('page', '1')) 
				except ValueError:
					page = 1
				try: 
					p = paginator.page(page) 
				except (EmptyPage, InvalidPage):
					p = paginator.page(paginator.num_pages)
				return render(request, 'busca-cidade.html', {'locais': p, 'cidade': cid})
			else:
				return render(request, 'cidades.html', {"cidade":Cidade.objects.all()} )

def prof_locais(request, id):
	loc = Local.objects.get(id=id);
	prof = Profissional.objects.filter(local=loc)
			
	paginator = Paginator(prof, 10)

	try:
		page = int(request.GET.get('page', '1')) 
	except ValueError:
		page = 1
	try: 
		p = paginator.page(page) 
	except (EmptyPage, InvalidPage):
		p = paginator.page(paginator.num_pages)
	return render(request, 'busca-locais.html', {'profissionais': p, 'local': loc})

				
		
