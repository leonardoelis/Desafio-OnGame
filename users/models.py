from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name, gender, birth_date, password):
        if not email:
            raise ValueError('Usuário precisa preencher o email')
        if not first_name:
            raise ValueError('Usuário precisa preencher o nome')
        if not last_name:
            raise ValueError('Usuário precisa preencher o sobrenome')
        if not gender:
            raise ValueError('Usuário precisa preencher o sexo')
        if not birth_date:
            raise ValueError('Usuário precisa preencher a data de nascimento')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, gender, birth_date, password):
        return self._create_user(email, first_name, last_name, gender, birth_date, password)

    def create_superuser(self, email, first_name, last_name, gender, birth_date, password):
        user = self._create_user(email, first_name, last_name, gender, birth_date, password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nome')
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Sobrenome')
    gender = models.CharField(max_length=2, null=False, blank=False, verbose_name='Sexo')
    birth_date = models.DateField(null=False, blank=False, verbose_name='Data de Nascimento')
    date_joined = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'birth_date']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

