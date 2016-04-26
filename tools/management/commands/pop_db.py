from django.core.management.base import BaseCommand

from item.apps import HandleItems
    #create_type_with_attrs, get_item_type_attrs, get_item_values,create_item_with_attrs

from django.conf import settings

class Command(BaseCommand):
    help = """Add testing data and test stuff."""

    def handle(self, *args, **options):

        FRIDGET = {'itemType': 'Fridge'}
        FRIDEATTRS = {'attributes': [{'label': 'length', 'dataType': 'int'},
                                     {'label': 'weight', 'dataType': 'int'},
                                     {'label': 'colour', 'dataType': 'str'}
                                     ]
                      }

        # if HandleItems.create_type_with_attrs(FRIDGET):
        #     print 'Yeeeahhhh!'

        item = HandleItems.get_item_types()[0]

        attrs = HandleItems.get_item_type_attrs(item)

        for attr in attrs:
            print attr, attrs[attr]