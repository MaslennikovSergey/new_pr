from django.urls import path, register_converter, re_path
from service.views import index, page, about, file_show, json_show 
from service import converts

#register_converter(converts.CheckParam, "dif_type")

urlpatterns = [
    
    path('service', index, name = 'service'),
    path('', index, name = 'service'),
    #path('service/<int:page_num>', page),
    #path('service/<str:page_num>', page),
    #path('service/<dif_type:page_num>', page),
    re_path(r'^service/(?P<page_num>[0-9]{3})/$',page),
    path('about/<int:id>', about, name = 'about'),
    path('file', file_show, name = 'file_show'),
    path('json', json_show, name = 'json_show'),
]