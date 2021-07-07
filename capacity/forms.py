from django import forms
from .models import WorkshopCapacity
  
  
# creating a form
class WorkshopCapacityForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = WorkshopCapacity
  
        # specify fields to be used
        fields = [
            "admin_id",
            "admin_name",
            "calender_week",
            "entry_check",
            "exit_check",
            "retail_ready"
        ]