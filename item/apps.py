from django.conf import settings

from item.models import ItemType, Item, Attribute, ItemAttribute, ItemAttributeValue

class Items(object):

    def _create_item_attr_relation(self, itemType, attr):
        obj = ItemAttribute(itemType=itemType, attribute=attr)
        obj.save()

    def _create_item_attr_value(self, item, attr, value):
        obj = ItemAttributeValue(item=item, attribute=attr, value=value)
        obj.save()

class HandleItems(Items):

    def __init__(self):
        self.errors = []

    #private methods
    def _create_item(self, name, itemType):
        obj = Item(name=name, itemType=itemType)
        obj.save()
        return obj

    #public methods
    def create_item_with_attrs(self, input):
    #creates item and populate its properties values.
        itemT = ItemType.objects.get(id=input['itemTypeID'])
        item = self._create_item(input['itemName'], itemT)

        attributes = input['attributes']

        for attr in attributes:
            attribute = Attribute.objects.get(id=attr['id'])
            self._create_item_attr_value(item, attribute, attr['value'])

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
    def get_all_items(self):
        result = {}
        for item in Item.objects.all():
            result[item.id] = item.name
        return result

class HandleItemTypes(Items):

    def __init__(self, data):
        self.errors = []
        self.data = data

    def _validate_attributes(self, data):
        errors = {}
        for attr in data:
            index = 0
            attr_errors = {}
            label= ''
            dataType= ''
            required= ''
            default= ''
            for k, v in attr.iteritems():
                if k == 'index':
                    index = v
                elif k == 'label':
                    label = v
                elif k == 'dataType':
                    dataType = v
                elif k == 'required':
                    required = v
                elif k == 'default':
                    default = v

            if not label:
                attr_errors['label'] = 'No label given.'

            if not dataType:
                attr_errors['dataType'] = 'No dataType given.'
            elif dataType not in ['str', 'int', 'dat', 'tim']:
                print dataType
                attr_errors['dataType'] = 'dataType not allowed.'

            if not required:
                attr_errors['required'] = 'No required given.'

            if not default:
                attr['default'] = ''
            else:
                #TODO VALIDATE AGAINST DATA TYPE
                pass

            if attr_errors:
                errors[index] = attr_errors

        return data, errors

    def is_valid(self):
        #validate input for dataType and attribute creation.

        self.errors = {}
        validated = True

        if 'itemType' in self.data:
            try:
                ItemType.objects.get(name=self.data['itemType'])
                self.errors['itemType'] ='itemType already exists.'
                validated = False
            except:
                pass

        data2, attrErrors = self._validate_attributes(self.data['attributes'])
        self.data['attributes'] = data2
        if attrErrors:
            self.errors['attributes'] = attrErrors
            validated = False

        if validated:
            self._create_type_with_attrs(self.data)
            return True
        else:
            return False

    #private methods
    def _create_itemType(self, name, description):
        obj = ItemType(name=name, description=description)
        obj.save()
        return obj

    def _create_attribute(self, label, dataType, defaultValue, required):
        obj = Attribute(label=label, dataType=dataType, defaultValue=defaultValue, required=required)
        obj.save()
        return obj

    #public methods
    def _create_type_with_attrs(self, input):
    #creates a new item type and its attributes and links them.
        try:
                itemType = self._create_itemType(input['itemType'], input['itemType'])
                for attr in input['attributes']:
                    newAttr = self._create_attribute(attr['label'], attr['dataType'], attr['default'], attr['required'])
                    self._create_item_attr_relation(itemType, newAttr)
                return True
        except Exception as e:
            print e
            return False

    @classmethod
    def get_all_item_types(self):
    #return all item types: {itemTypeID:ItemTypeName}
        result = {}
        for itemType in ItemType.objects.all():
            result[itemType.id] = itemType.name
        return result

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