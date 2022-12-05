from django.contrib import admin

# Register your models here.
from oddam_app.models import Institution

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass