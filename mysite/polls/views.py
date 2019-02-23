from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
# Create your views here.


def index(request):
	group_name_list = Group.objects.order_by('-name')[:10]
	context = {'group_name_list': group_name_list}
	return render(request, '/registration/user_test.html', context)
