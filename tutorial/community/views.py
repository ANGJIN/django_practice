from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request): #write with user request
    #clicking form button occurs POST request
    #request.mehthod is POST or GET
    if request.method == 'POST':
        #if POST, get contents of request.POST
        form = Form(request.POST)
        if form.is_valid(): #check for form data is valid
            form.save() #save data in form to DB
    else :
        #if not POST, just print form
        form = Form()
    #send form data to write.html template
    return render(request, 'write.html',{'form':form})

def list(request):
    #get list of all Aritcle
    articleList = Article.objects.all()
    #send articleList to list.html
    return render(request, 'list.html',{'articleList':articleList})