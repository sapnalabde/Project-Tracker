from unicodedata import name
from venv import create
from django.db import models



from django.contrib.auth.models import User

from accounts.models import Vertical
# Create your models here.
PROJECT_TASK_STATUS=((0,"Initiated"),(1,"In progress"),(3,"Completed"))
PRIORITY_TYPE=((1,"Low"),(2,"Medium"),(3,"High"))
APPROVAL_STATUS=((1,"Pending"),(2,"Approved"),(3,"Rejected"))
PROJECT_STATUS=((1,"Initiated"),(2,"On going"),(3,"On Hold"),(4,"Completed"))
PROJECT_TYPE=((1,"POC"),(2,"PO"),(3,"ECIF"),(4,"DEMO"),(5,"Initiative"),(6,"Development"))
TASK_TYPE=((1,"Internal Meeting"),(2,"External Meeting"),(3,"Training"),(4,"Task"))

class Project(models.Model):
    project_title=models.CharField(max_length = 100)
    client_Name= models.CharField(max_length = 100, null=True, blank=True)
    creator= models.CharField(max_length = 100)
    
    vertical=models.ForeignKey(Vertical,on_delete=models.CASCADE,blank=True)
    
    CsOwner=models.ForeignKey(User, on_delete=models.CASCADE)
    manager=models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
    priority=models.IntegerField(choices=PRIORITY_TYPE,default=1,null=True,blank=True)
    project_type=models.IntegerField(choices=PROJECT_TYPE,default=1,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True) 
    remark = models.TextField(null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    approval_status=models.IntegerField(choices=APPROVAL_STATUS,default=1,null=True,blank=True)
    project_status=models.IntegerField(choices=PROJECT_STATUS,default=1,null=True,blank=True)
    attachment = models.FileField(upload_to='media')




    def __str__(self):
        return self.project_title
    
    
class ProjectTeam(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    assign_to= models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    remark=models.TextField(null=True,blank=True)
    attachment = models.FileField(upload_to='media')
     
     
     
     
class Task(models.Model):
    creater=models.CharField(max_length = 100)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    task_type=models.IntegerField(choices=TASK_TYPE,default=1,null=True,blank=True)
    task_description=models.TextField(null=True,blank=True)
    Collaborated_with=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    task_status=models.IntegerField(choices=PROJECT_TASK_STATUS,default=1,null=True,blank=True)
    effort_hours=models.IntegerField()
    
class Teammember(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    m1=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    m2=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name="m2")
    m3=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True,related_name="m3")
    m4=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name="m4")

class Review(models.Model):
    name= models.CharField(max_length = 100)
    comments=models.TextField(max_length=1000)
    rating=models.IntegerField(default=0)