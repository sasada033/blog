from django.core.management.base import BaseCommand
from post.models import Post
from .analytics_api import get_trend_articles


class Command(BaseCommand):
    """コマンド定義クラス"""

    def handle(self, *args, **options):
        """コマンド定義関数"""
        updates = []
        for pk, page_view in get_trend_articles():
            post = Post(pk=pk, page_view=page_view)
            updates.append(post)
        Post.objects.bulk_update(updates, fields=['page_view'])
