from django.shortcuts import render

# Create your views here.
def chhome(request):
    return render(request, 'work/child_home.html')

def pghome(request):
    return render(request,'work/parent_home.html')
def adm(request):
    return render(request,'work/adm.html')
