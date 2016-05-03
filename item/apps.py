from django.conf import settings
from nepcore.forms.fields import CUSTOM_FIELD_MAP

from item.models import ItemType, Item, Attribute, ItemAttribute, ItemAttributeValue

class Items(object):

    def _create_item_attr_relation(self, itemType, attr):
        obj = ItemAttribute(itemType=itemType, attribute=attr)
        obj.save()

    def _create_item_attr_value(self, item, attr, value):
        obj = ItemAttributeValue(item=item, attribute=attr, value=value)
        obj.save()

    def _is_valid_data(self, dataType, data):
        try:
            field = CUSTOM_FIELD_MAP[dataType]()
            field.clean(data)
            return False
        except Exception as e:
            return e.msg

class HandleItems(Items):

    def __init__(self, data):
        self.data = data
        self.errors = []

    def _validate_attributes(self, data):
        errors = {}

        for k, v in data.iteritems():
            _id = k
            value = v
            attr_errors = {}

            try:
                attr = Attribute.objects.get(id=_id)
            except:
                attr_errors[_id] = 'No attributes exist with given id.'

            if not value:
                attr_errors['value'] = 'No value given for attribute.'

            if attr_errors:
                errors[_id] = attr_errors
            else:
                error = self._is_valid_data(attr.type, value)
                if error:
                    attr_errors['value'] = value
                    attr_errors['error'] = error
                    errors[_id] = attr_errors

        return errors

    def is_valid(self):
        #validate input for item creation.

        self.errors = {}
        validated = True

        #expected input:
        # {
        #   ‘itemType’: ‘1’,
        #   ‘itemName’: ‘320d’,
        #   ‘232’: ‘grey’,
        #   ’23’: ‘The fastest’,
        #   ’28’: ‘Greater than merc’
        # }

        temp = self.data

        if 'itemType' in temp:
            try:
                ItemType.objects.get(id=temp['itemType'])
                self.errors['itemType'] ='itemType already exists.'
                validated = False
            except:
                pass
        else:
            self.errors['itemType'] = 'No itemType given.'
            validated = False

        del temp['itemType']

        if 'itemName' not in temp:
            self.errors['itemName'] = 'No itemName given.'
            validated = False
        else:
            del temp['itemName']


        attrErrors = self._validate_attributes(temp)

        if attrErrors:
            self.errors['attributes'] = attrErrors
            validated = False

        if validated:
            self._create_item_with_attributes(self, self.data)
            return True
        else:
            return False

    #private methods
    def _create_item(self, name, itemType):
        obj = Item(name=name, itemType=itemType)
        obj.save()
        return obj

    #public methods
    def _create_item_with_attributes(self, data):
    #creates item and populate its properties values.
        itemT = ItemType.objects.get(id=data['itemType'])
        item = self._create_item(data['itemName'], itemT)

        del data['itemType']
        del data['itemName']

        for k, v in data.iteritems():
            attribute = Attribute.objects.get(id=k)
            self._create_item_attr_value(item, attribute, v)

    @classmethod
    def get_item_values(self, itemID):
    #returns a dict of field values for an item
        item = Item.objects.get(id=itemID)
        fields = []
        objs = ItemAttributeValue.objects.all().filter(item=item)

        for obj in objs:
            fields.append({'label': obj.attribute.label,
                           'value': obj.value})

        return {'item': item.name, 'fields': fields}

    @classmethod
    def get_all_items(self):
        #Returns all items in the db.
        returnItems = []
        for item in Item.objects.all():
            returnItems.append({'itemID': item.id,
                                'itemName': item.name,
                                'itemType': item.itemType.name})

        return {'items': returnItems}

    @classmethod
    def get_all_items_for_type(self, itemTypeName):
        #Return all items of a specified item type.
        returnItems = []
        itemType = ItemType.objects.get(name=itemTypeName)

        for item in Item.objects.all().filter(itemType=itemType):
            returnItems.append({'itemID': item.id,
                                'itemName': item.dataType})

        return {'items': returnItems}

class HandleItemTypes(Items):

    def __init__(self, data):
        self.errors = []
        self.data = data

    def _validate_attributes(self, data):
        #validate attributes when new ones are created.
        #Code needs revision. Crude, but works. Can be better. :'(
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

            dataType = True
            if not dataType:
                attr_errors['dataType'] = 'No dataType given.'
                dataType = False
            elif dataType not in ['str', 'int', 'dat', 'tim']:
                attr_errors['dataType'] = 'dataType not allowed.'
                dataType = False

            if not default:
                attr['default'] = ''
            else:
                if dataType:
                    error = self._is_valid_data(dataType, default)
                    if error:
                        attr_errors['default'] = error

            if not required:
                attr_errors['required'] = 'No required given.'

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
        else:
            self.errors['itemType'] = 'No itemType given.'
            validated = False

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
    def get_item_type_attrs(self, itemTypeName):
    #expects an itemType name
    #returns a dict with attribute types as follows:
    # {'itemTypeId': 0, 'fields': [{'fieldId': 0, 'dataType': 'str', 'label': 'Name'}]}

        fields = []
        itemType = ItemType.objects.get(name=itemTypeName)
        itAts = ItemAttribute.objects.all().filter(itemType=itemType)
        result = {}

        for itAt in itAts:
            attr = itAt.attribute
            print attr.dataType
            fields.append({'fieldId': attr.id,
                           'dataType': attr.dataType,
                           'label': attr.label})

        return fields