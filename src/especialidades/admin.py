from django.contrib import admin
from especialidades.models import Especialidade

# class EspecialidadeModelAdmin(admin.ModelAdmin):
#     list_display = ["especialidade"]
#     # list_filter = ["especialidade"]
#     search_fields = ["especialidade"]
admin.site.register(Especialidade)
