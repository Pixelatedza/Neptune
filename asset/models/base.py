from django.db import models

class Asset(models.Model):
	STATUSES = (
		(0,"Active"),
		(1,"Inactive"),
		(2,"Returned"),
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
		('UNKOWN', 'Unknown'),
		('HIGHLANDSPARK', 'Highlands Park'),
	)

	name = models.CharField(max_length=64, unique=True)
	serial_number = models.CharField('Serial Number',max_length=80, unique=True)
	item_code = models.CharField('Item Code',max_length=80)
	description = models.CharField('Description',max_length=200)
	manufacturer = models.CharField('Manufacturer',max_length=50)
	model_number = models.CharField('Model Number',max_length=50)
	status = models.IntegerField(choices=STATUSES)
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


	def __str__(self):
		return self.serial_number

	class Meta:
		abstract = True

class Computer(Asset):

	computer_name = models.CharField('Computer Name',max_length=100)
	nic = models.CharField('NIC',max_length=50)
	dhcp = models.CharField('DHCP', max_length=200)
	ip_address = models.GenericIPAddressField('IP Address',blank=True, null=True)
	workgroup = models.CharField('Workgroup',max_length=30)
	username = models.CharField('Username',max_length=50)
	extension = models.CharField('Extension', max_length=20)
	job_description = models.CharField('Job Description',max_length=40)
	cell_phone = models.IntegerField('Cell Phone',blank=True, null=True)
	email_address = models.EmailField('Email',blank=True, null=True)
	processor = models.CharField('Processor',max_length=30)
	ram = models.CharField('RAM',max_length=30)
	hard_drive = models.CharField('Hard Drive',max_length=30)
	display = models.CharField('Display',max_length=50)
	printer_attached = models.BooleanField('Printer attached')
	operating_system = models.CharField('Operating System',max_length=20)
	micro_win_key= models.CharField('Microsft Windows Key',max_length=30)
	micro_office_key= models.CharField('Microsoft Office Key',max_length=30)
	windows_user = models.CharField('Windows User',max_length=30)
	microsoft_office = models.CharField('Microsoft Office',max_length=20)
	openoffice = models.CharField('Openoffice',max_length=20)
	pop3_server = models.CharField('POP3 Server',max_length=20)
	smptp_server = models.CharField('SMTP Server',max_length=20)
	anti_virus = models.CharField('Anti-virus',max_length=30)
	team_viewer = models.BooleanField('Team Viewer')
	team_viewer_version = models.CharField('Team Viewer version',max_length=10)
	setup_for_itadmin = models.BooleanField('Setup for ITAdmin')
	ieexplorer_version = models.CharField('IE Explorer version',max_length=10)
	popup_blocker = models.BooleanField('Pop Blocker')
	advanced_security = models.BooleanField('Advanced Security')
	printer_installed = models.CharField('Printer installed',max_length=5)
	date_time_correct = models.BooleanField('Date/Time correct')
	region_checked = models.BooleanField('Region correct')
	alt_brow_rem = models.BooleanField('Alternative browser removed')
	rem_ill_pck = models.BooleanField('Removed illegal office')
	motovate = models.BooleanField('Motovate installed')
	etka = models.BooleanField('ETKA installed')
	elsa_pro = models.BooleanField('ELSA Pro installed')
	dnet = models.BooleanField('Dnet installed')
	elearning = models.BooleanField('ELearning installed')
	adobe_acrobat = models.CharField('Adobe Acrobat version',max_length=5)
	java_ver = models.CharField('Java version',max_length=5)
	adobe_flash = models.CharField('Adobe Flash version',max_length=5)

	def __str__(self):
		return self.serial_number

	class Meta:
		abstract = True

class DesktopComputer(Computer):

	def __str__(self):
		return self.serial_number

class DiagnosticMachine(Computer):

	odis = models.CharField('ODIS',max_length=40)

	def __str__(self):
		return self.serial_number

class NoteBook(Computer):

	def __str__(self):
		return self.serial_number

class Printer(Asset):

	spooler = models.IntegerField('Spooler number')
	spooler_name = models.CharField('Spooler name',max_length=40)
	ip_address = models.GenericIPAddressField('IP Address',max_length=20)

	def __str__(self):
		return self.spooler_name

class Storage(Asset):

	def __str__(self):
		return self.serial_number

class Server(Asset):

	def __str__(self):
		return self.serial_number

class Display(Asset):

	def __str__(self):
		return self.serial_number

class Software(Asset):

	def __str__(self):
		return self.serial_number

class Component(Asset):

	def __str__(self):
		return self.serial_number

class InputDevice(Asset):

	def __str__(self):
		return self.serial_number

class PrinterCon(Asset):

	def __str__(self):
		return self.serial_number

class Accessory(Asset):

	def __str__(self):
		return self.serial_number

class NetworkDevice(Asset):

	def __str__(self):
		return self.serial_number

class Tablet(Asset):

	def __str__(self):
		return self.serial_number