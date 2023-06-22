from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.sites.models import Site


class TempAcc(models.Model):

    class Meta:
        verbose_name = 'Временная ссылка'
        verbose_name_plural = 'Временные ссылки'

    clean_url = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        current_site = Site.objects.get_current()
        clean_url = get_random_string(length=20)
        unique_url = 'http://' + current_site.domain + '/tempacc/' + clean_url
        self.url = unique_url
        self.clean_url = clean_url
        super(TempAcc, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.clean_url)
