import re
import pandas as pd
from django.conf import settings
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException


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
        try:
            self.write_client.write(bucket=self._bucket,
                                    record=record,
                                    data_frame_measurement_name=measurement_name)
        except ApiException as ae:
            field, measurement, type_1, type_2 = re.findall(r'input\sfield\s\\?\"(.+?)\\?\"\son\smeasurement\s\\?'
                                                            r'\"(.+?)\\?\"\sis\stype\s(.+),\salready\sexists\sas'
                                                            r'\stype\s(.+)\sdropped', str(ae))[0]
            if type_2 == 'integer':
                type_2 = 'int'

            record = record.astype({field: type_2})
            self.write(record, measurement_name)
