from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .prometheus_models import token_social
from .models import Token


@receiver(post_save, sender=Token)
def send_metrics_post(sender, instance, *args, **kwargs):
    token_social.labels(instance.name).set(instance.social_volumes)
