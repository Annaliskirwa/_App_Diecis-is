from django.conf.urls import path
from tutorialsnow import views 
 
urlpatterns = [ 
    path('api/tutorials$', views.tutorial_list),
    path('api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    path('api/tutorials/published$', views.tutorial_list_published)
]