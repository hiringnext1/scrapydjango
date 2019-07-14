from .models import IndeedJobs
import django_filters


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Job Title')

    city = django_filters.CharFilter(lookup_expr='icontains', label='Location')

    class Meta:
        model = IndeedJobs
        fields = ['title', 'city']
