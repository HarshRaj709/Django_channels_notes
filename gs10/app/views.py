from django.shortcuts import render

# Create your views here.
def home(request,group_name):
    print(group_name)
    return render(request,'app/home.html',{'groupname':group_name})