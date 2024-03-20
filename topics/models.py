from django.db import models
from users.models import User


class Topic(models.Model):
    subject = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Assunto')
    category = models.CharField(max_length=500, null=False, blank=False, verbose_name='Categoria')
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Postagem')
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name='Imagem')
    message = models.TextField(max_length=15000, null=False, blank=False, verbose_name='Mensagem')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    text = models.TextField(max_length=15000, null=False, blank=False, verbose_name='Comentário')
    post_date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Postagem')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
