from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home_page(request):
    # return HttpResponse("<h1>Hello bitches!</h1>")
    page_title = "Welcome to TipBump"
    # my_list =
    context = {"title": page_title}
    return render(request, "home.html", context)

def about_page(request):
    page_title = "About Us"
    return render(request, "about.html", {"title": page_title})

def contact_page(request):
    page_title = "Contact Us"
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render(request, "form.html", context)

def scorecard_view(request):
    template_name = 'scorecard.html'
    return render(request,template_name)
