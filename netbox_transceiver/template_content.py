from extras.plugins import PluginTemplateExtension
from .models import Transceiver

class DeviceTransceiverList(PluginTemplateExtension):
    model='dcim:device'

    def left_page(self):
        return self.render('netbox_transceiver/device_include.html', extra_context={
                'netbox_Transceiver': Transceiver.objects.filter(device=self.context['device']),
            })

template_extension = [DeviceTransceiverList]