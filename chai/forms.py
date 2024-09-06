from django import forms 
from . import models 
from .models import ChaiVarity

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','slug']



class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(),
                                         label= "Select chai variety")