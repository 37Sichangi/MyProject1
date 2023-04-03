from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Customer, Region, land

# Create your views here.
# def myview(request):
# 	return render(request, "index.html")
class Home(CreateView):
    # form_class=CustomerForm
    model=Customer
    template_name="customer.html"
    fields="__all__"
    
class Customer(ListView):
    model=Customer
    template_name='cust.html'

class Region(CreateView):
    model=Region
    template_name="reg.html"
    fields="__all__"

class Land(CreateView):
    model=land
    template_name="lan.html"
    fields="__all__"

    

    	