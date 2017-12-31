from django.apps import AppConfig

class NepCore(AppConfig):
    name = 'nepcore'
    verbose_name = "Neptune"
    
class NepAuth(AppConfig):
    name = 'nepauth'
    verbose_name = "Neptune Authorization"