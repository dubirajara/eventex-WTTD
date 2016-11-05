from django.conf.urls import include, url
from django.contrib import admin

from eventex.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'^palestras/$', views.talk_list, name='talk_list'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', views.speaker_detail, name='speaker_detail'),
    url(r'^admin/', admin.site.urls),
]
