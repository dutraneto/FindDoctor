from django.shortcuts import render
from especialidades.models import  Especialidade
from profissionais.models import  Profissional
from profissionais.forms import  BuscarProfissionalForm, BuscarCidadeProfForm
from django.views.generic.base import View
from estabelecimentos.models import Cidade, Local
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

def busca(request):
	try:
		nome_profissional = request.GET['profissional']
		profissional = Profissional.objects.filter(nome_iconteins=nome_profissional)
		return render(request,'resposta.html',{'object':profissional})
	except Exception:
		return render(request,'msg_erro.html')

def especialidade_detalhe(request,pk):
	dados = {}
	dados['especialidade'] = Especialidade.objects.get(id=pk)
	dados['profissionais_lista'] = Profissional.objects.all()
	return render(request,'profissionais_lista.html',dados)

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


	def post(self, request):
		form = BuscarProfissionalForm(request.POST)
		if form.is_valid():
			dados_form = form.data
			esp = Especialidade.objects.filter(nomeEspecialidade__icontains= dados_form['busca'])
			prof = Profissional.objects.filter(especialidade= esp)

			return render(request, 'busca.html', {'profissionais': prof})

class BuscarCidadeView(View):


	def post(self, request):
		form = BuscarCidadeProfForm(request.POST)
		if form.is_valid():
			dados_form = form.data
			cid = Cidade.objects.filter(nomeCidade__icontains= dados_form['busca'])
			loc = Local.objects.filter(cidade=cid);
			prof = Profissional.objects.filter(local=loc)

			return render(request, 'busca.html', {'profissionais': prof})
