from django.shortcuts import render
from .models import ChaiVarity, Store
from django.shortcuts import get_object_or_404
from . import forms
from .forms import ChaiVarityForm


# Create your views here.
def all_chai(request):
    # now let show the value in the database on the frontend of the website
    # we have orm to link the db so we do not have to write the sql ourself
    chais = ChaiVarity.objects.all()
    return render(request, "chai/all_chai.html", {"chais": chais})


# now if we see the renderr code we might be thinling
# where to render the code because to render we need
# urls file but in the new application we do not have the
# urls files so we copy the content of the urls.py file and
# create a new urls.py file in app folder.


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, "chai/chai_detail.html", {"chai": chai})


def chai_store_view(request):
    stores= None
    if request.method == "POST":
      form = ChaiVarityForm(request.POST)
      if form.is_valid():
       chai_variety = form.cleaned_data['chai_varity']
       Store.objects.filter(chai_varieties= chai_variety)
    else:
       form = ChaiVarityForm()
    return render(request, "chai/chai_stores.html", 
                  {'stores':stores, 'form':form }) 


def chai_forms_view(request):
    form = forms.CreatePost()
    return render(request, "chai/chai_form.html", {"form": form})

