from .models import Project,ProjectTeam,Task
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ('vertical', 'project_type')

class Projectlist(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ('vertical', 'manager','approval_status','project_status')

        
        