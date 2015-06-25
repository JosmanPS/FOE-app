from django.conf.urls import *
from views import *

urlpatterns = patterns(
    '',

    # main site
    url(r'^$', index, name='index'),
)
