from django.contrib import admin
from .models import Melcom
# Register your models here.
class MelcomAdmin(admin.ModelAdmin):
    search_fields = ('productName',)

admin.site.register(Melcom, MelcomAdmin)