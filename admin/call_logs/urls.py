from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('missed_calls/', views.missed_calls, name='missed_calls'),
    path('call_logs/ajax/ajax_incoming', views.ajax_incoming, name='ajax_incoming'),
    path('call_logs/ajax/ajax_logs', views.ajax_logs, name='ajax_logs'),
    path('call_logs/ajax/ajax_missed', views.ajax_missed, name='ajax_missed')
]
