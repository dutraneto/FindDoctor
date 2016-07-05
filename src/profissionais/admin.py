from django.contrib import admin

# from .models import (Especialidade)
from .models import (Profissional)
# from pessoas.models import (Pessoa)
# from .models import (Usuario)

class ProfissionalModelAdmin(admin.ModelAdmin):
	list_display = ["nome", "sobrenome", "codConselho"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	list_filter = ["nome", "sobrenome", "especialidade", "area" ]

	search_fields = ["nome", "sobrenome", "especialidade", "area",  "codConselho"]

	filter_horizontal = ["especialidade", "local"]

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
