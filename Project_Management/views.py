from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from Project_Management.filters import Projectlist,UserFilter
from .models import Project,ProjectTeam,Task,Review
from .forms import Projectform,Taskform,ProjectTeamform,Teammemberform
from django.contrib.auth.models import  User, auth
from django.shortcuts import render,redirect,HttpResponse
from Project_Management.filters import UserFilter
from django.core.mail import EmailMessage, send_mail,EmailMultiAlternatives
from django.conf import settings 
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def mainpage(request):
    data=User.objects.all().count()
    pr=Project.objects.all().count()
    pro=Project.objects.filter(approval_status=1).count()
    user_list =Project.objects.all()
    com=Project.objects.filter(project_status=4).count()
    user_filter = UserFilter(request.GET, queryset=user_list)
    current_user = request.user
    fname = current_user.first_name
    return render(request ,'Projectmanagement/dashboard.html',{'data':data,'pr':pr,'pro':pro,'filter': user_filter,'com':com,'fname':fname})



# def project(request):
    
#     data=Project.objects.filter(active=True)
#     data=data.filter(department=Project.objects.get(user=request.user).department) | data.filter(department= request.user)
    
#     selectedowner=request.GET.get('owner',0)
#     owner = get_user_list(request.user)

#     dept=request.GET.get('department',0)
#     if int(selectedowner):
#         data=data.filter(owner=User.objects.get(id=selectedowner))
#     if int(dept):
#         data=data.filter(department__in=dept)
    

#     department= BusinessType.objects.filter(active=True)

   
#     return render(request,'myadmin/project_management/project.html',{'subuser':owner,'sel3':selectedowner,'data':data,'department':department,'selected_department':int(dept)})



def home(request):
    return render(request ,'base.html')


#----FUNCTIONS RELEATED TO PROJECT-----------#


def addproject(request): #function For adding new project
    current_user = request.user
    ffname = current_user.first_name
    intaial_data ={
        
        'creator': ffname
    }
    
    form=Projectform(initial=intaial_data)
    
    if request.method =='POST':
        
        form=Projectform(request.POST,request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)

            vertical_owner = instance.vertical.user.email
            cs_owner = instance.CsOwner.email
            project_owner = instance.manager.email

            Pro= request.POST.get('project_title')
           
            subject = "New Project Created || "+Pro
            body = {
            
			'Project Name': request.POST.get('project_title'), 
			'Client Name': request.POST.get('client_Name'), 
            'Start date': request.POST.get('start_date'),
            'End date':request.POST.get('end_date'), 
            
			}
            content = ("%s: %s" % (key, value) for (key, value) in body.items())
            msg="Dear Team,\n\nNew project has been created.Please find all the details in Project Tracker.\n\nDetails of the Project"
            w="\n\n Waiting for Admin Approval"
            message = msg+ "\n" +"\n" .join(content)+w
            from_email = settings.EMAIL_HOST_USER
            to_list = ['Jegan.rajendran@cloudstrats.com',vertical_owner, cs_owner, project_owner]
            msg = EmailMultiAlternatives(subject, message, from_email, to_list)
            # msg.attach_alternative(html_content, "text/html")
            file_stream = form.cleaned_data['attachment']
            print(f"\n Inmemory Object : {file_stream} \n")
            msg.attach(file_stream.name, file_stream.read(), file_stream.content_type)
            msg.send(fail_silently=True)
            # form.save()
            instance.save()
            
             
        return redirect('/Project_Management/projectreg/')

    return render(request,'Projectmanagement/createproject.html',{'form':form,'ffname':ffname})


def projectlist(request): #function for seeing all project
    data=Project.objects.all()
    uf=Projectlist(request.GET, queryset=data)
    
    return render(request,'Projectmanagement/projectlist.html',{'uf':uf}) 

def pendingprojectlist(request): #function for seeing all project
    data=Project.objects.filter(approval_status=1)
    uf=Projectlist(request.GET, queryset=data)
    
    return render(request,'Projectmanagement/pendingprojectlist.html',{'uf':uf}) 

