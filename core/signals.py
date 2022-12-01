from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .prometheus_models import token_social
from .models import Token


@receiver(pre_save, sender=Token)
def send_metrics_pre(sender, instance, *args, **kwargs):
    token_social.dec(instance.social_volumes)


@receiver(post_save, sender=Token)
def send_metrics_post(sender, instance, *args, **kwargs):
    token_social.inc(instance.social_volumes)
