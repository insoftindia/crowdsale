from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^crowdfunding/$', views.crowdfunding, name='crowdfunding'),
    url(r'^crowdfunding/latest/proposals/$', views.latest_crowdfunding_proposals, name='crowdfunding_latest_proposals'),
    url(r'^crowdfunding/closed/proposals/$', views.closed_crowdfunding_proposals, name='crowdfunding_closed_proposals'),
    # url(r'^crowdfunding/votedbyme/proposals/$', views.voted_crowdfunding_proposals, name='crowdfunding_voted_proposals'),
    url(r'^crowdfunding/close_proposal/$', views.close_proposal, name='crowdfunding_close_proposal'),
    url(r'^crowdfunding/new/$', views.create_crowdfunding, name='create_crowdfunding'),
    url(r'^crowdfunding/user_creation/$',views.user_creation,name='user_creation'),
    url(r'^crowdfunding/(?P<pk>\d+)/$', views.crowdfunding_detail, name='crowdfunding_detail'),
    # url(r'^crowdfunding/vote/$', views.crowdfunding_vote, name='crowdfunding_vote'),
    url(r'^crowdfunding/get_group_total_amount/$', views.get_group_total_amount, name='get_group_total_amount'),
    url(r'^crowdfunding/get_user_private_key/$', views.get_user_private_key, name='get_user_private_key'),
    # url(r'^crowdfunding/downvote/$', views.crowdfunding_downvote, name='crowdfunding_downvote'),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
