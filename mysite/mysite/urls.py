from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('charts.urls')),
    url(r'^charts/', include('charts.urls')),
]
