from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .filters import JobFilter
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
            'total_companies': IndeedJobs.objects.values('company').distinct().count(),
            'by_location': IndeedJobs.objects.filter(city__icontains=IndeedJobs.city),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),

        }
        )
        return context


class IndexView(FilterView):
    model = IndeedJobs
    template_name = 'sampledjango/indeedjobs_list.html'
    filterset_class = JobFilter
    context_object_name = 'indeed'
    paginate_by = 20
    queryset = IndeedJobs.objects.all()
    ordering = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context.update({
            'total_jobs': IndeedJobs.objects.all(),
            'filter': JobFilter(self.request.GET, queryset=self.get_queryset()),
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


class JobsByCategories(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_categories/jobs-by-categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByCategories, self).get_context_data()
        return context


class JobsByLocation(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByLocation, self).get_context_data()
        context.update({
            'jobs_ahm': IndeedJobs.job_objects.get_queryset_ahm().all(),
            'jobs_vadodara': IndeedJobs.job_objects.get_queryset_vadodara().all(),
            'jobs_bharuch': IndeedJobs.job_objects.get_queryset_bharuch().all(),
            'jobs_surat': IndeedJobs.job_objects.get_queryset_surat().all(),
        })

        return context


class JobsByAhm(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-ahm.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByAhm, self).get_context_data()
        context.update({
            'jobs_ahm': IndeedJobs.job_objects.get_queryset_ahm().all(),
        })

        return context


class JobsByVadodara(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-vadodara.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByVadodara, self).get_context_data()
        context.update({
            'jobs_vadodara': IndeedJobs.job_objects.get_queryset_vadodara().all(),
        })

        return context


class JobsByBharuch(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-bharuch.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsByBharuch, self).get_context_data()
        context.update({
            'jobs_bharuch': IndeedJobs.job_objects.get_queryset_bharuch().all(),
        })

        return context


class JobsBySurat(ListView):
    model = IndeedJobs
    template_name = 'jobs_by_location/jobs-by-location-surat.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(JobsBySurat, self).get_context_data()
        context.update({
            'jobs_surat': IndeedJobs.job_objects.get_queryset_surat().all(),
        })

        return context
