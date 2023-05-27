from extras.plugins import PluginTemplateExtension
from .models import Transceiver
from .tables import TransceiverTable

class DeviceTransceiverList(PluginTemplateExtension):
    model='dcim.device'

    def left_page(self):
        return self.render('netbox_transceiver/device_include.html', extra_context={
                'related_transceiver_table':  TransceiverTable(Transceiver.objects.filter(device=self.context['object']))
            }
        )

template_extensions = [DeviceTransceiverList]