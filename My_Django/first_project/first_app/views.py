from django.shortcuts import render
from django.http import HttpResponse
from .models import Webpage,AccessRecord
# Create your views here.

def index(request):
    #Comment here
   # return HttpResponse("Ali")

    #my_dict = {"insert_me":"Hello I am from views.py !"}
    #return render(request,'first_app/index.html',context=my_dict)
    Webpages= Webpage.objects.all()
    AccessRecords=AccessRecord.objects.all()
    my_dict = {'Webpages':Webpages,'AccessRecords':AccessRecords}
    return render(request,'first_app/index.html',my_dict)