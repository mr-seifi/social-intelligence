from django.conf import settings
from django.core.management.base import BaseCommand
from core.services import LunarCrushService, InfluxDBService, PrometheusService
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')


class Command(BaseCommand):
    help = 'This command fetch social data from feed service and send it to the monitoring server'

    def add_arguments(self, parser):
        parser.add_argument('proxy', type=int, help='Wanna use proxy?')
        parser.add_argument('monitoring', type=str, help='What is your monitoring system?')

    def handle(self, *args, **options):
        proxy = bool(options['proxy'])
        monitoring = options['monitoring']
        symbols = settings.LUNARCRUSH_ASSET_SYMBOLS
        lunar_service = LunarCrushService(True if proxy else False)
        inf_service = InfluxDBService()

        if monitoring == 'prometheus':
            PrometheusService.runserver()

        for sym in symbols:
            df = lunar_service.fetch_data(asset_symbol=sym, interval='1w')
            try:
                if monitoring == 'prometheus':  # TODO: State pattern
                    service = PrometheusService(sym)
                    service.send(df)
                else:
                    inf_service.write(record=df, measurement_name=sym)
            except Exception as e:
                continue

        logging.info(f'{inf_service}')
        self.stdout.write(f"All data is successfully fetched! {inf_service}", ending='')
