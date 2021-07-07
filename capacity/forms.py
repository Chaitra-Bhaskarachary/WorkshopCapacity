from django import forms
from .models import WorkshopCapacity
  
  
# creating a form
class WorkshopCapacityForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = WorkshopCapacity
  
        # specify fields to be used
        fields = "__all__"
      