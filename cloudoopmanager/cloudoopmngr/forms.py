from django import forms
from cloudoopmngr.models import DataNode, Host, HD

class NewDataNodeForm(forms.ModelForm):
 
   class Meta:
      model = DataNode


class CreateDataNodeForm(forms.Form):
    dnhostname = forms.CharField(label='Datanode Hostname', max_length=60)
    
class CreatePullDataNodesForm(forms.Form):
        hostname_pattern = forms.CharField(label='Datanode Hostname Pattern', max_length=60)
        domain = forms.CharField(label='Datanodes domain', max_length=60)
        num_dns = forms.IntegerField(label='Num DataNodes (min value 3)', min_value=3)
