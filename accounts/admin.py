from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name','username', 'email', 'contact_no', 'last_login', 'is_active')
    list_display_links = ('first_name', 'last_name', 'email')
    readonly_fields = ('last_login', "date_joined",)
    ordering = ('-date_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
