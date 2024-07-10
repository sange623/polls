from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from . import viewset

router = DefaultRouter()
router.register(r'poll',viewset.PollViewset,basename='PollViewset')
router.register(r'pollhaveoption',viewset.PollHaveOptionViewset,basename='PollHaveOptionsViewset')
router.register(r'polltable',viewset.PollTableViewset,basename='PollTableViewset')
router.register(r'vote',viewset.VoteViewset,basename='VoteViewset')

app_name = 'polls'
urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('api/',include(router.urls)),
]
