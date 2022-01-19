from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_detail_view(request, id=None):
    article_obj = None

    if id is not None:
        article_obj = Article.objects.get(id=id)
    
    print(article_obj.title)
    
    context={
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)

def article_search_view(request):

    # request.GET dictionary of queries
    article_obj = None

    try:
        query = int(request.GET.get('q')) # using request.GET["q"] sometimes gives error as it assumes that the key q is present in the dict.
    except:
        query = None

    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        'object': article_obj
    }
    return render(request, "articles/search.html", context = context)

@login_required
def article_create_view(request):
    form = ArticleForm()
    print(dir(form))
    context = {
        'form': form
    }
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_obj = Article.objects.create(title = title, content = content)
        context['title'] = title
        context['content'] = content
        context['created'] = True
        context['object'] = article_obj
    
    return render(request, "articles/create.html", context = context)

