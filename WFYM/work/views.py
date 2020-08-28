from django.shortcuts import render, redirect, get_object_or_404
from users.models import ChildProfile, ParentProfile, CustomUser
from .models import Alltask, Chores
from .forms import ChoreForm, TaskForm, TaskUpdateForm
# Create your views here.
def chhome(request):
	user = request.user.child_profile  
	tasks = Chores.objects.filter(child=user)
	context = {
		'tasks':enumerate(tasks),
	}
	return render(request, 'work/child_home.html',context)

def pghome(request):
	user = request.user.parent_profile  
	kids = ChildProfile.objects.filter(parent_name=user)
	count = kids.count()
	context = {
		'kids':kids,
		'tot_kids': range(count)
	}
	return render(request,'work/parent_home.html',context)

def adm(request):
    return render(request,'work/adm.html')

def chorelist(request):
	form = ChoreForm(request.POST, user = request.user.parent_profile)
	if request.method == 'POST':
		if form.is_valid():
			new_chores = form.save()
			new_chores.parent = request.user.parent_profile
			new_chores.save()
			return redirect('pghome-page')
	else:
		form = ChoreForm(user = request.user.parent_profile)
	return render(request,'work/chores.html',{'form':form})
	
	
def task(request):
	form = TaskForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			new_task = form.save()
			new_task.parent = request.user.parent_profile
			new_task.save()
			return redirect('pghome-page')
	else:
		form = TaskForm()
	return render(request,'work/entertask.html',{'form':form})
	
def alltasks(request):
	user = request.user.parent_profile  
	tasks = Alltask.objects.filter(parent=user)
	count = tasks.count()
	context = {
		'tasks': enumerate(tasks),
		'tot_tasks': range(count)
	}
	return render(request,'work/alltasks.html',context)
	
def indcl(request, child_id):
	chil = get_object_or_404(ChildProfile,pk=child_id)
	print(child_id)
	chores = Chores.objects.filter(child=chil)
	print(chores)
	context = {
		'chores':enumerate(chores),
		'chil':chil
	}
	return render(request,'work/childchore.html',context)
	
def update(request,task_id):
	tas = get_object_or_404(Alltask, pk=task_id)
	print(tas)
	instance = Alltask.objects.get(pk=task_id)
	form = TaskUpdateForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('alltask-page')
	return render(request,'work/update.html',{'form':form})
	

def task_remove(request, chore_id, task_name, child_id):
	chore = Chores.objects.get(id=chore_id)
	print(chore)
	if request.method == 'POST':
		chore.task.remove(Alltask.objects.get(task=task_name))
		return redirect('indcl-page', child_id=child_id)
	return render(request,'work/childchore.html')


def delete_task(request,task_id):
	task = get_object_or_404(Alltask,pk=task_id)
	if request.method == 'POST':
		task.delete()
		return redirect('alltask-page')
	return render(request, 'work/alltasks.html')

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	