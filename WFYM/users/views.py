from django.shortcuts import render,redirect
from .forms import ChildRegisterForm, PGRegisterForm
from .models import CustomUser
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def register(request):
    return render(request, 'users/register.html')

def child_register(request):
    if request.method == 'POST':
        form = ChildRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            childname = form.cleaned_data.get('first_name')
            messages.success(request, f'Account for: {childname} created as child account')
            return redirect('login-page')
    else:
        form = ChildRegisterForm()

    return render(request, 'users/child_register.html',{'form':form})

def pg_register(request):
    if request.method == 'POST':
        form = PGRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            pgname = form.cleaned_data.get('first_name')
            messages.success(request, f'Account for: {pgname} created as parent account')
            return redirect('login-page')
    else:
        form = PGRegisterForm()

    return render(request, 'users/pg_register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.is_guardian_or_parent:
                return redirect('pghome-page')
            elif user.is_child:
                return redirect('chhome-page')
            else:
                return redirect('adm-page')
        else:
            return render(request, 'users/login.html',{'error':'email or password is incorrect.'})
    else:
        return render(request, 'users/login.html')
