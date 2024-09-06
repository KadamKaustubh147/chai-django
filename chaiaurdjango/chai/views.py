from django.shortcuts import render

# Create your views here.

def all_chai(request):
    return render(request, "chai/all_chai.html") # template folder ke aandar all_chai.html naam ka file hai.
