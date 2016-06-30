from django.contrib import admin

from pessoas.models import Pessoa
# from pessoas.models import (Pessoa)
# from .models import (Usuario)

class PessoaModelAdmin(admin.ModelAdmin):
	list_display = ["nome", "sobrenome"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	list_filter = ["nome", "sobrenome"]

	search_fields = ["nome", "sobrenome"]
	class Meta:
		model = Pessoa




# admin.site.register(Especialidade, EspecialidadeModelAdmin)
admin.site.register(Pessoa, PessoaModelAdmin)
# admin.site.register(Usuario)
# admin.site.register(Pessoa)
