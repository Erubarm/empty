from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.start, name='start'),
    path("chat-list/", views.index, name = 'index'),
    path("chat/<str:Id>/", views.chat, name = 'chat'),
    path("create-chat/", views.create_chat, name = "create-chat"),
    path("delete-chat/<str:Id>/", views.del_chat, name="delete-chat"),
    path("del-message/<str:Id>/<str:id>/", views.del_message, name="del-message"),
    path("chat-up/<str:Id>/", views.chat_up, name="chat-up"),
    path("log-in/", views.log_user, name='log-user'),
    path("reg/", views.reg_user, name='reg-user'),
    path("log-out/", views.log_out, name='log-out'),
]