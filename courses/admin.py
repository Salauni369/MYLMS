from django.contrib import admin
from .models import Course, Video, Document, Question

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Document)
admin.site.register(Question)