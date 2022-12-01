from prometheus_client.metrics import Counter, Gauge

from django_prometheus.conf import NAMESPACE

# model_inserts = Counter(
#     "django_model_inserts_total",
#     "Number of insert operations by model.",
#     ["model"],
#     namespace=NAMESPACE,
# )
#
# model_updates = Counter(
#     "django_model_updates_total",
#     "Number of update operations by model.",
#     ["model"],
#     namespace=NAMESPACE,
# )
#
# model_deletes = Counter(
#     "django_model_deletes_total",
#     "Number of delete operations by model.",
#     ["model"],
#     namespace=NAMESPACE,
# )

token_social = Gauge(
    "django_model_token_social_volumes",
    "Number of social volumes by token.",
    ["token_name"],
    namespace=NAMESPACE,
)
