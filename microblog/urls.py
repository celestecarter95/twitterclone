from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MainView.as_view(), name="main"),
	url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
	url(r'^myfeed/$', login_required(views.MyFeedView.as_view()), name="myfeed"),
	#url(r'^user/(?P<pk>\d+)/follow/$', login_required(views.FollowForm.as_view()), name="follow"),
]
