from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
import ast
from django.http import HttpResponseRedirect

def index2(request):
    print(request)
    cc = {
        'aa':'111',
        'bb':'222'
    }
    return HttpResponse(json.dumps(cc),content_type="application/json")


def index(request):
    articles = models.Artical.objects.all()
    return render(request,'blog/index.html',{'articles':articles})


def article_page(request,article_id):
    article = models.Artical.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})


def sqltest(request):
    c1 = models.ArticalTest.objects.filter(content__contains='s').exclude(content='s10')
    c1 = models.ArticalTest.objects.filter(id__gt=13)
    c2 = []
    for item in c1:
        c2.append({'id':item.id,'title':item.title,'content':ast.literal_eval(item.content)})

    #models.ArticalTest.objects.create(title='xxx',content='666xxx')
    #models.ArticalTest.objects.filter(id=11).delete()

    c3 = models.ArticalTest.objects.filter(content__contains='s')

    c4 = models.ArticalTest.objects.filter(content__gt=3000)

    c5 = ['5','6','7','8']
    #models.ArticalTest.objects.create(title="test-test",content=json.dumps(c5))


    #return HttpResponse(c4)
    return HttpResponse(json.dumps(c2), content_type="application/json")

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Artical.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})


def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id','0')

    if article_id == '0':
         models.Artical.objects.create(title=title,content=content)
         return HttpResponseRedirect('/blog/index')

    article = models.Artical.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})
   # return HttpResponseRedirect('/blog/article_page',{'article':article})