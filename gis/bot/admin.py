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
    list_display_links = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)
    actions = ('sootv',)

    def sootv(self, request, queryset):
        for rec in queryset:
            temp = rec.date.split('.')
            rec.day = temp[0]
            rec.month = temp[1]
            rec.year = temp[2]
            rec.save()
        self.message_user(request, 'Действие выполнено')
    sootv.short_description = 'Привести запись в соответсвие'

@admin.register(MKDhistor)
class MKDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    list_display_links = ('date', 'maxdvor', 'complete', 'proc', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)
    actions = ('sootv',)

    def sootv(self, request, queryset):
        for rec in queryset:
            temp = rec.date.split('.')
            rec.day = temp[0]
            rec.month = temp[1]
            rec.year = temp[2]
            rec.save()
        self.message_user(request, 'Действие выполнено')
    sootv.short_description = 'Привести запись в соответсвие'

@admin.register(Usersbot)
class UsersbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    list_display_links = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    search_fields = ('id', 'username', 'email', 'last_name', 'first_name', 'status', 'uuid', 'role',)
    actions = ('activ', 'deactiv',)

    def activ(self, request, queryset):
        for rec in queryset:
            rec.status = '1'
            rec.save()
        self.message_user(request, 'Действие выполнено')
    sootv.short_description = 'Активировать учетные записи'

    def deactiv(self, request, queryset):
        for rec in queryset:
            rec.status = '0'
            rec.save()
        self.message_user(request, 'Действие выполнено')
    sootv.short_description = 'Деактивировать учетные записи'

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
