from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import *
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','category']
    fields = ['title' ,'category','author','description','image_main','image_url','content','show_in_home_first','show_in_home','active','ads_num','post_date']
    list_display = ['title' ,'author','category','show_in_home_first','show_in_home','active']
    list_editable = ['show_in_home_first','show_in_home','active']
    list_filter = ['active','author','category','show_in_home','post_date']


admin.site.register(Post,PostAdmin)
admin.site.register(Categories)
admin.site.register(Author)
# admin.site.register(Ads)
