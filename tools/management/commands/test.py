from django.core.management.base import BaseCommand
import os, sys, time

from django.conf import settings

class Command(BaseCommand):
    help = """Add testinf data and test stuff."""

    def process(self, path):

        pass
