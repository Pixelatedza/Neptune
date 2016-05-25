from django.db import models
from django.conf import settings

class ItemType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)

    def natural_key(self):
        return {"pk": self.pk, "name":self.name, "description":self.description}

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    itemType = models.ForeignKey(ItemType)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("export_csv","Can Export CSV"),
            ("send_email","Can Send via Email")
        )

class Attribute(models.Model):
    #different properties

    ITEM_TYPES = (('str', 'String'),
              ('int', 'Integer'),
              ('dat', 'Date'),
              ('tim', 'Time'))

    label = models.CharField(max_length=50)
    dataType = models.CharField(max_length=50, choices=ITEM_TYPES, default='str')
    defaultValue = models.CharField(max_length=50, null=True, blank=True)
    required = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.label

class ItemAttribute(models.Model):
    #item type and attribute relationship.
    itemType = models.ForeignKey(ItemType)
    attribute = models.ForeignKey(Attribute)

    def __str__(self):
        return self.itemType.name

class ItemAttributeValue(models.Model):
    #item, attribute and value.
    item = models.ForeignKey(Item)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.item.name