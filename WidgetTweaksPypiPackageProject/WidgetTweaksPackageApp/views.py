from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def index_view(request):
    form=ContactForm()
    return render(request,"WidgetTweaksPackageApp/form.html" ,{"form":form})
