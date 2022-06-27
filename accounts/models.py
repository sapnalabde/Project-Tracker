from django.db import models
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
#from payment.models import PaymentPlan
#from mailprocess.models import Country
#from product.models import Product
#from mailprocess.models import BusinessType
from django.utils import timezone
from .choice import *
#from crmplus.models import Lead, Deals, Contacts, Company, Task

class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vertical(ModelBase):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

USER_ROLE = ((1, "Admin"), (2, "Manager"), (3, "Executive"), (4, "User"),(5,"CsOwner"),(6,"Demo"))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
    parentuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="parentuser")
    mobile = models.BigIntegerField()
    #company = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    #country_detail = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    #business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    #website = models.CharField(_('domain name'), null=True, blank=True, max_length=100)
    userstatus = models.IntegerField(choices=STATUS_CHOICE, default=1)
    #total_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    #remaining_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    #used_amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    #skypeid = models.CharField(max_length=100, null=True, blank=True)
    #key = models.CharField(max_length=30, null=True, blank=True)
    #is_api_enabled = models.BooleanField(default=False)
    #myplan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE, null=True, blank=True, related_name='myplan')
    #salescrm_no_of_users = models.IntegerField(null=True, blank=True, default=1)
    #salescrm_valid_date = models.DateTimeField(null=True, blank=True)
    userrole = models.IntegerField(choices=USER_ROLE, default=4)
    department = models.ForeignKey(Vertical, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

    # def remaining_days(self):
    #     if self.myplan.id == 1:
    #         return 365
        # else:
        #     if self.salescrm_valid_date:
        #         noofdays = self.salescrm_valid_date - timezone.now()
        #         if noofdays.days == 0:
        #             return 1
        #         elif noofdays.days < 0:
        #             return 0
        #         else:
        #             return noofdays.days + 1
        #     return 0


    # def remaining_records(self):
    #     total_records = self.myplan.email_count
    #     if self.user.userdetail.parentuser is None:
    #         parentuser = self.user

    #     else:
    #         parentuser = self.user.userdetail.parentuser

    #     subuser = UserProfile.objects.filter(parentuser=parentuser, user__is_active=True)
    #     subuser = [userprofile.user for userprofile in subuser]
    #     subuser.append(parentuser)
    #     leadcount = Lead.objects.filter(user__in=subuser, active=True).count()
    #     contactcount = Contacts.objects.filter(user__in=subuser, active=True).count()
    #     companycount = Company.objects.filter(user__in=subuser, active=True).count()
    #     dealcount = Deals.objects.filter(user__in=subuser, active=True).count()
    #     taskcount = Task.objects.filter(user__in=subuser, active=True).count()
    #     total_uses_count = contactcount + companycount + dealcount + dealcount + taskcount + leadcount
    #     if total_uses_count:
    #         return total_records - total_uses_count
    #     return total_records


    def subusers(self):
        parentuser = None
        if self.parentuser is None:
            parentuser = self.user
        else:
            parentuser = self.parentuser
        if parentuser:
            sub_user = self.objects.filter(parentuser=parentuser)
            return sub_user
        return []

    def is_admin(self):
        if self.userrole == 1:
            return 1
        else:
            return 0




# class CRMPlusCount(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usercount")
#     lead_count = models.IntegerField(default=0)
#     contact_count = models.IntegerField(default=0)
#     deal_count = models.IntegerField(default=0)
#     task_count = models.IntegerField(default=0)
#     companies_count = models.IntegerField(default=0)
#     added_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
