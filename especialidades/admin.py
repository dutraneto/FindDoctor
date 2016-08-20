from django.contrib import admin
from especialidades.models import Especialidade

class EspecialidadeModelAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ["nomeEspecialidade"]
    list_filter = ["nomeEspecialidade"]

    class Meta:

        model = Especialidade
#     search_fields = ["especialidade"]

admin.site.register(Especialidade, EspecialidadeModelAdmin)
