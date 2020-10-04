from django.contrib import admin

from .models import Comment


# user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
# content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
# object_id = models.PositiveIntegerField()
# content_object = GenericForeignKey('content_type', 'object_id')
# content = models.TextField()
# parent = models.ForeignKey("self", null=True, black=True)
#

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'content_object']
    list_filter = ['user__username']

    search_fields = ['content', 'user__username']

    class Meta:
        model = Comment


admin.site.register(Comment, CommentModelAdmin)
