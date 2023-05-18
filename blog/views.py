from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post
# Create your views here.

posts=[
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'Content':'lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum',
        'date_post':'August-27-2018'
    },
    {
        'author':'Panji MS',
        'title':'Blog Post 2',
        'Content':'lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum',
        'date_post':'September-29-2018'
    }
]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
        #'posts':posts
        'posts':Post.objects.all()
    }
    '''
    templateData = {
        key : value, ##the key is accessed in the template page
    } 
    '''    
    return render(request, 'blog/home.html', context)


def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html' ,{'title':'About'})