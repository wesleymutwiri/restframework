from django.conf.urls import url,include
from .views import CreateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^bucketlist/$', CreateView.as_view(), name= 'create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)