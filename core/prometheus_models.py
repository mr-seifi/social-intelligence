from prometheus_client.metrics import Gauge

token_social = Gauge(
    "django_model_token_social_volumes",
    "Number of social volumes by token.",
    ["token_name"],
)
