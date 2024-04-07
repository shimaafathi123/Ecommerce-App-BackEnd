from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField


GENDER_CHOICES = [
    ("female", "Female"),
    ("male", "Male"),
]

def user_directory_path(instance, filename):
    return f'accounts/users/{filename}'

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500)
    otp = models.CharField(max_length=1000, null=True, blank=True)
    reset_token  = models.CharField(max_length=1000, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
  

    def save(self, *args, **kwargs):
        if not self.full_name:
            email_username, _ = self.email.split('@')
            self.full_name = email_username
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='accounts/users/', default='default/default-user.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=500, choices=GENDER_CHOICES, null=True, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
 
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    pid = ShortUUIDField(unique=True, length=10, max_length=20)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
     #profile, created = Profile.objects.get_or_create(user=instance)
     #profile.save()  
    #instance.profile.save()
    user = instance
    profile = instance.profile
    user.full_name = profile.full_name
    user.email = profile.email
    user.phone = profile.phone
    user.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
