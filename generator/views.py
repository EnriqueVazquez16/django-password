from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,"generator/home.html")
def password(request):


    letras=list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('uppercase'):
        letras.extend(list("ABCDEFGHIJKLMNOPQRSTUVXYZ"))
    if request.GET.get('Specials'):
        letras.extend(list("°!$%&/="))
    if request.GET.get('numbers'):
        letras.extend(list("123456789"))



    largo=int(request.GET.get('length'),12)
    finalpassword=''


    for i in range(largo):
        finalpassword+=random.choice(letras)

    return render(request,'generator/password.html',{'password':finalpassword})
def about(request):
    return render(request,"generator/about.html")