from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models.user import User
from .models.spot import Spot

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    
    list_display = ['id', 'email', 'is_superuser', 'last_login']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Spot)