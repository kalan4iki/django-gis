from django.contrib import admin
from .models import KNDhistor, DIPhistor, MKDhistor, Usersbot, Konfbot
# Register your models here.

@admin.register(KNDhistor)
class KNDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'allz', 'vrabote', 'dost', 'complete', 'netreb', 'times',)
    list_display_links = ('date', 'allz', 'vrabote', 'dost', 'complete', 'netreb', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)

@admin.register(DIPhistor)
class DIPhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_editable = ('complete', 'proc',)
    list_display_links = ('date', 'maxdvor', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)

@admin.register(MKDhistor)
class MKDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_editable = ('complete', 'proc',)
    list_display_links = ('date', 'maxdvor', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)

@admin.register(Usersbot)
class UsersbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    list_display_links = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    search_fields = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)

@admin.register(Konfbot)
class UsersbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'role',)
    list_display_links = ('id', 'name', 'status', 'role',)
    search_fields = ('id', 'name', 'status', 'role',)

'''
admin.site.register(Usersbot, UsersbotAdmin)
admin.site.register(KNDhistor, KNDhistorAdmin)
admin.site.register(DIPhistor, DIPhistorAdmin)
admin.site.register(MKDhistor, MKDhistorAdmin)
'''
