from django.db import models

class ItemType(models.Model):
    #different item types
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    #different item
    name = models.CharField(max_length=50)
    itemType = models.ForeignKey(ItemType)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    #different properties
    ITEM_TYPES = (('str', 'String'),
                  ('int', 'Integer'),
                  ('date', 'Date'))

    label = models.CharField(max_length=50)
    dataType = models.CharField(max_length=50, choices=ITEM_TYPES, default='str')

    def __str__(self):
        return self.name

class ItemAttribute(models.Model):
    #which specific items has which properties?
    itemType = models.ForeignKey(ItemType)
    attribute = models.ForeignKey(Attribute)

    def __str__(self):
        return self.itemType.name

class ItemAttributeValue(models.Model):
    #which value belong to a property for a specific item.
    item = models.ForeignKey(Item)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.itemID