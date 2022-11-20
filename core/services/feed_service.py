from django.conf import settings
import json
import pandas as pd
import requests


class LunarCrushService:

    def __init__(self, proxy=False):
        self._url = 'https://lunarcrush.com/api3/coins/{asset_symbol}/time-series'
        self._token = settings.LUNARCRUSH_TOKEN
        self._headers = {
            'authority': 'lunarcrush.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
                      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': self._token,
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        self._proxies = {
            'http': 'socks5://127.0.0.1:10808',
            'https': 'socks5://127.0.0.1:10808'
        }
        self._is_proxy = proxy

    @staticmethod
    def _get_params(interval='1w'):
        return {
            'interval': interval
        }

    def _request(self, asset_symbol, interval='1w'):
        kwargs = {
            'url': self._url.format(asset_symbol=asset_symbol),
            'params': self._get_params(interval),
            'headers': self._headers,
        }
        if self._is_proxy:
            kwargs['proxies'] = self._proxies

        return requests.get(**kwargs)

    @staticmethod
    def _json_load(response):
        return json.loads(response.text)

    @staticmethod
    def _get_asset_name(data) -> str:
        return data.get('data').get('name')

    @staticmethod
    def _get_asset_symbol(data) -> str:
        return data.get('data').get('symbol')

    @staticmethod
    def _get_timeframe(data) -> str:
        return data.get('config').get('interval')

    @staticmethod
    def _get_timeseries(data) -> dict:
        return data.get('timeSeries')

    @staticmethod
    def _to_dataframe(data: dict) -> pd.DataFrame:
        return pd.DataFrame(data)

    @staticmethod
    def _clean_dataframe(df: pd.DataFrame):
        df.time = pd.to_datetime(df.time, unit='s')
        df.index = df.time
        df.drop(['asset_id', 'time', 'price_score'], axis=1, inplace=True)
        df = df.astype('float64')

    def fetch_data(self, asset_symbol, interval='1w') -> pd.DataFrame:
        data = self._json_load(
            self._request(asset_symbol, interval)
        )

        time_series = self._get_timeseries(data)
        print(self._get_asset_name(data), self._get_asset_symbol(data), self._get_timeframe(data))
        df = self._to_dataframe(time_series)
        self._clean_dataframe(df)

        return df
