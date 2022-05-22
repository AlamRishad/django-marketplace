from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Freelancer(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=32)
     balance=models.FloatField()
     skills=models.CharField(max_length=100)

class Client(models.Model):
     name = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=32)
     balance=models.FloatField()

class Job_Detail(models.Model):
     Job_title = models.CharField(max_length=100)
     Job_desc = models.TextField()
     Job_Date=models.DateTimeField(default=timezone.now)
     Job_Budget=models.FloatField()
     Job_Created=models.ForeignKey(to='Client', on_delete=models.CASCADE)
     Job_Awarded= models.BooleanField()

class Job_Bid(models.Model):
      freelancer_id = models.ForeignKey(to='Freelancer', on_delete=models.CASCADE)
      proposal_message=models.CharField(max_length=1000)
      proposed_amount=models.FloatField()
      job_id = models.ForeignKey(to='Job_Detail', on_delete=models.CASCADE)
     

class Job_Awarded(models.Model):
     job_id= models.ForeignKey(to='Job_Detail', on_delete=models.CASCADE)
     client_id= models.ForeignKey(to='Client', on_delete=models.CASCADE)
     freelance_id=models.ForeignKey(to='Freelancer', on_delete=models.CASCADE)
     bidding_id=models.ForeignKey(to='Job_Bid', on_delete=models.CASCADE)
     
class Blog(models.Model):
     blog_title= models.CharField(max_length=100)
     blog_date=models.DateTimeField(default=timezone.now)
     blog_desc = models.TextField()
     blog_writer=models.CharField(max_length=100)

class Blog_Comment(models.Model):
     blog_comment = models.ForeignKey(to='Blog', on_delete=models.CASCADE)
     comment_writer = models.CharField(max_length=100)
     comment_date=models.DateTimeField(default=timezone.now)
     comment_desc = models.TextField()
    
# class Transaction(models.Model):
#      Amount = models.FloatField()
#      Job=models.ForeignKey(to='Job_Detail', on_delete=models.CASCADE)
#      Freelancer=models.ForeignKey(to='Freelancer', on_delete=models.CASCADE)
     
   

