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

token_unique_url_shares = Gauge(
    "token_unique_url_shares",
    "Number of unique url shares of token.",
    ["token_name"]
)

token_reddit_posts = Gauge(
    "token_reddit_posts",
    "Number of reddit posts.",
    ["token_name"]
)

token_reddit_posts_score = Gauge(
    "token_reddit_posts_score",
    "Reddit posts score.",
    ["token_name"]
)

token_reddit_comments = Gauge(
    "token_reddit_comments",
    "Number of reddit comments.",
    ["token_name"]
)

token_reddit_comments_score = Gauge(
    "token_reddit_comments_score",
    "Reddit comments score.",
    ["token_name"]
)

token_tweets = Gauge(
    "token_tweets",
    "Number of tweets.",
    ["token_name"]
)

token_tweet_spam = Gauge(
    "token_tweet_spam",
    "Number of spam tweets.",
    ["token_name"]
)

token_tweet_followers = Gauge(
    "token_tweet_followers",
    "Number of tweet followers.",
    ["token_name"]
)

token_tweet_quotes = Gauge(
    "token_tweet_quotes",
    "Number of tweet quotes.",
    ["token_name"]
)

token_tweet_retweets = Gauge(
    "token_tweet_retweets",
    "Number of retweets.",
    ["token_name"]
)

token_tweet_replies = Gauge(
    "token_tweet_replies",
    "Number of tweet replies.",
    ["token_name"]
)

token_tweet_favorites = Gauge(
    "token_tweet_favorites",
    "Number of tweet favorites.",
    ["token_name"]
)

token_tweet_sentiment1 = Gauge(
    "token_tweet_sentiment1",
    "Tweet sentiment.",
    ["token_name"]
)

token_tweet_sentiment2 = Gauge(
    "token_tweet_sentiment2",
    "Tweet sentiment.",
    ["token_name"]
)

token_tweet_sentiment3 = Gauge(
    "token_tweet_sentiment3",
    "Tweet sentiment.",
    ["token_name"]
)

token_tweet_sentiment4 = Gauge(
    "token_tweet_sentiment4",
    "Tweet sentiment.",
    ["token_name"]
)

token_tweet_sentiment5 = Gauge(
    "token_tweet_sentiment5",
    "Tweet sentiment.",
    ["token_name"]
)

token_tweet_sentiment_impact1 = Gauge(
    "token_tweet_sentiment_impact1",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_tweet_sentiment_impact2 = Gauge(
    "token_tweet_sentiment_impact2",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_tweet_sentiment_impact3 = Gauge(
    "token_tweet_sentiment_impact3",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_tweet_sentiment_impact4 = Gauge(
    "token_tweet_sentiment_impact4",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_tweet_sentiment_impact5 = Gauge(
    "token_tweet_sentiment_impact5",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_tweet_sentiment_impact6 = Gauge(
    "token_tweet_sentiment_impact6",
    "Tweet sentiment impact.",
    ["token_name"]
)

token_social_score = Gauge(
    "token_social_score",
    "Social score of token.",
    ["token_name"],
)

token_average_sentiment = Gauge(
    "token_average_sentiment",
    "Average sentiment of token.",
    ["token_name"],
)

token_sentiment_absolute = Gauge(
    "token_sentiment_absolute",
    "Absolute sentiment of token.",
    ["token_name"],
)

token_sentiment_relative = Gauge(
    "token_sentiment_relative",
    "Relative sentiment of token.",
    ["token_name"],
)

token_search_average = Gauge(
    "token_search_average",
    "Search sentiment of token.",
    ["token_name"],
)

token_news = Gauge(
    "token_news",
    "Number of token news.",
    ["token_name"],
)

token_social_impact_score = Gauge(
    "token_social_impact_score",
    "Social impact score of token.",
    ["token_name"],
)

token_correlation_rank = Gauge(
    "token_correlation_rank",
    "Token correlation rank.",
    ["token_name"],
)


token_galaxy_score = Gauge(
    "token_galaxy_score",
    "Token galaxy score.",
    ["token_name"],
)

token_volatility = Gauge(
    "token_volatility",
    "Token volatility.",
    ["token_name"],
)

token_alt_rank = Gauge(
    "token_alt_rank",
    "Alt rank of token.",
    ["token_name"],
)

token_alt_rank_30d = Gauge(
    "token_alt_rank_30d",
    "30d Alt rank of token.",
    ["token_name"],
)

token_market_cap_rank = Gauge(
    "token_market_cap_rank",
    "Token market cap rank.",
    ["token_name"],
)

token_percent_change_24h_rank = Gauge(
    "token_percent_change_24h_rank",
    "Token percentage change in 24h rank.",
    ["token_name"],
)

token_volume_24h_rank = Gauge(
    "token_volume_24h_rank",
    "Token volume change in 24h rank.",
    ["token_name"],
)

token_social_volume_24h_rank = Gauge(
    "token_social_volume_24h_rank",
    "Token social volume in 24h rank.",
    ["token_name"],
)

token_social_score_24h_rank = Gauge(
    "token_social_score_24h_rank",
    "Token social score in 24h rank.",
    ["token_name"],
)

token_medium = Gauge(
    "token_medium",
    "Token medium.",
    ["token_name"],
)

token_youtube = Gauge(
    "token_youtube",
    "Token youtube.",
    ["token_name"],
)

token_social_contributors = Gauge(
    "token_social_contributors",
    "Token social contributors.",
    ["token_name"],
)

token_influential_content = Gauge(
    "token_influential_content",
    "Token influential content.",
    ["token_name"],
)

token_influential_content_score = Gauge(
    "token_influential_content_score",
    "Token influential content score.",
    ["token_name"],
)

token_social_volume = Gauge(
    "token_social_volume",
    "Token social volume.",
    ["token_name"],
)

token_social_volume_global = Gauge(
    "token_social_volume_global",
    "Token social volume global.",
    ["token_name"],
)

token_social_dominance = Gauge(
    "token_social_dominance",
    "Token social dominance.",
    ["token_name"],
)

token_market_cap_global = Gauge(
    "token_market_cap_global",
    "Token market cap global.",
    ["token_name"],
)

token_market_dominance = Gauge(
    "token_market_dominance",
    "Token market dominance.",
    ["token_name"],
)
