from django.contrib import admin
from .models import User, Post, Response


admin.site.register(Post)
admin.site.register(Response)
admin.site.register(User)
