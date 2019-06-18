from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import IndeedJobs


# Create your views here.

class HomeListView(ListView):
    model = IndeedJobs
    template_name = 'index.html'
    context_object_name = 'indeed'
    paginate_by = 20
    queryset = IndeedJobs.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
        }
        )
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__contains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class IndexView(ListView):
    model = IndeedJobs
    template_name = 'jobs-list-layout-2.html'
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
