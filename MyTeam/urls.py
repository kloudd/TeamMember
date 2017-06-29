from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teamMember/$', views.TeamMemberList.as_view()),
    url(r'^teamMember/(?P<pk>[0-9]+)/$', views.TeamMemberDetail.as_view()),

    

    
]
