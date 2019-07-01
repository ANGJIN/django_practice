from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        #name of fields in community.models
        fields=['name','title','contents','url','email']