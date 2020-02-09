from django.contrib import admin
from .models import Post, Comment, About_me,Title
from django.utils.html import format_html

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] 

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

    show_link.short_description = "URL"
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
admin.site.register(Comment, CommentAdmin)


admin.site.register(About_me)
admin.site.register(Title)

admin.site.register(Post, PostAdmin)

