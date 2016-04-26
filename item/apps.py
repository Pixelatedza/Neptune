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
        return obj

    @classmethod
    def create_attribute(self, label, dataType):
        obj = Attribute(label=label, dataType=dataType)
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
    def create_item_with_attr(self, input):
    #create item and populate its properties values.
        itemT = ItemType.objects.get(id=input['itemTypeID'])
        item = self.create_item(input['itemName'], itemT)

        attributes = input['attributes']

        for attr in attributes:
            attribute = Attribute.objects.get(attribute['id'])
            self.create_item_attr_value(item, attribute, attribute['value'])

    @classmethod
    def get_item_values(self, item):
    #returns a dict of attribute values for a item. {attribute label: value}
        values = {}
        objs = ItemAttributeValue.objects.all().filter(item=item)

        for obj in objs:
            valueLabel = Attribute.object.get(obj.attribute).label
            value = obj.value

            values[valueLabel] = value

    @classmethod
    def get_item_type_attrs(self, itemType):
    #returns a dict with attribute types: {attribute label: attribute type)
        attributes = ItemAttribute.objects.all().filter(itemType=itemType).attribute
        result = {}

        for attr in attributes:
            result[attr.label] = attr.dataType

    @classmethod
    def create_type_with_attrs(self, input):
    #creates a new item type and its attributes and links them.
        itemType = input['item_type']

        newItemType = self.create_itemType(itemType, itemType)

        for attr in input['attributes']:
            newAttr = self.create_attribute(attr['label'], attr['_type'])
            self.create_item_attr_relation(newItemType, newAttr)

        return True