from django.shortcuts import render


# Create your views here.
def master(req):
    return render(req,'master.html')
def home(req):
    return render(req,'index.html')
def contact(req):
    return render(req,'contact.html')
