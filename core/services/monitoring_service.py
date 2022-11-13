import pandas as pd
from django.conf import settings
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDBService:

    def __init__(self):
        self._url = f'http://{settings.INFLUX_SERVER_HOST}:{settings.INFLUX_SERVER_PORT}'
        self._token = settings.INFLUX_TOKEN
        self._org = settings.INFLUX_ORG
        self._bucket = settings.INFLUX_BUCKET_NAME

    @property
    def client(self):
        return InfluxDBClient(url=self._url, token=self._token, org=self._org, debug=settings.DEBUG)

    @property
    def write_client(self) -> InfluxDBClient.write_api:
        return self.client.write_api(write_options=SYNCHRONOUS)

    def write(self, record: pd.DataFrame, measurement_name):
        self.write_client.write(bucket=self._bucket,
                                record=record,
                                data_frame_measurement_name=measurement_name)
