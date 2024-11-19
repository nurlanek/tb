from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (
    Dolboor, Project_confirmation, Negizgimaalymat,
    Kenenmaalymat, Iskeashyruuplany, Dolboordundudjeti,
    Dolboordunkomandasy, Baaloo_turuktuuluk, Tirkemeler
)

# Her model için kaynak sınıfı oluşturma
class DolboorResource(resources.ModelResource):
    class Meta:
        model = Dolboor

@admin.register(Dolboor)
class DolboorAdmin(ImportExportModelAdmin):
    resource_class = DolboorResource
    list_display = ('dolboordun_atalyshy', 'user', 'is_active', 'dolboordun_moonotu', 'dolboordun_byudzheti')
    search_fields = ('dolboordun_atalyshy', 'user__username')
    list_filter = ('is_active', 'dolboordun_geografiyalyk_ordu')
    ordering = ('-id',)

class ProjectConfirmationResource(resources.ModelResource):
    class Meta:
        model = Project_confirmation

@admin.register(Project_confirmation)
class ProjectConfirmationAdmin(ImportExportModelAdmin):
    resource_class = ProjectConfirmationResource
    list_display = ('user', 'dolboor', 'confirmation', 'created', 'is_active')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    list_filter = ('confirmation', 'is_active')
    ordering = ('-created',)

class NegizgimaalymatResource(resources.ModelResource):
    class Meta:
        model = Negizgimaalymat

@admin.register(Negizgimaalymat)
class NegizgimaalymatAdmin(ImportExportModelAdmin):
    resource_class = NegizgimaalymatResource
    list_display = ('user', 'dolboor', 'yuridikalyk_jekekishi', 'aty_jonu','mekmenin_atalyshy')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    list_filter = ('yuridikalyk_jekekishi',)
    ordering = ('-id',)

# Diğer modeller için de benzer yapı:
class KenenmaalymatResource(resources.ModelResource):
    class Meta:
        model = Kenenmaalymat

@admin.register(Kenenmaalymat)
class KenenmaalymatAdmin(ImportExportModelAdmin):
    resource_class = KenenmaalymatResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)

class IskeashyruuplanyResource(resources.ModelResource):
    class Meta:
        model = Iskeashyruuplany

@admin.register(Iskeashyruuplany)
class IskeashyruuplanyAdmin(ImportExportModelAdmin):
    resource_class = IskeashyruuplanyResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)

class DolboordundudjetiResource(resources.ModelResource):
    class Meta:
        model = Dolboordundudjeti

@admin.register(Dolboordundudjeti)
class DolboordundudjetiAdmin(ImportExportModelAdmin):
    resource_class = DolboordundudjetiResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)

class DolboordunkomandasyResource(resources.ModelResource):
    class Meta:
        model = Dolboordunkomandasy

@admin.register(Dolboordunkomandasy)
class DolboordunkomandasyAdmin(ImportExportModelAdmin):
    resource_class = DolboordunkomandasyResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)

class BaalooTuruktuulukResource(resources.ModelResource):
    class Meta:
        model = Baaloo_turuktuuluk

@admin.register(Baaloo_turuktuuluk)
class BaalooTuruktuulukAdmin(ImportExportModelAdmin):
    resource_class = BaalooTuruktuulukResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)

class TirkemelerResource(resources.ModelResource):
    class Meta:
        model = Tirkemeler

@admin.register(Tirkemeler)
class TirkemelerAdmin(ImportExportModelAdmin):
    resource_class = TirkemelerResource
    list_display = ('user', 'dolboor')
    search_fields = ('user__username', 'dolboor__dolboordun_atalyshy')
    ordering = ('-id',)
