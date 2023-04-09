from django.contrib import admin

# import Post
from .models import Post

# edit the admin user interface
class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {"slug":('title',)}


admin.site.register(Post, PostAdmin)
