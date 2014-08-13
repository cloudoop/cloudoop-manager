from django import forms
from cloudoopmngr.models import DataNode, Host, HD

class NewDataNodeForm(forms.ModelForm):
 
   class Meta:
      model = DataNode
            
class NewHostForm(forms.ModelForm):
    
    class Meta:
        model = Host
        labels = {
            'hostname': 'Hostname (FQDN)',
            'mem': 'Memory (GB)',
            'os': 'OS',
            'ip': 'IP Address',
        }

class CreateDataNodeForm(forms.Form):
    dnhostname = forms.CharField(label='Datanode Hostname', max_length=60)
    
class CreatePullDataNodesForm(forms.Form):
    hostname_pattern = forms.CharField(label='Datanode Hostname Pattern', max_length=60)
    domain = forms.CharField(label='Datanodes domain', max_length=60)
    num_dns = forms.IntegerField(label='Num DataNodes (min value 3)', min_value=3)
    
    def __init__(self, *args, **kwargs):
        super(CreatePullDataNodesForm, self).__init__(*args, **kwargs)
        num_hosts_available = Host.objects.filter(hd__status=HD.AVAILABLE).distinct().count()
        if (num_hosts_available >= 3):
            self.fields['num_dns'] = forms.IntegerField(label='Num DataNodes (min value 3)',max_value=num_hosts_available, min_value=3)

            
            
            
            