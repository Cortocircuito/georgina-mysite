from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'text',)
    search_fields = ('title', 'text',)
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    fields = ('title', 'author', 'text', 'published_date',)


admin.site.register(Post, PostAdmin)
