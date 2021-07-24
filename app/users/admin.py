from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )})
    )
    list_display = ('email', 'full_name', 'is_staff')
    list_filter = []
    search_fields = ('full_name', 'email')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2'),
        }),
    )
    ordering = ('email',)