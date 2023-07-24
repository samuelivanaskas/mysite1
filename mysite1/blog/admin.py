from django.contrib import admin

# Register your models here.
from models import Post

post = Post.objects.create(title='first post blog', author=user, content='my first blog content')
