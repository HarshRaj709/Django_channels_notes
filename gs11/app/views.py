from django.shortcuts import render
from .models import Group,Chat

# Create your views here.
def home(request,group_name):
    print(group_name)
    group = Group.objects.filter(group = group_name).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group = group)      #providing group name to chat
    else:
        group = Group.objects.create(group = group_name)
    #we can use below code then we dont need to use if else condition.
    #group, created = Group.objects.get_or_create(group=group_name)
    return render(request,'app/home.html',{'groupname':group_name,'chats':chats})