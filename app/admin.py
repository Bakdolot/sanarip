from django.contrib import admin

from .models import Culture, Farmer, Season, Plot


class CultureAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["name"]


class FarmerAdmin(admin.ModelAdmin):
    search_fields = ["full_name"]
    list_filter = ["full_name"]


class PlotAdmin(admin.ModelAdmin):
    search_fields = ["farmer__full_name", "culture__name"]
    list_filter = ["farmer__full_name", "culture__name"]


admin.site.register(Culture, CultureAdmin)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(Season)
