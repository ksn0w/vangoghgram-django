from django.conf.urls import url, include

urlpatterns = [
    url('^user/', include('modules.User.urls'))
]