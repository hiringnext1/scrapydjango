from django.contrib import admin
from .models import IndeedJobs
# Register your models here.


class IndeedJobsAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'city', 'salary', 'date_posted']


admin.site.register(IndeedJobs, IndeedJobsAdmin)