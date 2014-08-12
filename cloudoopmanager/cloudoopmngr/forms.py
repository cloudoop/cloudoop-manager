from django import forms
from cloudoopmngr.models import DataNode, Host, HD

class NewDataNodeForm(forms.ModelForm):
 
   class Meta:
      model = DataNode


class CreateDataNodeForm(forms.Form):
    dnhostname = forms.CharField(label='Datanode Hostname', max_length=60)