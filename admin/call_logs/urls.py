from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('missed_calls/', views.missed_calls, name='missed_calls'),
    path('today_calls/', views.today_calls, name='today_calls'),
    path('current_calls/', views.current_calls, name='current_calls'),
    path('voicemail_calls/', views.voicemail_calls, name='voicemail_calls'),
    path('outgoing_calls/', views.outgoing_calls, name='outgoing_calls'),
    path('callreports/', views.callreports, name='callreports'),
    path('ajax/ajax_incoming', views.ajax_incoming, name='ajax_incoming'),
    path('ajax/ajax_logs', views.ajax_logs, name='ajax_logs'),
    path('ajax/ajax_missed', views.ajax_missed, name='ajax_missed'),
    path('ajax/ajax_today', views.ajax_today, name='ajax_today'),
    path('ajax/ajax_current', views.ajax_current, name='ajax_current'),
    path('ajax/ajax_voicemail', views.ajax_voicemail, name='ajax_voicemail'),
    path('ajax/ajax_outgoing', views.ajax_outgoing, name='ajax_outgoing')
]
