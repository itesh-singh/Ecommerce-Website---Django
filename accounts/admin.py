from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

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


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="30" height="30" style="border-radius:50%;" />',
                obj.profile_picture.url
            )
        return "-"

    thumbnail.short_description = "Profile Picture"

    list_display = (
        'thumbnail',
        'user',
        'city',
        'state',
        'country',
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
