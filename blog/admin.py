from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
from django.db import models

admin.site.register(Post)
admin.site.register(Movies)
admin.site.register(Sliders)
admin.site.register(Advt)


