from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Post, Comment, Category, Subcategory

class SubcategoryAdmin(ModelAdmin):
    model = Subcategory
    menu_label = 'Subcategories'
    menu_icon = 'tag'
    add_to_settings_menu = False
    exclude_from_explorer = False

class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = 'Categories'
    menu_icon = 'tag'
    menu_order = 700
    add_to_settings_menu = False
    exclude_from_explorer = False

class PostAdmin(ModelAdmin):
    model = Post
    menu_label = 'Blog Post'
    menu_icon = 'pilcrow'
    menu_order = 600
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('author', 'title', 'category', 'status')
    list_filter = ('category', 'subcategory', 'status')
    search_fields = ('author', 'title')

class CommentAdmin(ModelAdmin):
    model = Comment
    menu_label = 'Post Comment'
    menu_icon = 'openquote'
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('author', 'date_created', 'content', 'post')
    search_fields = ('post')

modeladmin_register(CategoryAdmin)
modeladmin_register(SubcategoryAdmin)
modeladmin_register(CommentAdmin)
modeladmin_register(PostAdmin)
