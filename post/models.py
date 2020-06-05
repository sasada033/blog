from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField


User = get_user_model()


class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'


class Post(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = MarkdownxField(verbose_name='本文', help_text='Markdown形式で記入')
    page_views = models.IntegerField(verbose_name='ページビュー数')

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='最終更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Post'

    def __str__(self):
        return self.title
