from prometheus_client.metrics import Gauge

token_open = Gauge(
    "token_open",
    "Open price of token.",
    ["token_name"]
)

token_close = Gauge(
    "token_close",
    "Close price of token.",
    ["token_name"]
)

token_high = Gauge(
    "token_high",
    "High price of token.",
    ["token_name"]
)

token_low = Gauge(
    "token_low",
    "Low price of token.",
    ["token_name"]
)

token_volume = Gauge(
    "token_volume",
    "Volume of token.",
    ["token_name"]
)

token_market_cap = Gauge(
    "token_market_cap",
    "Market Cap of token.",
    ["token_name"]
)

token_url_shares = Gauge(
    "token_url_shares",
    "Number of url shares of token.",
    ["token_name"]
)

token_social = Gauge(
    "token_social",
    "Number of social volumes by token.",
    ["token_name"],
)
