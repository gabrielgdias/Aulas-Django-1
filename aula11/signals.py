from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from slugify import slugify

from .models import Automovel, UserProfile


@receiver(pre_save, sender=Automovel)
def slugify_automovel(sender, instance, **kwargs):
    automovel = instance
    marca = automovel.marca
    modelo = automovel.modelo
    slug = f"{marca} {modelo}"
    automovel.slug = slugify(slug)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        UserProfile.objects.create(user=user)


@receiver(post_delete, sender=User)
def send_email(sender, instance, **kwargs):
    user = instance
    print(f"Muito {user.username} obrigado por ter participado da plataforma!\n")
