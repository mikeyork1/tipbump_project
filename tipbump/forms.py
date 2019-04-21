from django import forms

from .models import Store

class StoreForm(forms.Form):
    store_name = forms.CharField()
    slug = forms.SlugField()
    store_id = forms.CharField()
    report_creation_day = forms.CharField()
    report_creation_time = forms.DateTimeField()
    report_emails = forms.CharField(widget=forms.Textarea)

class StoreModelForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_name','store_id','slug','report_creation_day','report_creation_time','report_emails']