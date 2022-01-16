"""
To render HTML Web Pages!
"""

import random
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template



def home_view(request, *args, **kwargs):
    """
    Take in a request
    return html as response
    """

    print(id)

    #hard coded
    name = "Aman" 

    #pseudo random
    random_id = random.randint(1, 3) 

    my_list= [13, 423, 54, 346, 235, 346]
    article_queryset = Article.objects.all()  #this is a queryset, not a list, but behaves like a list
    my_list = article_queryset

    #from database
    article_obj = Article.objects.get(id=random_id)
    article_title = article_obj.title
    article_content = article_obj.content

    #django templates
    # H1_STR = f"""<h1>{article_title} (id: {article_obj.id})</h1>"""
    # P_STR = f"""<p>{article_content}</p>"""
    # HTML_STRING = H1_STR + P_STR

    #ALT1
    
    context = {
        "objectlist": my_list,
        "title": article_title,
        "content": article_content,
        "id": article_obj.id
    }
    
    # HTML_STRING = """#<h1>{title} (id: {id})</h1>
    # <p>{content}!</p>
    # """.format(**context)
    

    #ALT2
    """
    f = open("my-templete.html", 'r')
    string = f.read()
    HTML_STRING = string.format(**context)
    """

    #ALT3
    HTML_STRING = render_to_string("home-view.html", context = context)

    #ALT4
    """
    tmpl = get_template("home-view.html")
    tmpl_string = tmpl.render(context = context)
    """

    

    return HttpResponse(HTML_STRING)