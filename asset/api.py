from serializers import PrettyJSONSerializer
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from asset.models.base import *

class DesktopComputerResource(ModelResource):

	class Meta:
		queryset = DesktopComputer.objects.all()
		resource_name = 'desktop_computer'
		serializer = PrettyJSONSerializer()

class NoteBookResource(ModelResource):

	class Meta:
		queryset = NoteBook.objects.all()
		resource_name = 'notebook'
		serializer = PrettyJSONSerializer()

class PrinterResource(ModelResource):

	class Meta:
		queryset = Printer.objects.all()
		resource_name = 'printer'
		serializer = PrettyJSONSerializer()

class StorageResource(ModelResource):

	class Meta:
		queryset = Storage.objects.all()
		resource_name = 'storage'
		serializer = PrettyJSONSerializer()

class ServerResource(ModelResource):

	class Meta:
		queryset = Server.objects.all()
		resource_name = 'server'
		serializer = PrettyJSONSerializer()

class DisplayResource(ModelResource):

	class Meta:
		queryset = Display.objects.all()
		resource_name = 'display'
		serializer = PrettyJSONSerializer()

class SoftwareResource(ModelResource):

	class Meta:
		queryset = Software.objects.all()
		resource_name = 'software'
		serializer = PrettyJSONSerializer()

class ComponentResource(ModelResource):

	class Meta:
		queryset = Component.objects.all()
		resource_name = 'component'
		serializer = PrettyJSONSerializer()

class InputDeviceResource(ModelResource):

	class Meta:
		queryset = InputDevice.objects.all()
		resource_name = 'input_device'
		serializer = PrettyJSONSerializer()

class PrinterConResource(ModelResource):

	class Meta:
		queryset = PrinterCon.objects.all()
		resource_name = 'printer_con'
		serializer = PrettyJSONSerializer()

class AccessoryResource(ModelResource):

	class Meta:
		queryset = Accessory.objects.all()
		resource_name = 'accessory'
		serializer = PrettyJSONSerializer()

class NetworkDeviceResource(ModelResource):

	class Meta:
		queryset = NetworkDevice.objects.all()
		resource_name = 'network_device'
		serializer = PrettyJSONSerializer()

class TabletResource(ModelResource):

	class Meta:
		queryset = Tablet.objects.all()
		resource_name = 'tablet'
		serializer = PrettyJSONSerializer()

class DiagnosticMachineResource(ModelResource):

	class Meta:
		queryset = DiagnosticMachine.objects.all()
		resource_name = 'diagnosticmachine'
		serializer = PrettyJSONSerializer()

