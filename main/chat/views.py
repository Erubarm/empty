from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def start(request):
    return render(request, 'start.html')


def log_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user-name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=user_name)
        except:
            messages.error(request, 'Такого пользователя нет')
      ###################################################################
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'chat/log-user.html', {'log' : 'login'})

def log_out(request):
    logout(request)
    return redirect('start')

def reg_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # TODO
            login(request, user)
            return redirect('index')

    return render(request, 'chat/reg-user.html', {'form' : form})

@login_required(login_url='log-in')
def index(request):
    find = request.GET.get('find') if request.GET.get('find') != None else '' ###########
    chats = Chat.objects.filter(name__icontains=find)
    context = {'chats':chats,
               'find':find}
    return render(request, 'chat/index.html', context)

@login_required(login_url='log-in')
def chat(request, Id):
    chat =  Chat.objects.get(id=Id)
    messages = chat.message_set.all().order_by('date')

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            chat = chat,
            words = request.POST.get('words')
        )
        return redirect('chat', Id=chat.id)
    context = {'chat' : chat,
               'message' : messages,}
    return render(request, 'chat/chat.html', context)

@login_required(login_url='log-in')
def del_message(request, Id, id):
    message = Message.objects.get(id=Id)
    if request.method == 'POST':
        message.delete()
        return redirect('chat', id)
    return render(request, 'chat/del-message.html', {'message':message})


@login_required(login_url='log-in')
def chat_up(request, Id):
    chat = Chat.objects.get(id=Id)

    if request.method == 'POST':
        chat.name = request.POST.get('name')
        chat.text = request.POST.get('text')
        chat.save()
        return redirect('index')

    return render(request, 'chat/create-chat.html')

@login_required(login_url='log-in')
def create_chat(request):
    if request.method == 'POST':
        chat = Chat.objects.create(
            author = request.user,
            name = request.POST.get('name'),
            text = request.POST.get('text')
        )
        return redirect('index')
    return render(request, 'chat/create-chat.html')

@login_required(login_url='log-in')
def del_chat(request, Id):
    chat = Chat.objects.get(id=Id)
    if request.method == 'POST':
        chat.delete()
        return redirect('index')
    return render(request, 'chat/delete-chat.html', {'chat':chat})



