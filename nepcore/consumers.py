from channels import Group
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
from nepcore.models import NEPMenuBinding
        
class Demultiplexer(WebsocketDemultiplexer):
    
    consumers = {
        "menu": NEPMenuBinding.consumer,
    }
    
    groups = ['menu-updates']