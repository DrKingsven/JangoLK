from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'status']

    fieldsets = UserAdmin.fieldsets + (
        ('Реквизиты 1С', {'fields': ('status',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Реквизиты 1С', {'fields': ('status',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)
    list_filter = ('status',)


admin.site.register(CustomUser, CustomUserAdmin)
