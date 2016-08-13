from django.shortcuts import render
from especialidades.models import  Especialidade
from profissionais.models import  Profissional

# Create your views here.

def index(request):
	dados = {}
	dados['lista_profissionais'] = Profissional.objects.order_by('nome')
	dados['lista_especialidades'] = Especialidade.objects.order_by('nomeEspecialidade')
	return render(request, 'profissionais_pesquisa.html', dados)

def busca(request):
	try:
		nome_profissional = request.GET['profissional']
		profissional = Profissional.objects.get(nome=nome_profissional)
		return render(request,'resposta.html',{'object':profissional})
	except Exception:
		return render(request,'msg_erro.html')

def especialidade_detalhe(request,pk):
	dados = {}
	dados['especialidade'] = Especialidade.objects.get(id=pk)
	dados['profissionais_lista'] = Profissional.objects.all()
	return render(request,'profissionais_lista.html',dados)


	

