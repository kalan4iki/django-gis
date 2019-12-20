from django.contrib import admin
from .models import KNDhistor, DIPhistor, MKDhistor, Usersbot
# Register your models here.

class KNDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_display_links = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    search_fields = ('date',)

class DIPhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_display_links = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    search_fields = ('date',)

class MKDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_display_links = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    search_fields = ('date',)

class UsersbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    list_display_links = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    search_fields = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)

admin.site.register(Usersbot, UsersbotAdmin)
admin.site.register(KNDhistor, KNDhistorAdmin)
admin.site.register(DIPhistor, DIPhistorAdmin)
admin.site.register(MKDhistor, MKDhistorAdmin)
