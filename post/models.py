from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager


class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = MarkdownxField(verbose_name='本文', help_text='Markdown形式で記入')
    tags = TaggableManager(blank=True)
    is_public = models.BooleanField(verbose_name='公開設定', default=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='最終更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title
