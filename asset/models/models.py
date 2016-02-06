from django.db import models

class Asset(models.Model):
	STATUSES = (
		(0,"Active")
		(1,"Inactive")
		(2,"Returned")
		(3,"Disposed")
	)

	CONDITION_CHOICES = (
		('NEW', 'New'),
		('GREAT', 'Great'),
		('GOOD', 'Good'),
		('SATISFACTORY', 'Satisfactory'),
		('BAD', 'Bad'),
		('POOR', 'Poor'),
	)

	LOCATION_CHOICES = (
		('HATVWPRETORIA', 'Hatfield VW Pretoria'),
		('HATVWBRYANSTON', 'Hatfield VW Bryanston'),
		('HATVWBRAAMFONTEIN', 'Hatfield VW Braamfontein'),
		('HATVWCOMMERCIAL', 'Hatfield VW Commercial'),
		('HATAUDICNTR', 'Audi Centre Hatfield'),
		('RIVAUDICNTR', 'Audi Centre Rivonia'),
		('ACCESSORIES', 'Accessories'),
		('HATTRUCKANDBUS', 'Hatfield Truck and Bus'),
		('HOLDINGS', 'Holdings'),
		('UNKOWN', 'Unkown'),
		('HIGHLANDSPARK', 'Highlands Park'),
	)

	name = models.CharField(max_length=64, unique=True)
	serial_number = models.CharField('Serial Number',max_length=80, unique=True)
	item_code = models.CharField('Item Code',max_length=80)
	description = models.CharField('Description',max_length=200)
	manufacturer = models.CharField('Manufacturer',max_length=50)
	model_number = models.CharField('Model Number',max_length=50)
	purchase_cost = models.DecimalField('Purchase Cost', max_digits=15, decimal_places=2, null=True, blank=True)
	current_value = models.DecimalField('Current Value', max_digits=15, decimal_places=2, null=True, blank=True)
	condition = models.CharField('Condtion', max_length=20, choices = CONDITION_CHOICES)
	location = models.CharField('Location',max_length=30,  choices = LOCATION_CHOICES)
	owner = models.CharField('Owner', max_length=40)
	supplier = models.CharField('Supplier', max_length=40)
	invoice_number = models.CharField('Invoice Number',max_length=40)
	date_received = models.DateField('Date received')
	retired_date = models.DateField('Date retired', blank=True, null=True)
	comments = models.TextField('Comments')
	status = models.IntegerField(choice=STATUSES)

	def __str__(self):
		return self.serial_number

	class Meta:
		abstract = True
