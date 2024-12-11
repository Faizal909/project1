from django.shortcuts import render,redirect
from app2.models import table
from app2.form import studytable
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.


def home(request):
    return render(request, 'home.html')
def form(request):
    a=studytable()
    if request.method=='POST':
        b=studytable(request.POST)
        if b.is_valid():
            b.save()
            return HttpResponse('Signed up successfully')
    return render(request, 'form.html')

def login(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['password']
        try:
            q=table.objects.get(username=a)
        except table.DoesNotExist:
            return HttpResponse('Invalid username or password')
        if q.password==b:
            request.session['member_id']=q.id
            return render(request, 'afterlogin.html')
        else:
            return HttpResponse(' Invalid username or password ')
    return render(request, 'login.html')
def afterlogin(request):
    return render(request,"afterlogin.html")
def new_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("afterlogin")
        else:
            return HttpResponse("Invalid credentials")
    return render(request,"new_login.html")
def data(request):
    return render(request, 'data.html')