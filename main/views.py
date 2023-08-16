from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.
from .models import files,systmfile
from files import settings
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import HttpResponse

# def login(request):
#     return render(request,'login.html')
@login_required(login_url='login')
def home(request):
    name=files.objects.all()
    sys=systmfile.objects.all()
    return render(request,'file.html',{"name":name,"sys":sys})

def dlt(request):
    data=files.objects.all()
    data.delete()
    return redirect("/file")

def filedlt(request,id):
    data=files.objects.get(id=id)
    data.delete()
    return redirect("/file")

@login_required(login_url='login')
def mainview(request):
    sys=systmfile.objects.all()
    return render(request,'index.html',{"sys":sys})


def myfiles(request):
    if request.method == 'POST':
        my_files=request.FILES.get('file')
        files.objects.create(name=my_files)
        return HttpResponse('')
    return JsonResponse({'post':"false"})
    # return render(request,'.html')
