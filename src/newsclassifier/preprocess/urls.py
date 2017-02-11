from django.conf.urls import include, url

from .views import *

urlpatterns = [

    url(r'', (TokenizeView.as_view()), name='tokenize_view'),

]
