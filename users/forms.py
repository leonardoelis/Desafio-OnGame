from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        gender_choices = [
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
            ('NI', 'Prefiro não informar')
        ]
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender', 'birth_date']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'gender': forms.Select(choices=gender_choices),
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Insira sua senha'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme sua senha'})


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        gender_choices = [
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
            ('NI', 'Prefiro não informar')
        ]
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender', 'birth_date']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'gender': forms.Select(choices=gender_choices),
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance
        if email != user.email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este email já está em uso')

        return email
