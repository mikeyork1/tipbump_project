from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Site(models.Model):
    company_name = models.CharField(max_length=200,blank=False,null=False)
    report_creation_day = models.CharField(max_length=50,blank=True,null=True)
    report_creation_time = models.DateTimeField()
    notification_emails = models.CharField(max_length=1000,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f"/site/{self.id}"

    def get_edit_url(self):
        return f"/site/{self.id}/edit"

class Store(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    store_name = models.CharField(max_length=200,blank=False,null=False)
    store_id = models.CharField(max_length=50,blank=False,null=False)
    report_creation_day = models.CharField(max_length=50,blank=True,null=True)
    report_creation_time = models.DateTimeField()
    report_emails = models.CharField(max_length=1000,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return f"/store/{self.slug}"

    def get_edit_url(self):
        return f"/store/{self.slug}/edit"

    def get_delete_url(self):
        return f"/store/{self.slug}/delete"
