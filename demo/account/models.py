from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True, default="")
    self_introduction = models.TextField(blank=True, default="")


class ResetPasswordToken(models.Model):
    user = models.OneToOneField(User)
    
    # URL generated by sha256, so we need max_length=64
    dynamic_url = models.CharField(max_length=64, unique=True, null=True)
    entry_token = models.CharField(max_length=64, blank=True)
    created_time = models.DateTimeField(auto_now_add=True) 
    updated_time = models.DateTimeField(auto_now=True)
    expire_time = models.DateTimeField()


@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        ResetPasswordToken.objects.create(user=instance, expire_time=timezone.localtime(timezone.now()))
