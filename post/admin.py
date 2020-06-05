from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CustomUser, Post


admin.site.register(CustomUser)
admin.site.register(Post, MarkdownxModelAdmin)