def updateproject(request,id): #function for updating project details
    product=Project.objects.get(id=id)
    form=Projectform(instance=product)
    if request.method == 'POST':
        form=Projectform(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/Project_Management/projectlist/')
    file_url = product.attachment.url
    return render(request,'Projectmanagement/updateproject.html',{'form':form, 'file_url':file_url})

def deleteproject(request,id): #function for deleteing project details
    product=Project.objects.get(id=id)
    product.delete()
    return redirect('/Project_Management/projectlist/')

def attach(request,id):
    Doc = Project.objects.get(id=id)
    return render(request,'/list.html',{'i':Doc})

def projectdetail(request,id):
    Doc = Project.objects.get(id=id)
    #Doc=Project(instance=p)
    return render(request,'Projectmanagement/projectdetail.html',{'Doc':Doc})
    # Doc = ""
    # try:
    #     Doc = Project.objects.get(active=True, id=id)
    #     print(Doc)
    # except:
    #     return redirect('/Project_Management/Projectdetail/')
    
    # return render(request,'/Project_Management/projectdetail.html',{'Doc':Doc})

    

def approvallist(request):
    data = Project.objects.exclude(approval_status=2)
    return render(request,'Projectmanagement/approvallist.html',{'data':data})

def approvalpage(request,id): #function for updating project details
    product=Project.objects.get(id=id)
    form=Projectform(instance=product)
    if request.method == 'POST':
        form=Projectform(request.POST,request.FILES,instance=product)
        if form.is_valid():
            instance=form.save(commit=True)
            vertical_owner = instance.vertical.user.email
            cs_owner = instance.CsOwner.email
            project_owner = instance.manager.email

            assgin = instance.manager.first_name
            m="Dear"""+assgin +",\n\n"
            Pro= request.POST.get('project_title')
            p={Pro}
            subject = "Project approved || "+Pro
            # body = {
            
			# 'Project Name': request.POST.get('project_title')
			
			# }
            # content = ("%s: %s" % (key, value) for (key, value) in body.items())
            msg=" project is been approved please assigned team members on PM tracker and initiate the project."
            
            message = m+ "\n" +"\n" .join(p)+msg
            from_email = settings.EMAIL_HOST_USER
            to_list = ['Jegan.rajendran@cloudstrats.com',vertical_owner, cs_owner, project_owner]
            msg = EmailMultiAlternatives(subject, message, from_email, to_list)
            # msg.attach_alternative(html_content, "text/html")
            #file_stream = form.cleaned_data['attachment']
            #print(f"\n Inmemory Object : {file_stream} \n")
            #msg.attach(file_stream.name, file_stream.read(), file_stream.content_type)
            msg.send(fail_silently=True)
            # form.save()
            instance.save()
            return redirect('/Project_Management/approvallist/')
    file_url = product.attachment.url
    return render(request,'Projectmanagement/approvalpage.html',{'form':form, 'file_url':file_url})


# #----FUNCTIONS RELEATED TO PROJECTTEAM-----------#


def addteam(request): #function For adding new projectteam

    form=ProjectTeamform()
    if request.method =='POST':
        form=ProjectTeamform(request.POST,request.FILES)

        if form.is_valid():

            instance=form.save(commit=True)
            assign = instance.assign_to.email
            

            assgin = instance.assign_to.first_name
            m="Dear"""+assgin +",\n\n"
            Pro= instance.project.project_title
            p={Pro}
            subject = "Project Assigned || "+Pro
            # body = {
            
			# 'Project Name': request.POST.get('project_title')
			
			# }
            # content = ("%s: %s" % (key, value) for (key, value) in body.items())
            msg=" project is assigned please executive on PM tracker and initiate the project."
            
            message = m+ "\n" +"\n" .join(p)+msg
            from_email = settings.EMAIL_HOST_USER
            to_list = ['Jegan.rajendran@cloudstrats.com',assign]
            msg = EmailMultiAlternatives(subject, message, from_email, to_list)
            # msg.attach_alternative(html_content, "text/html")
            #file_stream = form.cleaned_data['attachment']
            #print(f"\n Inmemory Object : {file_stream} \n")
            #msg.attach(file_stream.name, file_stream.read(), file_stream.content_type)
            msg.send(fail_silently=True)
            # form.save()
            instance.save()
            return redirect('/mainpage/')

        

    return render(request,'Projectmanagement/createteam.html',{'form':form})

def teamlist(request): #function for seeing all projectteam
    data=ProjectTeam.objects.all()
    
    return render(request,'Projectmanagement/teamlist.html',{'data':data}) 

# def updateteam(request,id): #function for updating team details
#     product=ProjectTeam.objects.get(id=id)
#     form=ProjectTeamform(instance=product)
#     if request.method == 'POST':
#         form=ProjectTeamform(request.POST,request.FILES,instance=product)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('/teamlist/')
#     return render(request, '',{'form':form})

# def deleteteam(request,id): #function for deleteing team details
#     product=Project.objects.get(id=id)
#     product.delete()
#     return redirect('/teamlist').

# #----FUNCTIONS RELEATED TO TASKCREATION-----------#


def addtask(request): #function For adding new projectteam
    current_user = request.user
    ffname = current_user.first_name
    intaial_data ={
        
        'creater': ffname
    }
    
    form=Taskform(initial=intaial_data)
    if request.method =='POST':
        form=Taskform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/Project_Management/tasklist/')

    return render(request,'Projectmanagement/taskceation.html',{'form':form})


def tasklist(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Task.objects.filter(creater__icontains=q)
        
    else:
        data = Task.objects.all()
  
    return render(request, 'Projectmanagement/tasklist.html',{'data': data})


def get_assigned_to(request):
    id = request.GET.get('vertical')
    data = Project.objects.filter(vertical__id = id)
    print(f"\n {data} \n")
    return render(request, "Projectmanagement/assigned_to.html",{'data':data})

# def teammembers(request): #function For adding new teammembers
#     # m1 =  None
#     # m2 =  None
#     # m3 =  None
#     # m4 =  None
#     form=Teammemberform()
#     if request.method =='POST':
#         members = request.POST.getlist('m1')#[sdasd@gdg.com]
#         form=Teammemberform(request.POST)

#         if form.is_valid():
#             # form.save(commit=True)
#             # if instance.m1:
#             #     m1 =  instance.m1.email
#             # if instance.m2:
#             #     m2 = instance.m2.email              
#             # if instance.m3:            
#             #     m3 = instance.m3.email            
#             # if instance.m4:
#             #     m4 = instance.m4.email  
#             assgin = 'Teams'
#             m="Dear"""+assgin +",\n\n"
#             Pro= request.POST.get('project_title')
#             p={Pro}
#             subject = "Project Assigned || "+Pro
#             # body = {
            
# 			# 'Project Name': request.POST.get('project_title')
			
# 			# }
#             # content = ("%s: %s" % (key, value) for (key, value) in body.items())
#             msg=" project is assigned."
            
#             message = m+ "\n" +"\n" .join(p)+msg
#             from_email = settings.EMAIL_HOST_USER
#             try:
#                 to_list = ['Jegan.rajendran@cloudstrats.com',]+members
#                 msg = EmailMultiAlternatives(subject, message, from_email, to_list)
#                 msg.send(fail_silently=True)
#             except:
#                 pass
            
#             # msg.attach_alternative(html_content, "text/html")
#             #file_stream = form.cleaned_data['attachment']
#             #print(f"\n Inmemory Object : {file_stream} \n")
#             #msg.attach(file_stream.name, file_stream.read(), file_stream.content_type)
            
#             form.save(commit=True)
#             # instance.save()
#             return redirect('/mainpage/')
        
#     return render(request,'Projectmanagement/teammembers.html',{'form':form})


def teammembers(request): #function For adding new teammembers
    m1 =  None
    m2 =  None
    m3 =  None
    m4 =  None
    form=Teammemberform()
    if request.method =='POST':
        form=Teammemberform(request.POST)

        if form.is_valid():

            instance=form.save(commit=True)
            if instance.m1:
                m1 =  instance.m1.email
            if instance.m2:
                m2 = instance.m2.email              
            if instance.m3:            
                m3 = instance.m3.email            
            if instance.m4:
                m4 = instance.m4.email  
            assgin = 'Teams'
            m="Dear"""+assgin +",\n\n"
            Pro= instance.project.project_title
            p={Pro}
            subject = "Project Assigned || "+Pro
            # body = {
            
			# 'Project Name': request.POST.get('project_title')
			
			# }
            # content = ("%s: %s" % (key, value) for (key, value) in body.items())
            msg=" project is assigned."
            
            message = m+ "\n" +"\n" .join(p)+msg
            from_email = settings.EMAIL_HOST_USER
            try:
                to_list = ['Jegan.rajendran@cloudstrats.com',m1,m2,m3,m4]
                msg = EmailMultiAlternatives(subject, message, from_email, to_list)
                msg.send(fail_silently=True)
            except:
                pass
            
            # msg.attach_alternative(html_content, "text/html")
            #file_stream = form.cleaned_data['attachment']
            #print(f"\n Inmemory Object : {file_stream} \n")
            #msg.attach(file_stream.name, file_stream.read(), file_stream.content_type)
            
            # form.save()
            instance.save()
            return redirect('/mainpage/')
        
    return render(request,'Projectmanagement/teammembers.html',{'form':form})

def Reviewfun(request):
    if request.method == "POST":
        name = request.POST.get("name")
        comments = request.POST.get("comments")
        rating = request.POST.get("rating")
        review=Review(name=name,comments=comments,rating=rating)
        review.save()
        messages.success(request, "Thank you for your valuable feedback in next version we will try to implement")
        return redirect('Reviewfun')
    return render(request,'Projectmanagement/review.html')

def Reviewdetail(request):
    detail=Review.objects.all()
    return render(request,'Projectmanagement/reviewdetail.html',{'detail':detail})




