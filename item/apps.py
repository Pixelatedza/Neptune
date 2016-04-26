import os, sys, time

from django.conf import settings

from item.models import ItemType, Item, Property, ItemProperty, ItemPropertyValue

class handle_items(object):

    def create_item_type(self, name, description):
        obj = ItemType(name=name, description=description)
        obj.save()

    def create_item(self, name, itemType):
        obj = Item(name=name, itemType=itemType)
        obj.save()

    def create_property(self, name, label, type):
        obj = Property(name=name, label=label, type=type)
        obj.save()

    def create_item_prop_relation(self, itemID, propertyID):
        obj = ItemProperty(itemID=itemID, propertyID=propertyID)
        obj.save()

    def create_item_prop_value(self, itemID, propertyID, value):
        obj = ItemPropertyValue(itemID=itemID, propertyID=propertyID, value=value)
        obj.save()

    def __init__ (self):
        pass