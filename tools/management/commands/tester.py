from django.core.management.base import BaseCommand
import os, sys, time

from django.conf import settings

from item.models import ItemType, Item, Property, ItemProperty, ItemPropertyValue

class Command(BaseCommand):
    help = """Add testing data and test stuff."""

    def create_item_prop_relation(self, itemID, PropertyID):
        ItemProperty.objects.create()

    def handle(self, *args, **options):

        print 'hello'
