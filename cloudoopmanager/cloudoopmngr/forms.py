from django import forms
from cloudoopmngr.models import DataNode

class NewDataNodeForm(forms.ModelForm):
 
   class Meta:
      model = DataNode

class DataNodeForm(forms.ModelForm):
    campus = forms.ModelChoiceField(queryset=models.Campus.objects.all())
    school = forms.ModelChoiceField(queryset=models.School.objects.none()) # Need to populate this using jquery
    centre = forms.ModelChoiceField(queryset=models.Centre.objects.none()) # Need to populate this using jquery

    class Meta:
        model = models.Center

        fields = ('campus', 'school', 'centre')