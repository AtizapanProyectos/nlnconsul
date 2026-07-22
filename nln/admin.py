from django.contrib import admin

from .models import Opinion


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa", "rating", "fecha", "aprobado")
    list_filter = ("rating", "aprobado")
    search_fields = ("nombre", "empresa", "opinion")