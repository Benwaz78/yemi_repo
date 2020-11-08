from django.contrib import admin
from frontend.models import *

# Register your models here.
admin.site.site_header = 'Yemi Django'
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(AboutModel)