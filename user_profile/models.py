from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import URLValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    f_name = models.CharField(max_length=30,db_index=True,blank=True, default='')
    l_name = models.CharField(max_length=30, db_index=True, blank=True, default='')
    email = models.EmailField(max_length=254, db_index=True, blank=True, default='')
    # image = models.ImageField(upload_to='profilepics', blank=True)
    # created_at = models.DateTimeField(auto_now_add = True)
    github_profile = models.TextField(db_index=True, blank=True, default='',validators=[URLValidator()])
    reddit_profile = models.TextField( db_index=True, blank=True, default='',validators=[URLValidator()])
    facebook_profile = models.TextField( db_index=True, blank=True, default='',validators=[URLValidator()])
    linkedin_profile = models.TextField(db_index=True, blank=True, default='',validators=[URLValidator()])
    def get_full_name(self):
        return self.f_name + ' '+ self.l_name
    def __str__(self):
        return self.f_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# class Profile(models.Model):
#     name = models.CharField(max_length = 100, db_index = True)
#     slug = models.SlugField(max_length = 120, unique = True, db_index = True)
#     # created_at = models.DateTimeField(auto_now_add = True)
#     # updated_at = models.DateTimeField(auto_now = True)
#     # description = models.TextField(blank = True)
#     # image = models.ImageField(upload_to='profilepics', blank=True)
#     github_profile = models.CharField(max_length = 60, db_index=True, blank=True, default='')
#     reddit_profile = models.CharField(max_length = 60, db_index=True, blank=True, default='')
#     facebook_profile = models.CharField(max_length = 60, db_index=True, blank=True, default='')
#     linkedin_profile = models.CharField(max_length = 60, db_index=True, blank=True, default='')


    # def __str__(self):
    #     return self.name
    # def get_absolute_url(self):
    #     return reverse('user_profile:my_profile', args=[self.slug])
    # class Meta:
    #     ordering = ('name', )
    #     index_together = (('slug'),)
