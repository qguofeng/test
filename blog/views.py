from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import logging
logger = logging.getLogger('blog.views')
# Create your views here.

def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC' : settings.SITE_DESC,
    }
def index(request):

    try:
        #分类数据获取
        #category_list = Catagory.objects.all()
        #广告数据
        #最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list,10)
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            articles = paginator.page(1)
        #文章归档
        #1、获取文章的年份和月份
        for a in Article.object.distinct_data():
            print(a)
    except Exception as e:
        logger.error(e)

        """
    article_list = Article.objects.all()
    paginator = Paginator(article_list,10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
        """
    return render(request,'index.html',locals())
    #return  render(request,'base.html',locals())