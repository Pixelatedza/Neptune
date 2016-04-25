from django.core.management.base import BaseCommand
import os, sys, time

from django.conf import settings

class Command(BaseCommand):
    help = """Add testing data and test stuff."""

    def handle(self, *args, **options):

        print 'hello'
