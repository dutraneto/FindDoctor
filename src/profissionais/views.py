from django.shortcuts import render
from especialidades.models import  Especialidade

# Create your views here.

def index(request):

	return render(request, 'index.html', {"especialidade": Especialidade.objects.all()})
