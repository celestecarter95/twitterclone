import hashlib
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User)
	bio  = models.TextField('Short Bio', blank=True, null=True)
	picture = models.ImageField(upload_to="pics/%Y/%m/%d", blank=True, null=True)
	following = models.ManyToManyField('Profile', blank=True, null=True)

	def get_gravatar_img_path(self):
		if self.user.email:
			return "https://www.gravatar.com/avatar/%s" % (hashlib.md5(self.user.email).hexdigest(),)
		return "https://www.gravatar.com/avatar/%s" % (hashlib.md5("no email found").hexdigest(),)

	def __unicode__(self):
		return self.user.get_full_name() or self.user.username

class Post(models.Model):
	profile = models.ForeignKey(Profile)
	body	= models.CharField(max_length=140)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.body

