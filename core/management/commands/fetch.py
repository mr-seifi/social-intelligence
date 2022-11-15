import re

from django.conf import settings
from django.core.management.base import BaseCommand
from core.services import LunarCrushService, InfluxDBService


class Command(BaseCommand):
    help = 'This command fetch social data from feed service and send it to the monitoring server'

    def add_arguments(self, parser):
        parser.add_argument('proxy', type=int, help='Wanna use proxy?')

    def handle(self, *args, **options):
        proxy = bool(options['proxy'])
        symbols = settings.LUNARCRUSH_ASSET_SYMBOLS
        lunar_service = LunarCrushService(True if proxy else False)
        inf_service = InfluxDBService()

        for sym in symbols:
            df = lunar_service.fetch_data(asset_symbol=sym, interval='1w')
            inf_service.write(record=df, measurement_name=sym)

        self.stdout.write(f"All data is successfully fetched! {inf_service}", ending='')
