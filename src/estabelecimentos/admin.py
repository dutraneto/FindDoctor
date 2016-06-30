from django.contrib import admin

from .models import Estabelecimento


class EstabelecimentoModelAdmin(admin.ModelAdmin):
	list_display = ["estabelecimento", "ddd", "telefone_1", "telefone_2"]
	# list_display_links = ["updated"]
	# list_editable = ["title"]
	list_filter = ["estabelecimento"]

	search_fields = ["estabelecimento"]

	class Meta:
		model = Estabelecimento

admin.site.register(Estabelecimento, EstabelecimentoModelAdmin)
