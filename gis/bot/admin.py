from django.contrib import admin
from .models import KNDhistor, DIPhistor, MKDhistor, Usersbot, Konfbot
# Register your models here.

@admin.register(KNDhistor)
class KNDhistorAdmin(admin.ModelAdmin):
    list_display = ('date', 'allz', 'procall', 'vrproc', 'doproc', 'coproc', 'neproc', 'times',)
    list_display_links = ('date', 'allz', 'times',)
    search_fields = ('date',)
    exclude = ('day', 'month', 'year',)
    actions = ('sootv',)

    def procall(self, rec):
        return f'{round(((int(rec.complete) + int(rec.netreb)) * 100) / int(rec.allz))}'
    procall.short_description = 'Процент выполненого'
    def vrproc(self, rec):
        return f'{rec.vrabote}  ({rec.vraboteproc}%)'
    vrproc.short_description = 'В работе'
    def doproc(self, rec):
        return f'{rec.dost}  ({rec.dostproc}%)'
    doproc.short_description = 'Доступно'
    def coproc(self, rec):
        return f'{rec.complete}  ({rec.completeproc}%)'
    coproc.short_description = 'Выполнено'
    def neproc(self, rec):
        return f'{rec.netreb}  ({rec.netrebproc}%)'
    neproc.short_description = 'Не ребуются'

    def sootv(self, request, queryset):
        for rec in queryset:
            temp = rec.date.split('.')
            rec.day = temp[0]
            rec.month = temp[1]
            rec.year = temp[2]
            rec.save()
        self.message_user(request, 'Действие выполнено')
    sootv.short_description = 'Привести запись в соответсвие'

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
    activ.short_description = 'Активировать учетные записи'

    def deactiv(self, request, queryset):
        for rec in queryset:
            rec.status = '0'
            rec.save()
        self.message_user(request, 'Действие выполнено')
    deactiv.short_description = 'Деактивировать учетные записи'

@admin.register(Konfbot)
class UsersbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'role',)
    list_display_links = ('id', 'name', 'status', 'role',)
    search_fields = ('id', 'name', 'status', 'role',)
