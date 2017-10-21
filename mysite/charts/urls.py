from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.monthlyReport, name='charts'),
    url(r'^monthlyRecord$', views.monthlyReport, name='monthlyRecc'),
    url(r'^yearlyRecord$', views.yearlyReport, name='yearlyRecord'),
    url(r'^visualiseDate$', views.visualiseDate, name='visualiseDate'),
    url(r'^date$', views.date, name='date'),
    url(r'^nextMonth$', views.nextMonth, name=''),
    url(r'^previousMonth$', views.previousMonth, name=''),
]