from django.core.management.base import BaseCommand
from prometheus_client import start_http_server
from time import sleep


class Command(BaseCommand):
    help = 'This command starts prometheus server on 8000 port'

    def handle(self, *args, **options):
        start_http_server(8000)
        while True:
            sleep(100)
