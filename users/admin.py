from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Image

@admin.register(User)
class AdminUser(UserAdmin):
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Personal info', {'fields':('first_name','last_name')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields' : ('email','password1','password2'),
        }),
    )
    list_display = ('email','first_name','last_name','is_staff')
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)


admin.site.register(Image)