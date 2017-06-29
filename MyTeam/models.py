from django.db import models
class TeamMember(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	phone_number = models.IntegerField(default=0)
	email = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	
	    
