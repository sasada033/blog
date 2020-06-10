from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.db.models import Count
from markdownx.utils import markdownify
from post.models import Post
from taggit.models import Tag
from post.forms import PostSearchForm


register = template.Library()


@register.filter
def markdown_to_html(text):
    """マークダウンをhtmlに変換する。"""
    return mark_safe(markdownify(text))


@register.filter(is_safe=True)
@stringfilter
def split_timesince(value, delimiter=None):  # timesince を分割してシンプルに表示する
    return value.split(delimiter)[0]


@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()


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
    posts = \
        Post.objects.filter(is_public=True).order_by('-created_at').select_related('user',).prefetch_related('tags',)[:5]

    context = {'new_posts': posts}
    return context


@register.inclusion_tag('post/search_form.html')
def create_search_form(request):
    form = PostSearchForm(request.GET or None)

    context = {'form': form}
    return context
