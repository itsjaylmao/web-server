from django.contrib import admin
from .models import Post, Category, Subcategory,  Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date_created')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    pass

class SubcategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Comment, CommentAdmin)
