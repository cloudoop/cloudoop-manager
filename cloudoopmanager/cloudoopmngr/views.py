from django.shortcuts import render, get_object_or_404
from cloudoopmngr.models import DataNode, Host, HD
from forms import NewDataNodeForm, CreateDataNodeForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db.models import Min, Count

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

def view_datanodes(request):
    datanodes = DataNode.objects.all()
    return render(request, 'alldatanodes.html', {'datanodes':datanodes})

def view_hosts(request):
    hosts = Host.objects.all()
    return render(request, 'allhosts.html', {'hosts':hosts})

def infrastructure_overview(request):
    hosts = Host.objects.all()
    datanodes = DataNode.objects.all()
    return render(request, 'infroverview.html', {'datanodes':datanodes,'hosts':hosts})

def delete_datanode(request, datanode_id):
    datanode = get_object_or_404(DataNode, pk=datanode_id)
    hds = datanode.hds.all()
    for hd in hds:
        hd.status = HD.AVAILABLE
        hd.save()
    datanode.delete()
    return HttpResponseRedirect('/view-datanodes/')

def delete_host(request, host_id):
    host = get_object_or_404(Host, pk=host_id)
    host.delete()
    return HttpResponseRedirect('/view-hosts/')

def _find_host_available():
    ref_hds = -1
    hosts_available = Host.objects.filter(hd__status=HD.AVAILABLE).distinct()
    for host in hosts_available:
        av_hds = HD.objects.filter(status=HD.AVAILABLE,host=host.pk).count()
        if av_hds > ref_hds:
            ref_hds = av_hds
            selected_host = host
    return selected_host

def _get_first_hd_in_host(host):
    hd = HD.objects.filter(host=host.pk,status=HD.AVAILABLE).first()
    return hd

def add_datanode(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateDataNodeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            host = _find_host_available()
            hd = _get_first_hd_in_host(host)
            dn = DataNode(hostname=form.cleaned_data['dnhostname'],host=host)
            dn.save()
            dn.hds.add(hd)
            hd.status=HD.OCCUPIED
            hd.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/view-datanodes/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateDataNodeForm()

    args = {}
    args.update(csrf(request))
    
    args['form'] = form
 
    return render(request, 'adddatanode.html', args)
