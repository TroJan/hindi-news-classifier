from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

    url(r'', include('newsclassifier.preprocess.urls',
                      namespace='preprocess')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),

]
