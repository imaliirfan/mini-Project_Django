from django.http import HttpResponse
from django.shortcuts import render


# Now we will create the method or functions
def home(request):
    # return HttpResponse("Hello, World. you are at django learning homepage")
    return render(request, "index.html")


def about(request):
    # return HttpResponse("this is about us page")
    return render(request, "aboutus.html")


def contact(reuqest):
    # return HttpResponse("this is contact us page")
    return render(reuqest, "contactus.html")
