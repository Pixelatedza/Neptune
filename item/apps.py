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

    #Following class methods to be used in other modules and apps. Above methods intended for internal use of this module.
    @classmethod
    def create_item_with_attrs(self, input):
    #creates item and populate its properties values.
        itemT = ItemType.objects.get(id=input['itemTypeID'])
        item = self.create_item(input['itemName'], itemT)

        attributes = input['attributes']

        for attr in attributes:
            attribute = Attribute.objects.get(id=attr['id'])
            self.create_item_attr_value(item, attribute, attr['value'])

    @classmethod
    def create_type_with_attrs(self, input):
    #creates a new item type and its attributes and links them.
        try:

            itemType = self.create_itemType(input['itemType'], input['itemType'])
            for attr in input['attributes']:
                newAttr = self.create_attribute(attr['label'], attr['dataType'])
                self.create_item_attr_relation(itemType, newAttr)

            return True
        except:
            return False

    @classmethod
    def get_item_values(self, itemID):
    #returns a dict of attribute values for an item; {attribute label: value}
        item = Item.objects.get(id=itemID)
        values = {}
        objs = ItemAttributeValue.objects.all().filter(item=item)

        for obj in objs:
            valueLabel =  obj.attribute.label
            value = obj.value
            values[valueLabel] = value

        return values

    @classmethod
    def get_item_type_attrs(self, itemTypeID):
    #expects an itemType ID
    #returns a dict with attribute types: {attribute id: attribute label)
        itemType = ItemType.objects.get(id=itemTypeID)
        itAts = ItemAttribute.objects.all().filter(itemType=itemType)
        result = {}

        for itAt in itAts:
            result[itAt.attribute.id] = itAt.attribute.label

        return result

    @classmethod
    def get_all_item_types(self):
    #return all item types: {itemTypeID:ItemTypeName}
        result = {}
        for itemType in ItemType.objects.all():
            result[itemType.id] = itemType.name
        return result

    @classmethod
    def get_all_items(self):
        result = {}
        for item in Item.objects.all():
            result[item.id] = item.name
        return result



class HandleItemTypes(object):
    pass
