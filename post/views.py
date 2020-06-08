from django.views import generic
from .models import Post


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(is_public=True)
    ordering = '-created_at'
    paginate_by = 10
    template_name = 'post/index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'
