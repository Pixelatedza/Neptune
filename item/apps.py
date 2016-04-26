import os, sys, time

from django.conf import settings

from item.models import ItemType, Item, Attribute, ItemAttribute, ItemAttributeValue

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
    def create_attribute(self, label, type):
        obj = Attribute(label=label, type=type)
        obj.save()
        return obj

    @classmethod
    def create_item_attr_relation(self, itemType, attr):
        obj = ItemAttribute(itemType=itemType, attribute=attr)
        obj.save()

    @classmethod
    def create_item_attr_value(self, item, attr, value):
        obj = ItemAttributeValue(item=item, attribute=attr, value=value)
        obj.save()

    @classmethod
    def get_props_for_itemType(self, itemType):

        objs = ItemAttribute.objects.all().filter(itemType=itemType)

        attributes = {}

        for obj in objs:
            attr = Attribute.objects.get(id=obj.attribute)
            attributes[attr.label] = attr.id

        return attributes

    @classmethod
    def get_item_values(self, itemID):
        values = {}
        objs = ItemAttributeValue.objects.all().filter(itemID=itemID)

        for obj in objs:
            valueLabel = Attribute.object.get(obj.propertyID).label
            value = obj.value

            values[valueLabel] = value

    @classmethod
    def create_type_with_attrs(self, input):

        itemType = input['item_type']

        newItemType = self.create_itemType(itemType, itemType)

        for attr in input['attributes']:
            newAttr = self.create_attribute(attr['label'], attr['_type'])
            self.create_item_attr_relation(newItemType, newAttr)

        return True

    def __init__ (self):
        pass