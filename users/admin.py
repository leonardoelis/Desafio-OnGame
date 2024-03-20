from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User

    readonly_fields = ['date_joined', 'change_date']
    ordering = ['email']
    list_display = ['email', 'first_name', 'last_name', 'gender', 'birth_date']

    fieldsets = [
        (
            'Informações de Acesso', {'fields': ['email', 'password']}
        ),
        (
            'Informações Pessoais', {'fields': ['first_name', 'last_name', 'gender', 'birth_date']}
        ),
        (
            'Permissões', {'fields': ['is_active', 'is_admin', 'is_staff', 'is_superuser']}
        ),
        (
            'Datas Importantes', {'fields': ['date_joined', 'change_date']}
        )
    ]

    add_fieldsets = [
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'first_name', 'last_name', 'gender', 'birth_date', 'password1', 'password2'),
            },
        ),
    ]


admin.site.register(User, CustomUserAdmin)
