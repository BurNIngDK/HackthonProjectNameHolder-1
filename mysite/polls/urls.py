from django.urls import path
from .models import Group

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<string:group_id>/', Group.group_ui, name='group_ui'),
    path('<string:group_id>/chatroom/', Group.group_chat_room, name='group_chat_room'),
]