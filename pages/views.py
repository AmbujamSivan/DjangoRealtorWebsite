from django.shortcuts import render
from django.http import HttpResponse

#View for Index page
def index(request):
    #return HttpResponse('<h1>"This is a page"</h1>')
    return render(request,'pages/index.html')

def about(request):
     return render(request,'pages/about.html')