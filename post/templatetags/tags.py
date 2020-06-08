from django import template
from django.utils.safestring import mark_safe
from django.db.models import Count
from markdownx.utils import markdownify
from post.models import Post
from taggit.models import Tag


register = template.Library()


@register.filter
def markdown_to_html(text):
    """マークダウンをhtmlに変換する。"""
    return mark_safe(markdownify(text))


@register.inclusion_tag('post/aside_primary.html')
def create_tag_list():
    tags = Tag.objects.all().annotate(post_count=Count('taggit_taggeditem_items')).order_by('-post_count')
    major_tags = tags[:5]
    minor_tags = tags[5:]

    context = {
        'major_tags': major_tags,
        'minor_tags': minor_tags,
    }
    return context


@register.inclusion_tag('post/aside_secondary.html')
def create_post_list():
    posts = Post.objects.filter(is_public=True).order_by('-created_at')[:5]

    context = {
        'new_posts': posts,
    }
    return context
