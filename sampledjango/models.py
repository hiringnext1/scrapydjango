from django.template.defaultfilters import slugify
from djongo import models
from tinymce.models import HTMLField
# Create your models here.


class IndeedJobsManager(models.Manager):

    def get_queryset_ahm(self):
        return super().get_queryset().filter(city__icontains='Ahmedabad')

    def get_queryset_vadodara(self):
        return super().get_queryset().filter(city__icontains='Vadodara')

    def get_queryset_surat(self):
        return super().get_queryset().filter(city__icontains='Surat')

    def get_queryset_rajkot(self):
        return super().get_queryset().filter(city__icontains='Rajkot')

    def get_queryset_bharuch(self):
        return super().get_queryset().filter(city__icontains='Bharuch')

    def get_queryset_ankleshwar(self):
        return super().get_queryset().filter(city__icontains='Ankleshwar')

    def get_queryset_vapi(self):
        return super().get_queryset().filter(city__icontains='Vapi')

    def get_queryset_gandhinagar(self):
        return super().get_queryset().filter(city__icontains='Gandhinagar')


class IndeedJobs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    # experience = models.CharField(max_length=100, null=True, blank=True)
    job_description = HTMLField(null=True, blank=True)
    date_posted = models.CharField(max_length=200, null=True, blank=True)
    job_url = models.URLField(max_length=1000, unique=True, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, auto_created=True, auto_now_add=True)

    objects = models.Manager()
    job_objects = IndeedJobsManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while IndeedJobs.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.slug, )])
