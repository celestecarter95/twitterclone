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
		#my_profile = self.request.user.profile_set.all()[0]
		my_profile, created = Profile.objects.get_or_create(user = self.request.user)
		profile_list = list(my_profile.following.all())
		profile_list.append(my_profile)
		return Post.objects.filter(profile__in = profile_list).order_by('-pub_date')

class FollowFormView(SingleObjectMixin, View):
	model = Profile

	def post(self, request, *args, **kwargs):
		#self tells me who we want to follow and request tell me who the login user is
		#my_profile, created = Profile.objects.get_or_create(user = self.request.user)
		try:
			my_profile = request.user.profile_set.all()[0]
		except Profile.DoesNotExist:
			my_profile = Profile(bio = '', user = request.user)
		my_profile.following.add(self.get_object())
		my_profile.save()
		#return HttpResponseRedirect(reverse_lazy('microblog:profiledetail', args = (self.get_object().pk, )))
		return HttpResponseRedirect(reverse_lazy('microblog:followsuccess', args = (self.get_object().pk, )))
		#return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object.pk()))

class FollowSuccessView(DetailView):
	template_name = 'microblog/follow_success.html'
	model = Profile

class CreatePostView(CreateView):
	model = Post
	fields = ['body']
	success_url = reverse_lazy('microblog:myfeed')

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

class CreateProfileView(CreateView):
	model = Profile
	fields = ['bio', 'picture', 'following']

	def get_success_url(self):
		return reverse('microblog:main')

	def form_valid(self, form):
		profile = form.save(commit=False)
		if 'picture' in self.request.FILES:
			profile.picture = self.get_form_kwargs().get('files')['picture']
		profile.user = self.request.user
		profile.save()

		return super(CreateProfileView, self).form_valid(form)

class UpdateProfileView(UpdateView):
	model = Profile
	fields = ['bio', 'picture', 'following']

	def get_success_url(self):
		return reverse('microblog:profiledetail', args = (self.get_object().pk,))

	def form_valid(self, form):
		profile = form.save(commit=False)
		if 'picture' in self.request.FILES:
			profile.picture = self.get_form_kwargs().get('files')['picture']
		profile.save()

		return super(UpdateProfileView, self).form_valid(form)

