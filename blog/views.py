from django.shortcuts import render
from django.http import HttpResponse


posts = [{
    'author':'Adewale', 
    'title':'The Prince of Mars',
    'content':'Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.', 
    'date_posted':'January 21,2020'
},
{
    'author':'Adeleye', 
    'title':'Welcome to Saturn',
    'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.', 
    'date_posted':'January 21,2020'
}]


def home(request):
    context = {
        'posts':posts,
        'title':'Home - Chatty-web'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

