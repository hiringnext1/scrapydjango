from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import JobFilter
from dal import autocomplete


from .models import IndeedJobs


# Create your views here.

class HomeListView(FilterView):
    model = IndeedJobs
    template_name = 'new_theme/index.html'
    filterset_class = JobFilter
    context_object_name = 'indeed'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'by_location': IndeedJobs.objects.filter(city__icontains=IndeedJobs.city),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),

        }
        )
        return context


class IndexView(ListView):
    model = IndeedJobs
    template_name = 'sampledjango/indeedjobs_list.html'
    context_object_name = 'indeedjobs'
    paginate_by = 20
    queryset = IndeedJobs.objects.all()
    ordering = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
        }
        )
        return context


class IndexDetailView(DetailView):
    model = IndeedJobs
    template_name = 'sampledjango/indeedjobs_detail.html'


class TestListView(FilterView):
    model = IndeedJobs
    template_name = 'test_page.html'
    filterset_class = JobFilter
    context_object_name = 'indeed_test'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TestListView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'by_location': IndeedJobs.objects.filter(city__icontains=IndeedJobs.city),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),
        }
        )
        return context

