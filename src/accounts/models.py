from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(_("Birth Date"), blank=True, null=True)
    phone_number = models.CharField(
        _("Phone Number"), max_length=50, null=True, blank=True
    )
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
