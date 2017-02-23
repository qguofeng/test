from django.contrib import admin
from blog.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor/dindeditor-all.js',
            '/static/js/kindeditor/kindeditor-all-min.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Catagory)
admin.site.register(Ad)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Links)