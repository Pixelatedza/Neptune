from django.conf import settings
from django.core.exceptions import ValidationError
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
        except ValidationError as e:
            return e.messages[0]

class HandleItems(Items):

    def __init__(self, data):
        self.data = data
        self.errors = []

    def _validate_single_fields(self, data):
        errors = {}

        for k, v in data.iteritems():
            _id = k
            value = v
            attr_errors = {}

            try:
                attr = Attribute.objects.get(id=_id)
            except:
                attr_errors[_id] = 'No attributes exist with given id.'

            if not value and value != 0:
                attr_errors['value'] = 'No value given for attribute.'

            if attr_errors:
                errors[_id] = attr_errors
            else:
                error = self._is_valid_data(attr.dataType, value)
                if error:
                    errors[_id] = error

        return errors

    @classmethod
    def delete_item(self, itemPK):
        item = Item.objects.get(pk=itemPK)
        item.archived = True
        item.save()

    def is_valid(self):
        #validate input for item creation/updating.

        self.errors = {}
        validated = True

        #expected input for item creation:
        # {
        #   'itemType': '1',
        #   'itemName': '320d',
        #   '232': 'almost grey',
        #   '23': 'The fastest diesel',
        #   '28': 'Greater than beetle'
        # }

        #expected input for item update:
        # {
        #   'itemPK: '1',
        #   'itemType': '1',
        #   'itemName': '320d',
        #   '232': 'almost grey',
        #   '23': 'The fastest diesel',
        #   '28': 'Greater than beetle'
        # }

        temp = self.data.copy()

        create = True

        if 'itemPK' in temp:
            create = False
            del temp['itemPK']

        if 'itemType' in temp:
            try:
                ItemType.objects.get(id=temp['itemType'])
            except:
                self.errors['itemType'] ='itemType does not exist.'
                validated = False
        else:
            self.errors['itemType'] = 'No itemType given.'
            validated = False

        del temp['itemType']

        if 'itemName' not in temp:
            self.errors['itemName'] = 'No itemName given.'
            validated = False
        else:
            del temp['itemName']

        attrErrors = self._validate_single_fields(temp)

        if attrErrors:
            self.errors = attrErrors
            validated = False

        if validated:
            if create:
                self._create_item_with_attributes(self.data)
                return True
            else:
                self._update_item_and_attributes(self.data)
                return True
        else:
            return False

    #private methods
    def _create_item(self, name, itemType):
        obj = Item(name=name, itemType=itemType)
        obj.save()
        return obj

    def _create_item_with_attributes(self, data):
    #creates item and populate its properties values.
        itemT = ItemType.objects.get(id=data['itemType'])
        item = self._create_item(data['itemName'], itemT)

        del data['itemType']
        del data['itemName']

        for k, v in data.iteritems():
            attribute = Attribute.objects.get(id=k)
            self._create_item_attr_value(item, attribute, v)

    def _update_item_and_attributes(self, data):
        #updates item and its properties values.
        item = Item.objects.get(pk=data['itemPK'])
        itemT = ItemType.objects.get(id=data['itemType'])

        item.name = data['itemName']
        item.save()

        del data['itemPK']
        del data['itemType']
        del data['itemName']

        for k, v in data.iteritems():
            # If an item was created without a value for a specific field, that value
            # will not show up in itemAttributeValue. This will cause an DoesNotExist
            # error. Now it will create that itemAttributeValue if it does not exist.
            try:
                attribute = ItemAttributeValue.objects.get(item=item.pk, attribute=k)
                attribute.value = v
                attribute.save()
            except:
                attribute = Attribute.objects.get(id=k)
                self._create_item_attr_value(item, attribute, v)

    @classmethod
    def get_item_values(self, itemID):
    #returns a dict of field values for an item
        item = Item.objects.get(id=itemID)
        fields = {}
        objs = ItemAttributeValue.objects.all().filter(item=item)

        for obj in objs:
            fields.update({obj.attribute.label: obj.value})

        return {'item': item.name, 'fields': fields, 'itemType': item.itemType.name}

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
    def get_all_items_for_type(self, itemTypePK):
        #Return all items of a specified item type, except if it is archived.
        returnItems = []
        itemType = ItemType.objects.get(pk=itemTypePK)

        for item in Item.objects.all().filter(itemType=itemType):
            if not item.archived:
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

            #dataType = True
            if not dataType:
                attr_errors['dataType'] = 'No dataType given.'
                #dataType = False
            elif dataType not in ['str', 'int', 'dat', 'tim']:
                attr_errors['dataType'] = 'dataType not allowed.'
                #dataType = False

            if not default:
                attr['default'] = ''
            else:
                if dataType:
                    error = self._is_valid_data(dataType, default)
                    if error:
                        attr_errors['default'] = error

            ## Requried is nie 'n required field nie?
            # if not required:
            #     attr_errors['required'] = 'No required given.'

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
                    newAttr = self._create_attribute(attr['label'], attr['dataType'], attr.get('default',None), attr.get('required',False))
                    self._create_item_attr_relation(itemType, newAttr)
                return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_all_item_types(self):
    #return all item types: {itemTypeID:ItemTypeName}
        result = {}
        for itemType in ItemType.objects.all():
            result[itemType.id] = itemType.name
        return result

    @classmethod
    def get_item_type_attrs(self, itemTypePK):
    #expects an itemType name
    #returns a dict with attribute types as follows:
    # {'itemTypeId': 0, 'fields': [{'fieldId': 0, 'dataType': 'str', 'label': 'Name'}]}

        fields = []
        #itemType = ItemType.objects.get(pk=itemTypePK)
        itAts = ItemAttribute.objects.all().filter(itemType=itemTypePK)

        return itAts