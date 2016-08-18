""" Created by Jieyi on 8/18/16. """
from django.conf.urls import url, include

from api import views
from api.views import Login

urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    url(r'^login/', include([
        url(r'^index/$', Login.as_view(), name='login'),
        url(r'^test/$', views.test, name='test'),
    ]
    )),
]
