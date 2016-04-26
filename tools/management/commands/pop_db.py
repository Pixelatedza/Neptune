from django.core.management.base import BaseCommand

from item.apps import HandleItems
    #create_type_with_attrs, get_item_type_attrs, get_item_values,create_item_with_attrs

from django.conf import settings

class Command(BaseCommand):
    help = """Add testing data and test stuff."""

    def handle(self, *args, **options):

        #EXAMPLES:

        FRIDGE = {'itemType': 'Car','attributes': [{'label': 'length', 'dataType': 'int'},
                                     {'label': 'weight', 'dataType': 'int'},
                                     {'label': 'colour', 'dataType': 'str'}]
                      }
        #create taskType and Attribute example:
        # if HandleItems.create_type_with_attrs(FRIDGE):
        #     print 'Yeeeahhhh!'


        #retrieval of attributes for an item type example:
        # item = HandleItems.get_all_item_types()
        # itemName = item.itervalues().next()
        #
        # for key, value in item.iteritems():
        #     if value == itemName:
        #         itemID = key
        #
        # attrs = HandleItems.get_item_type_attrs(itemID)
        #
        # for attr in attrs:
        #     print attr, attrs[attr]
        #
        # #Example of an item create:
        # newItem = {'itemTypeID': itemID}
        # newItem['itemName'] = 'TaTa'
        # newItem['attributes'] = []
        # for attr in attrs:
        #     newItem['attributes'].append({'id' : attr, 'value' : 'not too sure what val'})
        #
        # HandleItems.create_item_with_attrs(newItem)

        #Example of getting values for an item:
        items = HandleItems.get_all_items()
        item = items.itervalues().next()

        for key, value in items.iteritems():
            if value == item:
                itemID = key
        values = HandleItems.get_item_values(itemID)

        print values
