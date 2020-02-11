from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'post']

admin.site.register(Comment, CommentAdmin)

