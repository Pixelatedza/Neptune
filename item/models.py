#Ignore Herco's english in this file.

from django.db import models

class ItemType(models.Model):
    #different item types
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    #different items
    name = models.CharField(max_length=255)
    itemType = models.ForeignKey(ItemType)
    def __str__(self):
        return self.name

class Property(models.Model):
    #different properties
    label = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ItemProperty(models.Model):
    #which specific items has which properties?
    itemTypeID = models.ForeignKey(ItemType)
    propertyID = models.ForeignKey(Property)

    def __str__(self):
        return self.itemTypeID

class ItemPropertyValue(models.Model):
    #which value belong to a property for a specific item.
    itemID = models.ForeignKey(Item)
    propertyID = models.ForeignKey(Property)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.itemID
