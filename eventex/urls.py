from django.urls import path, include
from django.contrib import admin

from eventex.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    path('palestras/', views.talk_list, name='talk_list'),
    path('palestrantes/<slug:slug>/', views.speaker_detail, name='speaker_detail'),
    path('admin/', admin.site.urls),
]
