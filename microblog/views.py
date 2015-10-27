from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy, reverse

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

class FollowFormView(SingleObjectMixin, View):
	model = Profile

	def post(self, request, *args, **kwargs):
		#self tells me who we want to follow and request tell me who the login user is
		my_profile = request.user.profile_set.all()[0]
		my_profile.following.all(self.get_object())
		my_profile.save()
		return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.get_object().pk, )))
		# return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object.pk()))

class FollowSuccessView(SingleObjectMixin, TemplateView):
	template_name = 'microblog/follow_success.html'
	model = Profile

class CreatePostView(CreateView):
	model = Post
	fields = ['body']

	def get_success_url(self):
		#return HttpResponseRedirect(reverse('microblog:profiledetail', args=(self.request.user.id)))
		return reverse_lazy('microblog:myfeed')

	def form_valid(self, form):
		profile = self.request.user.profile_set.all()[0]
		post = form.save(commit=False)
		post.profile = profile
		post.save()
		return super(CreatePostView, self).form_valid(form)

class UpdatePostView(UpdateView):
	model = Post
	fields = ['body']
	success_url =  reverse_lazy('microblog:myfeed')

class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('microblog:deletesuccess')

