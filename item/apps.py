import os, sys, time

from django.conf import settings

from item.models import ItemType, Item, Property, ItemProperty, ItemPropertyValue

class HandleItems(object):

    @classmethod
    def create_itemType(self, name, description):
        obj = ItemType(name=name, description=description)
        obj.save()
        return obj

    @classmethod
    def create_item(self, name, itemType):
        obj = Item(name=name, itemType=itemType)
        obj.save()

    @classmethod
    def create_property(self, label, type):
        obj = Property(label=label, type=type)
        obj.save()
        return obj

    @classmethod
    def create_item_prop_relation(self, itemTypeID, propertyID):
        obj = ItemProperty(itemTypeID=itemTypeID, propertyID=propertyID)
        obj.save()

    @classmethod
    def create_item_prop_value(self, itemID, propertyID, value):
        obj = ItemPropertyValue(itemID=itemID, propertyID=propertyID, value=value)
        obj.save()

    @classmethod
    def get_props_for_itemType(self, itemTypeID):

        objs = ItemProperty.objects.all().filter(itemTypeID=itemTypeID)

        properties = {}

        for obj in objs:
            prop = Property.objects.get(id=obj.propertyID)
            properties[prop.label] = prop.id

        return properties

    @classmethod
    def get_item_values(self, itemID):
        values = {}
        objs = ItemPropertyValue.objects.all().filter(itemID=itemID)

        for obj in objs:
            valueLabel = Property.object.get(obj.propertyID).label
            value = obj.value

            values[valueLabel] = value

    @classmethod
    def create_type_with_props(self, input):

        itemType = input['item_type']

        newItemType = self.create_itemType(itemType, itemType)

        for prop in input['properties']:
            newProp = self.create_property(prop['label'], prop['_type'])
            self.create_item_prop_relation(newItemType, newProp)

        return True

    def __init__ (self):
        pass