# Generated by Django 4.2.11 on 2024-03-20 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0002_rename_topics_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=15000, verbose_name='Comentário')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Postagem')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topic')),
            ],
        ),
    ]
