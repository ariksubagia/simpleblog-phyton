from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ( 'title', 'slug', 'content', 'cover', 'created_at' )
    list_display = ( 'title', 'summary', 'created_at' )
    readonly_fields = ( 'created_at', )
    prepopulated_fields = {
        'slug' : ( 'title',  )
    }

    def save_model(self, request, obj, form, change):
        obj.poster_id = request.user.id
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Article, ArticleAdmin)

admin.site.site_header = 'BITBlog Admin'