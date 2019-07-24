from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import StoreModelForm, SiteModelForm
from .models import Store, Site

#######################################
############ Store views ##############
#######################################

def store_list_view(request):
    qs = Store.objects.all()
    template_name = 'store/list.html'
    context = {'object_list': qs}
    return render(request,template_name,context)

@staff_member_required
def store_create_view(request):
    form = StoreModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = StoreModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)

def store_detail_view(request, slug):
    obj = get_object_or_404(Store, slug=slug)
    template_name = 'store/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def store_update_view(request, slug):
    obj = get_object_or_404(Store, slug=slug)
    form = StoreModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"form": form, 'title': f"{obj.store_name}"}
    return render(request, template_name, context)

@staff_member_required
def store_delete_view(request, slug):
    obj = get_object_or_404(Store, slug=slug)
    template_name = 'store/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/store")
    context = {"object": obj}
    return render(request, template_name, context)

###########################################
############ end Store views ##############
###########################################


######################################
############ Site views ##############
######################################

@staff_member_required
def site_detail_view(request):
    obj = get_object_or_404(Store, id=1)
    template_name = 'store/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def site_update_view(request):
    obj = get_object_or_404(Site, id=1)
    form = SiteModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"form": form, 'title': f"{obj.company_name}"}
    return render(request, template_name, context)

##########################################
############ end Site views ##############
##########################################
