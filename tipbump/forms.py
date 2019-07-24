from django import forms

from .models import Store, Site

class SiteModelForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['company_name','report_creation_day','report_creation_time','notification_emails']

    # company_name = models.CharField(max_length=200,blank=False,null=False)
    # report_creation_day = models.CharField(max_length=50,blank=True,null=True)
    # report_creation_time = models.DateTimeField()
    # notification_emails = models.CharField(max_length=1000,blank=True,null=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)


# class StoreForm(forms.Form):
#     store_name = forms.CharField()
#     slug = forms.SlugField()
#     store_id = forms.CharField()
#     report_creation_day = forms.CharField()
#     report_creation_time = forms.DateTimeField()
#     report_emails = forms.CharField(widget=forms.Textarea)
#
class StoreModelForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_name','store_id','slug','report_creation_day','report_creation_time','report_emails']