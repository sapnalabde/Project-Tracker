from ast import Return
import json
#import binascii
import os
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import UserProfile
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import *
from .choice import *
#from mailprocess.decorators import login_required_ajax
#from mailprocess.models import Country, BusinessType
from .models import *
#from crmplus.utils import *
#from settings.settupsave import *
#import logging
#logger = logging.getLogger(__name__)

def site_user_registration(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        mobile = request.POST.get('mobile')
        #country = request.POST.get('country')
        #skypeid = request.POST.get('skypeid')
        vertical = request.POST.get('vertical')
        email = email.lower()
        cus = User.objects.filter(Q(email=email) | Q(username=username))
        if cus:
            return HttpResponse(json.dumps(2), content_type="application/json")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            # user.is_staff=True
            user.is_active = True
            user.save()
            profileinfo = UserProfile(user=user, mobile=mobile, userstatus=1,
                                    vertical=int(vertical))
            profileinfo.save()

            # save_widget(user)
            # funnel_save(user)
            # pipeline_save(user)
            # service_pipeline_save(user)

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return HttpResponse(json.dumps(1), content_type="application/json")
    else:
        template_name = 'accounts/signup.html'
        return render(request, template_name,
                      { 'vertical': Vertical.objects.all()})


def login_site(request):
    if request.method == "POST":
        cus = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = User.objects.get(username=username)
        except:
            try:
                cus = User.objects.get(email=username)
            except:
                return HttpResponseRedirect("/account/signin/?msg=Username is not correct.Please fill correct one.")
        user = authenticate(username=cus.username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect("/mainpage/")
        else:
            return HttpResponseRedirect("/account/signin/?msg=Password is not correct.Please fill correct one.")
        # if user is not None:
        #         if user.is_active:
        #             login(request, user)
                    
        #             if str(request.user.groups.all()[0]) == 'Admin':
        #                 return redirect('Admin:mainpage')
                        
        #             elif str(request.user.groups.all()[0]) == 'Manager':
        #                 return redirect('Manager:mainpage')

        #             elif str(request.user.groups.all()[0]) == 'Executive':
        #                 return redirect('Executive:mainpage')

        #             elif str(request.user.groups.all()[0]) == 'user':
        #                 return redirect('user:mainpage')
                        
        #             else:
        #                 return redirect('mainpage')
    else:
        template_name = 'account/signin.html'
        return render(request, template_name, {})


def changepassword(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps(3), content_type="application/json")
    password = request.POST.get('new_password')
    try:
        user = request.user
        user.set_password(password)
        user.save()
    except:
        return HttpResponse(json.dumps(2), content_type="application/json")

    return HttpResponse(json.dumps(1), content_type="application/json")


def forgotpassword(request):
    template_name = 'accounts/forgotpassword.html'
    msg = None
    if request.method == "POST":
        sourcemail = request.POST.get('email')
        username = request.POST.get('username')
        asd = str(sourcemail)
        try:
            obj = User.objects.get(email=asd, username=username)
            # password=obj.userdetail.mobile
            # password= ''.join(random.choice(string.ascii_letters) for x in range(6))
            # obj.set_password(password)
            # obj.save()
            # templatename="mail/forgot-mailer.html"
            # c={'user':obj,}
            # message = loader.render_to_string(templatename, c)
            # send_mail('Instructions for changing your MailCleaners Password',message,'"MailCleaners Account" <admin@mailcleaners.org>',[sourcemail],fail_silently=False,html_message=message)
            msg = "Please <a href='/accounts/signin/%s/'>click here</a> for login on your account. After login please visit profile page to change your password for further use." % (
                obj.username)
        except Exception as e:
            return render(request, template_name,
                          {'msg': "We have not any user associated with that username and email id."})
        return render(request, template_name, {'msg': msg})
    return render(request, template_name, {})


# @login_required_ajax
# def accounts(request):
#     template_name = 'myadmin/profile.html'
#     if request.method == "POST":
#         try:
#             name = request.POST.get('first_name')
#             mobile = request.POST.get('mobile')
#             #county_id = request.POST.get('country_detail')
#             vertical_id = request.POST.get('vertical')
#             request.user.first_name = name
#             request.user.save()
#             request.user.userdetail.mobile = mobile
#             #request.user.userdetail.country_detail_id = county_id
#             request.user.userdetail.vertical_id = vertical_id
#             request.user.userdetail.save()
#             return HttpResponse(json.dumps(1), content_type="application/json")
#         except:
#             return HttpResponse(json.dumps(2), content_type="application/json")
#     return render(request, template_name,
#                   {'vertical': Vertical.objects.all()})


def auth_logout(request):
    logout(request)
    return redirect("/")


# def companydetails(request):
#     if not request.user.is_authenticated:
#         return HttpResponse(json.dumps(3), content_type="application/json")
#     if request.method == "POST":
#         try:
#             company = request.POST.get('company')
#             website = request.POST.get('website')
#             address = request.POST.get('address')
#             request.user.userdetail.company = company
#             request.user.userdetail.website = website
#             request.user.userdetail.address = address
#             request.user.userdetail.save()
#             return HttpResponse(json.dumps(1), content_type="application/json")
#         except:
#             return HttpResponse(json.dumps(2), content_type="application/json")

#     return HttpResponse(json.dumps(2), content_type="application/json")


def admin_login(request, username):
    user = User.objects.get(username=username)
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return HttpResponseRedirect("/mysite/")


@login_required(login_url='/')
def accounts_usage(request):
    fromdate = request.GET.get('fromdate', None)
    todate = request.GET.get('todate', None)
    template_name = "accounts/usage.html"
    #usage = UserUsage.objects.filter(active=True, userusage__user=request.user).order_by("-date")
    if fromdate and todate:
        fromdate = fromdate + " 00:00"
        todate = todate + " 23:59"
        usage = usage.filter(date__range=[fromdate, todate])
    total = usage.aggregate(Sum('price'))
    paginator = Paginator(usage, 1000)
    page = request.GET.get('page')
    try:
        usage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        usage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        usage = paginator.page(paginator.num_pages)

    return render(request, template_name, {'usage': usage, 'total': total.get("price__sum")})


# @login_required(login_url='/')
# def api_access(request, status):
#     userdetail = request.user.userdetail
#     if status == "enable":
#         key = binascii.hexlify(os.urandom(11)).decode()
#         userdetail.key = key
#         userdetail.is_api_enabled = True
#         userdetail.save()
#     else:
#         userdetail.key = ""
#         userdetail.is_api_enabled = False
#         userdetail.save()
#     return HttpResponseRedirect("/mysite/api/")


def subuser_details(request, slug):
    subuser = User.objects.get(username=slug)
    template_name = 'myadmin/crmplus/subuser_details.html'
    return render(request, template_name, {'subuser': subuser})


def subuser(request):
    user = request.user
    msg = None
    if len(get_user_list(user)) >= user.userdetail.salescrm_no_of_users:
        msg = "#Please upgrade your plan to create Subusers"
    parentuser = get_parentuser(user)
    subuser = UserProfile.objects.filter(parentuser=parentuser, user__is_active=True)
    #subuser = column_ordering(request, subuser)
    role = request.user.userdetail.userrole
    subuser = get_permission_based_subuser(subuser,role,user)
    template_name = 'myadmin/crmplus/subuser.html'
    return render(request, template_name, {'subuser': subuser, 'role':role, 'msg':msg})


def change_subuser(request, slug=None):
    user = request.user
    subuser = None
    if slug:
        subuser = User.objects.get(username=slug)
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("parentuser")
        password = request.POST.get("password")
        mobile = request.POST.get('mobile')
        # country = request.POST.get('country')
        # skypeid = request.POST.get('skypeid')
        userrole = request.POST.get('userrole')
        vertical = request.POST.get('vertical')
        email = email.lower()

        cus = User.objects.filter(Q(email=email) | Q(username=username))
        if cus:
            return HttpResponse(json.dumps(2), content_type="application/json")
        parentuser = get_parentuser(user)
        # business_type = parentuser.userdetail.business_type
        myplan = parentuser.userdetail.myplan
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = True
        user.save()
        profileinfo = UserProfile(user=user, mobile=mobile,
                                  userrole=userrole,
                                  parentuser=parentuser, myplan=myplan, vertical=int(vertical), salescrm_no_of_users = parentuser.userdetail.salescrm_no_of_users)
        profileinfo.userstatus = 1
        profileinfo.save()
        # crmcount = CRMPlusCount(user=user)
        # crmcount.save()
        return HttpResponse(json.dumps(1), content_type="application/json")
    else:
        template_name = 'myadmin/crmplus/change_subuser.html'
        role = get_role(user)
        return render(request, template_name, { 'status_choice': STATUS_CHOICE, 'role':role, 'subuser':subuser}, )


def edit_subuser(request,slug=None):
    subuser = None
    if slug:
        subuser = User.objects.get(username=slug)
    if request.method == "POST":
        password = request.POST.get("password")
        mobile = request.POST.get('mobile')
        #country = request.POST.get('country')
        vertical = request.POST.get('vertical')
        #skypeid = request.POST.get('skypeid')
        userrole = request.POST.get('userrole')
        subuser.save()
        subuser.userdetail.mobile = mobile
        subuser.userdetail.password = password
        #subuser.userdetail.country_detail_id = int(country)
        subuser.userdetail.vertical = int(vertical)
        subuser.userdetail.userrole = userrole
        #subuser.userdetail.skypeid = skypeid
        subuser.userdetail.save()
        return HttpResponse(json.dumps(1), content_type="application/json")
    else:
        template_name = 'myadmin/crmplus/edit_subuser.html'
        role = get_role(request.user)
        return render(request, template_name, { 'status_choice': STATUS_CHOICE, 'role':role, 'subuser':subuser,'vertical': vertical.objects.all()}, )

def delete_subuser(request, slug):
    subuser = User.objects.get(username=slug)
    subuser.is_active = False
    subuser.save()
    return HttpResponseRedirect("/accounts/subuser/")

def detail(request):
    current_user = request.user
    ffname = current_user.first_name
    
    prof=User.objects.get(first_name = ffname)
    return render(request, 'account/profile.html',{'prof':prof})
 
