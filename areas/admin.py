from django.contrib import admin
from areas.models import Area

# Register your models here.
# class AreaAdmin(admin.ModelAdmin):

    # list_filter = ['nomeArea']

    # class Meta:
    #     model = Area


admin.site.register(Area)
