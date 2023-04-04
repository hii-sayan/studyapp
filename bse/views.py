from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn Pyhon!'},
    {'id': 2, 'name': 'Lets learn java'},
    {'id': 3, 'name': 'Lets learn sql'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'bse/home.html', context)

def room(request, pk):
    room= None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request,'bse/room.html', context)