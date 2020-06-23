import logging
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostSearchForm, InquiryForm
from taggit.models import Tag


logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(is_public=True).select_related('user',).prefetch_related('tags',)
    ordering = '-created_at'
    paginate_by = 5
    template_name = 'post/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        form = PostSearchForm(self.request.GET or None)
        tag = self.kwargs.get('tag')

        if self.request.path == '/trend/':
            queryset = queryset.order_by('-page_view')

        if tag:
            queryset = queryset.filter(tags=get_object_or_404(Tag, name=tag))
            messages.success(self.request, '「{}」の記事 - {}件'.format(tag, queryset.count()))
            return queryset

        elif form.is_valid():
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                queryset = queryset.filter(
                    Q(title__icontains=key_word) | Q(content__icontains=key_word)
                )
                messages.success(self.request, '「{}」の検索結果 - {}件'.format(key_word, queryset.count()))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.kwargs.get('tag') and not self.request.GET.get('key_word'):
            context['is_top'] = True
        if self.request.path == '/trend/':
            context['is_trend'] = True

        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'


class InquiryView(generic.FormView):
    template_name = 'post/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('post:inquiry')

    def form_valid(self, form):
        form.send_email(self.request)
        messages.success(self.request, '管理人宛にメールを送信しました。お問い合わせありがとうございます。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class PrivacyPolicyView(generic.TemplateView):
    template_name = 'post/privacy.html'


class ProfileView(generic.TemplateView):
    template_name = 'post/profile.html'
