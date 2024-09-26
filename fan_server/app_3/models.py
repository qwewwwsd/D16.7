from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Post(models.Model):

    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастер заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = RichTextUploadingField(null=True, config_name='default',)
    category = models.CharField(max_length=20, choices=TYPE, default='tank')

    def get_absolute_url(self): return reverse('post_id', args=[str(self.pk)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
