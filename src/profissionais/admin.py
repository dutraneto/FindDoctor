from django.contrib import admin

from especialidades.models import (Especialidade)
from .models import (Profissional)
from pessoas.models import Pessoa
# from pessoas.models import (Pessoa)
# from .models import (Usuario)
from estabelecimentos.models import (Estabelecimento)

class ProfissionalModelAdmin(admin.ModelAdmin):
	list_display = ["profissao","pessoa", "crm"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	list_filter = ["pessoa", "profissao", "especialidade", "estabelecimento"]

	search_fields = ["pessoa", "profissao", "especialidade", "crm"]

	class Meta:
		model = Profissional


# class EspecialidadeModelAdmin(admin.ModelAdmin):
#     list_display = ["especialidade"]
#     # list_filter = ["especialidade"]
#     search_fields = ["especialidade"]
#
#     class Meta:
#         model = Especialidade

# admin.site.register(Especialidade, EspecialidadeModelAdmin)
admin.site.register(Profissional, ProfissionalModelAdmin)
# admin.site.register(Usuario)
# admin.site.register(Pessoa)
