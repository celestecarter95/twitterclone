from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy

from .models import Profile, Post
# Create your views here.

class MainView(ListView):
	model = Post 
	paginate_by = 10
	queryset = Post.objects.all().order_by('-pub_date')

	#def get_queryset(self):
	#	return Profile.objects.order_by('-pub_date')[:10]

class ProfileDetailView(DetailView):
	model = Profile

class MyFeedView(ListView):
	model = Post
	paginate_by = 10
	template_name = "microblog/myfeed.html"

	def get_queryset(self):
		my_profile = self.request.user.profile_set.all()[0]
		profile_list = list(my_profile.following.all())
		profile_list.append(my_profile)
		return Post.objects.filter(profile__in = profile_list)

#class FollowFormView(SingleObjectMixin, View):
#	model = Profile
#
#	def post(self, request, *args, **kwargs):
#		#self tells me who we want to follow and request tell me who the logined in user is
#		my_profile = request.user.profile_set.all()[0]
#		my_profile.following.all(self.get_object())
#		my_profile.save()
#		# don't want redirect to followsuccss want to redirect to profiledetail with args
#		# return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.get_object().pk, ))) OR
#		return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object.pk()))

#class FollowFormView(FormView):
#	success_url = reverse_lazy('microblog:profiledetail', args=(something with pk))
#
#	class FollowUserForm(forms.Form):
#		follow_user_id = forms.IntegerField(widget=forms.HiddenInput)
#
#	form_class = FollowUserForm
#
#	def form_valid(self, form):
