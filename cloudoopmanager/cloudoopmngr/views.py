from django.shortcuts import render, get_object_or_404
from cloudoopmngr.models import DataNode, Host, HD
from forms import NewDataNodeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.

def index(request):
    return render(request,'index.html',)

def tables(request):
    return render(request,'tables.html',)

def blank(request):
    return render(request,'blank.html',)

def forms(request):
    return render(request,'forms.html',)

def flot(request):
    return render(request,'flot.html',)

def morris(request):
    return render(request,'morris.html',)

def login(request):
    return render(request,'login.html',)

def buttons(request):
    return render(request,'buttons.html',)

def panels(request):
    return render(request,'panels-wells.html',)

def typography(request):
    return render(request,'typography.html',)

def notifications(request):
    return render(request,'notifications.html',)

def grid(request):
    return render(request,'grid.html',)

def add_datanode(request):
    if request.POST:
        form = NewDataNodeForm(request.POST)
        if form.is_valid():
            form.save()
            for hd in form.cleaned_data['hds']:
                hd.status=HD.OCCUPIED
                hd.save()
            return HttpResponseRedirect('/view-datanodes/')
    else:
        form = NewDataNodeForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render(request, 'adddatanode.html', args)

def view_datanodes(request):
    datanodes = DataNode.objects.all()
    return render(request, 'alldatanodes.html', {'datanodes':datanodes})

def infrastructure_overview(request):
    hosts = Host.objects.all()
    datanodes = DataNode.objects.all()
    hds = HD.objects.all()
    return render(request, 'infroverview.html', {'datanodes':datanodes,'hosts':hosts, 'hds':hds})

def delete_datanode(request, datanode_id):
    datanode = get_object_or_404(DataNode, pk=datanode_id)
    datanode.delete()
    return HttpResponseRedirect('/view-datanodes/') 