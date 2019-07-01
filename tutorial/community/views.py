from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request): #write with user request
    form = Form()
    #send form data to write.html template
    return render(request, 'write.html',{'form':form})