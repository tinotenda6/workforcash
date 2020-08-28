from django.shortcuts import render,redirect
from .forms import ChildRegisterForm, PGRegisterForm, PGName, parent_confirm
from .models import CustomUser
from .models import ChildProfile, ParentProfile
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory

CustomUser = get_user_model()
def register(request):
    return render(request, 'users/register.html')

def child_register(request):
    if request.method == 'POST':
        form = ChildRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            childname = form.cleaned_data.get('username')
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
            pgname = form.cleaned_data.get('username',)
            messages.success(request, f'Account for: {pgname} created as parent account')
            return redirect('login-page')
    else:
        form = PGRegisterForm()

    return render(request, 'users/pg_register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.is_guardian_or_parent:
                return redirect('pghome-page')
            elif user.is_child:
                return redirect('chhome-page')
            else:
                return redirect('adm-page')
        else:
            return render(request, 'users/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'users/login.html')
        

def pgname(request):
	form = PGName(request.POST, instance = request.user.child_profile)
	if request.method == 'POST':
		if form.is_valid():
			new_par = form.save()
			return redirect('chhome-page')
		else:
			form = PGName()
	return render(request, 'users/pgname.html',{'form':form})        
     
#             
def pgconfirm(request):
	if request.method == 'POST':
		form = parent_confirm(request.POST)
		if form.is_valid():
			form.save()
			name = request.POST.get('name')
			print(name)
			return redirect('pghome-page')
	else:
		form = parent_confirm()
	return render(request, 'users/pgconf.html',{'form':form})   
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
