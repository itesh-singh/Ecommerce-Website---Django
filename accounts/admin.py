from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):

    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'date_joined',
        'is_active'
    )

    list_display_links = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    # ✅ make fields read only
    readonly_fields = ('password', 'last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'username', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superadmin')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    filter_horizontal = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)
