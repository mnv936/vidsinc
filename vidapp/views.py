from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.

def index(request):
    return render(request, "vidapp/index.html")


def watch(request,videoID):
    #if(request.method == 'POST'):
        #if(request.POST['videoID']):
            #videoID = request.POST['videoID']
            return render(request, "vidapp/watch2.html", {'videoID':videoID})
