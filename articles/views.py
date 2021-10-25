from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import models
from . import create_form
def articles_list (request):
    articles=models.Articles.objects.all().order_by('date')
    args={'articles':articles}
    return render(request,'articles/articleslist.html',args)

def articles_detail (request,slug):

    # return HttpResponse(slug)
    article=models.Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
@login_required(login_url="/accounts/login")
def create_article (request):
    if request.method=='POST':
        form=create_form.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            return redirect('articles:list')
    else:
        form=create_form.CreateArticle()
    return render(request, 'articles/create_article.html',{'form':form})