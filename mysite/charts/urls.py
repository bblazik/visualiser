from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.monthlyReport, name='charts'),
    url(r'^monthlyRecord$', views.monthlyReport, name='monthlyRecc'),
    url(r'^yearlyRecord$', views.yearlyReport, name='yearlyRecord'),
    url(r'^data$', views.visualiseData, name='data')
    
]