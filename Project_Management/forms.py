from ast import Pass
from dataclasses import fields
from tkinter import Widget
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django import forms
from accounts.models import Vertical
from .models import Project,ProjectTeam,Task,Teammember
from django.contrib.auth.models import  User




class Projectform(forms.ModelForm):
    
    class Meta:
        model=Project
        fields=('project_title','client_Name','creator','vertical','manager',
               'priority','project_type','start_date','end_date','remark','description',
               'approval_status','project_status','attachment','CsOwner')
        
        widgets = {
            'project_title' : forms.TextInput(attrs={'class':'form-control'}),
            'client_Name'   : forms.TextInput(attrs={'class':'form-control'}),
            'creator'       : forms.TextInput(attrs={'class':'form-control'}),
            'vertical'      : forms.Select(attrs={
                'class': 'form-control verticalElement',
                'hx-target': '#id_assignted_to',
                'hx-trigger':'change',
                'hx-swap':'innerHTML'
            }),
            
            'manager'       : forms.Select(attrs={'class': 'form-control'}),
            'priority'      : forms.Select(attrs={'class': 'form-control'}),
            'project_type'  : forms.Select(attrs={'class': 'form-control'}),
            'start_date'    : forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'end_date'      : forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'remark'        : forms.Textarea(attrs={'class': 'form-control'}),
            'description'   : forms.Textarea(attrs={'class': 'form-control'}),
            'approval_status':forms.Select(attrs={'class': 'form-control'}),
            'project_status':forms.Select(attrs={'class': 'form-control'}),
            'CsOwner':forms.Select(attrs={'class': 'form-control'}),
            'attachment'    :forms.FileInput(attrs={'class':'form-control'})
        }
        
        
class ProjectTeamform(forms.ModelForm):
    
    class Meta:
        model=ProjectTeam
        fields=('project','assign_to','remark','attachment')
        
        widgets = {
            'project' : forms.Select(attrs={'class': 'form-control'}),
            'assign_to'    : forms.Select(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
            'attachment'    :forms.FileInput(attrs={'class':'form-control'})
            
        }   
        
        
class Taskform(forms.ModelForm):

    class Meta:
        model =Task
        fields=('creater','project','date','task_type','task_description','Collaborated_with','task_status','effort_hours')



        widgets = {

            'creater'    : forms.TextInput(attrs={'class':'form-control'}),
            'project'    : forms.Select(attrs={'class': 'form-control'}),
            'date'       : forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'task_type'  : forms.Select(attrs={'class': 'form-control'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control'}),
            'Collaborated_with': forms.Select(attrs={'class': 'form-control'}),
            'task_status':forms.Select(attrs={'class': 'form-control'}),
            'effort_hours':forms.NumberInput(attrs={'class': 'form-control'})
        }   

# class Teammemberform(forms.ModelForm):
    
#     def __init__(self, *args, **kwargs):
#         super(Teammemberform, self).__init__(*args, **kwargs)

#         members = [(i.email, i.get_full_name()) for i in User.objects.all()]
#         print(f"\n Members : {members} \n")
#         self.fields['m1'] = forms.ChoiceField(
#             choices=members,
#             widget=forms.Select(attrs={'class': 'form-control', 'multiple':'true'})
#         )
    
#     class Meta:
#         model=Teammember
#         fields=('project','m1')

#         widgets={
#             'project': forms.Select(attrs={'class': 'form-control'}),
#         }

class Teammemberform(forms.ModelForm):
    
    class Meta:
        model=Teammember
        fields=('project','m1','m2','m3','m4')
        
        widgets={
            'project': forms.Select(attrs={'class': 'form-control'}),
            'm1': forms.Select(attrs={'class': 'form-control'}),
            'm2': forms.Select(attrs={'class': 'form-control'}),
            'm3': forms.Select(attrs={'class': 'form-control'}),
            'm4': forms.Select(attrs={'class': 'form-control'}),
           
        }


        