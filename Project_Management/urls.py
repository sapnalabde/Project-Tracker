from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('mainpage/', views.mainpage),
    path('Project_Management/projectreg/',views.addproject),#url For adding new project
    #path('search/', views.searchoption),#url for search option
    path('Project_Management/list/<id>/',views.attach),# url for pdf attachment
    path('Project_Management/projectdetail/<id>/',views.projectdetail),# url for details
    path('Project_Management/projectlist/',views.projectlist),#url For seeing projectlist
    path('Project_Management/pendingprojectlist/',views.pendingprojectlist),#url For seeing pendingprojectlist
    path('Project_Management/updateproject/<id>/',views.updateproject),#url For updating  project
    path('Project_Management/deleteproject/<id>/',views.deleteproject), #url For delete the project
    path('Project_Management/approvallist/',views.approvallist), #url For delete the project.
    path('Project_Management/approvalpage/<id>/',views.approvalpage), #url For delete the project


    
    path('Project_Management/teamreg/',views.addteam),#url For adding new projectteam
    # path('Project_Management/teamlist/',views.teamlist),#url For adding new projectteamlist
    # path('Project_Management/updateteam/<id>/',views.updateteam),#url For updating  team
    # path('Project_Management/deleteteam/<id>/',views.deleteteam), #url For delete the team

    path('Project_Management/taskreg/',views.addtask),#url For adding new addtask
    path('Project_Management/teamlist/',views.teamlist),#url For adding new projectteamlist
    path("get-assigned-to/", views.get_assigned_to, name="get_assigned_to"),
    path('Project_Management/tasklist/',views.tasklist),#url For seeing projectlist
    # path('Project_Management/updateteam/<id>/',views.updateteam),#url For updating  team
    # path('Project_Management/deleteteam/<id>/',views.deleteteam), #url For delete the team
    path('Project_Management/teammembers/',views.teammembers),
    

    path('Project_Management/Reviewfun/',views.Reviewfun, name= "Reviewfun"),#url for review funciton
    path('Project_Management/Reviewdetail/',views.Reviewdetail),#url for review detail list
    path('',views.home),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)