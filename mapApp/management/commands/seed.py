# <yourapp>/management/commands/seed.py
from django.core.management.base import BaseCommand
from driverTracker.tests.factories import DriverFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--drivers',
            default=10,
            type=int,
            help='The number of fake drivers to create.')

    def handle(self, *args, **options):
        for _ in range(options['drivers']):
            DriverFactory.create()