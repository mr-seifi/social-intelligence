import re
import pandas as pd
from django.conf import settings
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException
from collections import defaultdict
from core import prometheus_models
from prometheus_client import start_http_server


class InfluxDBService:

    def __init__(self):
        self._url = f'http://{settings.INFLUX_SERVER_HOST}:{settings.INFLUX_SERVER_PORT}'
        self._token = settings.INFLUX_TOKEN
        self._org = settings.INFLUX_ORG
        self._bucket = settings.INFLUX_BUCKET_NAME
        self._tries = 3
        self._tries_per_name = defaultdict(lambda: 0)
        self._successfully_sent = set()

    @property
    def client(self):
        return InfluxDBClient(url=self._url, token=self._token, org=self._org, debug=settings.DEBUG)

    @property
    def write_client(self) -> InfluxDBClient.write_api:
        return self.client.write_api(write_options=SYNCHRONOUS)

    def report(self, measurement):
        self._successfully_sent.add(measurement)

    def write(self, record: pd.DataFrame, measurement_name):
        try:
            self.write_client.write(bucket=self._bucket,
                                    record=record,
                                    data_frame_measurement_name=measurement_name)
            self.report(measurement_name)

        except ApiException as ae:
            field, measurement, type_1, type_2 = re.findall(r'input\sfield\s\\?\"(.+?)\\?\"\son\smeasurement\s\\?'
                                                            r'\"(.+?)\\?\"\sis\stype\s(.+),\salready\sexists\sas'
                                                            r'\stype\s(.+)\sdropped', str(ae))[0]
            if type_2 == 'integer':
                type_2 = 'int'

            record = record.astype({field: type_2})
            self._tries_per_name[measurement_name] += 1
            if self._tries_per_name[measurement_name] > self._tries:
                return
            self.write(record, measurement_name)
        except Exception as ex:
            print('exception occurred', ex)

    def __repr__(self):
        return f'{len(remained := set(settings.LUNARCRUSH_ASSET_SYMBOLS) - self._successfully_sent)} coins did not ' \
               f'send! {remained}'


class PrometheusService:

    def __init__(self, token_name: str):
        self._token_name = token_name

    def send(self, df: pd.DataFrame):
        [getattr(prometheus_models, f'token_{col}').labels(self._token_name).set(df[col][-1] or 0)
         for col in df.columns
         if getattr(prometheus_models, f'token_{col}', None)]

    @staticmethod
    def runserver():
        start_http_server(8000)
