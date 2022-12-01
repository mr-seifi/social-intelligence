from django.db.models.signals import pre_save
from django.dispatch import receiver
from .prometheus_models import token_social
from .models import Token


@receiver(pre_save, sender=Token)
def send_metrics(sender, instance, update_fields, *args, **kwargs):
    d = update_fields['social_volumes'] - instance.social_volumes
    token_social.inc(d)
    print(f'{d} sent!')
