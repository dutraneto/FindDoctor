from django.contrib.auth.models import User, Group
from profissionais.models import Profissional
from especialidades.models import Especialidade
from estabelecimentos.models import Local, Cidade, Estado
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profissional
        fields = ('id', 'especialidade', 'nome', 'sobrenome', 'codConselho', 'local')


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('id', 'nomeEspecialidade')


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ('id', 'nomeLocal', 'cnpj', 'logradouro', 'numero',
                      'bairro', 'cep', 'cidade', 'telefone')


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id', 'nomeCidade')
