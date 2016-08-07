from django.contrib import admin
from estabelecimentos.models import Local, Estado, Cidade
# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Local)
