from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Grocery
from .forms import GroceryForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import auth

def view(request):
    grocery = Grocery.objects.all()
    if request.method == "POST":
        displaydate = request.POST.get('displaydate')
        grocery = Grocery.objects.filter(date=displaydate)
        return render(request,'view.html',{'grocery':grocery})
    else:
        grocery = Grocery.objects.all()
        return render(request,'view.html',{'grocery':grocery})

def add(request):
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = GroceryForm()
    return render(request, 'add.html', {'form': form})

@csrf_exempt
def update(request,id):
    if request.method == 'POST':
        editrow = Grocery.objects.get(pk=id)
        form = GroceryForm(request.POST, instance=editrow)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        editrow = Grocery.objects.get(pk=id)
    form = GroceryForm(instance=editrow)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        delrow= Grocery.objects.get(pk=id)
        delrow.delete()
        return HttpResponseRedirect('/')



@csrf_exempt
def signup(request):
    if request.method =="POST":
        if request.POST['password1']==request.POST['password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{"error":"Username is already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])

                return redirect('/')
        else:
            return render(request,'signup.html',{'error':"Password does not matched"})
    else:
        return render(request,'signup.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': "Username or password is incorrect"})
    else:
        return render(request, 'login.html')

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')


