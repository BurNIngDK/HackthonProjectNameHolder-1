from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Group(models.Model):
	name = models.CharField(max_length=30)
	private = models.BooleanField()
	users = models.ManyToManyField(User)
	weird = models.IntegerField(default=0)
	def __str__(self):
		return self.name

	def group_ui(request, group_id):
		return HttpResponse("You're currently inside UI of group %s." % group_id)

	def group_chat_room(request, group_id):
		return HttpResponse("You're currently inside group %s chat room." % group_id)
