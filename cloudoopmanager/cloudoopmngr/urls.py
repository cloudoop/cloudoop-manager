from django.conf.urls import patterns, url
from cloudoopmngr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tables/$', views.tables, name="tables"),
    url(r'^blank/$', views.blank, name="blank"),
    url(r'^forms/$', views.forms, name="forms"),
    url(r'^flot/$', views.flot, name="flot"),
    url(r'^morris/$', views.morris, name="morris"),
    url(r'^login/$', views.login, name="login"),
    url(r'^buttons/$', views.buttons, name="buttons"),
    url(r'^panels/$', views.panels, name="panels"),
    url(r'^typography/$', views.typography, name="typography"),
    url(r'^notifications/$', views.notifications, name="notifications"),
    url(r'^grid/$', views.grid, name="grid"),
    
)