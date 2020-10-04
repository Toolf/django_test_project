from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'owner']
    list_display_links = ['created_at']
    list_editable = ['title']
    list_filter = ['title', 'created_at', 'owner__username']

    search_fields = ['title', 'content', 'created_at', 'owner__username']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)

