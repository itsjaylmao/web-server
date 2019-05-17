from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
)

class Category(models.Model):
    name = models.CharField(max_length=48)

    panels = [FieldPanel('name')]
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=48)

    panels = [FieldPanel('name')]

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextField('Content', features=[
        'h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul',
        'hr', 'link', 'image', 'embed', 'code', 'blockquote',
        'document-link', 'superscript', 'subscript', 'strikthrough'
    ])
    blurb = models.TextField(max_length=320, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+')
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', related_name='posts', on_delete=models.CASCADE)
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    read_time = models.IntegerField(null=True)
 
    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('author'),
        FieldPanel('content'),
        FieldPanel('blurb'),       
        FieldPanel('tags'),
        ImageChooserPanel('image'),
        FieldPanel('category'),
        FieldPanel('subcategory'),
        FieldPanel('read_time'),
        FieldPanel('status'),
        FieldPanel('date_published')    
]

    class Meta:
        ordering = ['-date_created']

    def publish(self):
        self.date_published = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length=64)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    panels = [
        FieldPanel('author'),
        FieldPanel('date_created'),
        FieldPanel('content'),
        FieldPanel('post'),
    ]

