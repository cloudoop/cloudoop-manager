from django import forms
from cloudoopmngr.models import DataNode

class NewDataNodeForm(forms.ModelForm):
 
   class Meta:
      model = DataNode