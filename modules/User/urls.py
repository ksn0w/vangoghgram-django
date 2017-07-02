from django.conf.urls import url
from .views import instagram

urlpatterns = [
    url('^instagram/',instagram)
]