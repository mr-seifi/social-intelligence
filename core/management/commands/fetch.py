import re

from django.conf import settings
from django.core.management.base import BaseCommand
from core.services import LunarCrushService, InfluxDBService
from influxdb_client.rest import ApiException

class Command(BaseCommand):
    help = 'This command fetch social data from feed service and send it to the monitoring server'

    def add_arguments(self, parser):
        parser.add_argument('proxy', type=int, help='Wanna use proxy?')

    def handle(self, *args, **options):
        proxy = bool(options['proxy'])
        symbols = settings.LUNARCRUSH_ASSET_SYMBOLS
        lunar_service = LunarCrushService(True if proxy else False)
        inf_service = InfluxDBService()

        for sym in symbols:  # TODO: Move this logic to the class
            df = lunar_service.fetch_data(asset_symbol=sym, interval='1w')
            try:
                inf_service.write(record=df, measurement_name=sym)
                continue

            except ApiException as ae:
                field, measurement, type_1, type_2 = re.findall(r'input\sfield\s\\?\"(.+?)\\?\"\son\smeasurement\s\\?'
                                                                r'\"(.+?)\\?\"\sis\stype\s(.+),\salready\sexists\sas'
                                                                r'\stype\s(.+)\sdropped', str(ae))[0]
                if type_2 == 'integer':
                    type_2 = 'int'

                df = df.astype({field: type_2})
            inf_service.write(record=df, measurement_name=sym)

        self.stdout.write("All data is successfully fetched!", ending='')
