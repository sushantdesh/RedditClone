from django.contrib import admin

# Register your models here.
from .models import Posts
from .models import Comment
admin.site.register(Posts)
admin.site.register(Comment)
