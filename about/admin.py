from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    summernote_fields = ('content',)
