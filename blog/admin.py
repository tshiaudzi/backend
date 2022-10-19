import email
from django.contrib import admin

# Register your models here.
from  .models import Post, book,Comment

admin.site.register(book)
admin.site.register(Comment)
@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status',)
    list_filter = ('status','create','author','publish')
    search_fields =('title','body')
    prepopulated_fields ={'slug':('title',)}
    raw_id_fields =('author',)
    date_hierarchy= 'publish'
    ordering = ('status','publish')


class commentAdmin(admin.ModelAdmin):
    list_display =('name','email','created','activated',)
    list_filter =('active','created','updated',)
    search_fields = ('name','email','body',)