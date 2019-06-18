from djongo import models
from tinymce.models import HTMLField
# Create your models here.


class IndeedJobs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    # experience = models.CharField(max_length=100, null=True, blank=True)
    job_description = HTMLField(null=True, blank=True)
    date_posted = models.CharField(max_length=200, null=True, blank=True)
    job_url = models.URLField(max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id, )])




