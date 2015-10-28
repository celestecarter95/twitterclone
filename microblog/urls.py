from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', views.MainView.as_view(), name="main"),
	url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
	url(r'^myfeed/$', login_required(views.MyFeedView.as_view()), name="myfeed"),
	url(r'^addpost/$', login_required(views.CreatePostView.as_view()), name="addpost"),
	url(r'^updatepost/(?P<pk>\d+)/$', login_required(views.UpdatePostView.as_view()), name="updatepost"),
	url(r'^deletepost/(?P<pk>\d+)/$', login_required(views.DeletePostView.as_view()), name="deletepost"),
	url(r'^deletepost/success/$', login_required(TemplateView.as_view(template_name='microblog/success.html')), name="deletesuccess"),
	url(r'^profile/(?P<pk>\d+)/follow/$', login_required(views.FollowFormView.as_view()), name="follow"),
    url(r'^profile/(?P<pk>\d+)/follow/success/$', login_required(views.FollowSuccessView.as_view()), name="followsuccess"),
	url(r'^profile/create/$', views.CreateProfileView.as_view(), name="createprofile"),
	url(r'^profile/(?P<pk>\d+)/update/$', views.UpdateProfileView.as_view(), name="updateprofile"),
]
