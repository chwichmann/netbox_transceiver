from django.urls import reverse

from django.db import models
from netbox.models import NetBoxModel
from django.utils.translation import gettext as _

from .choices import *

class TransceiverTypeProfile(models.Model):
    choice = models.CharField(max_length=154, unique=True)


class TransceiverType(NetBoxModel):
    """
    A TransceiverType represents a hardware element that can be installed on a interface.
    It do not change the behavior of that interface, it's simply there and is now tracked
    """

    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='transceiver_types'
    )
    model = models.CharField(
        max_length=100
    )
    part_number = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('Discrete part number (optional)')
    )
    physic = models.CharField(
        max_length=50,
        choices=TransceiverTypePhysicChoices,
        blank=True,
        verbose_name='Physical connection',
        help_text=_('The pyhsical connection of the transceiver.')
    )
    form = models.CharField(
        max_length=50,
        choices=TransceiverTypeFormChoices,
        blank=True,
        verbose_name='Form factor',
        help_text=_('The form factor of the transceiver.')
    )
    profile = models.ManyToManyField(
        to=TransceiverTypeProfile,
        choices=TransceiverTypeProfileChoices,
        blank=True,
        verbose_name='Capable profiles',
        help_text=_('The possible profiles of the transceiver.')
    )
    tx_power_min = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        verbose_name='Min Tx Power'
    )
    tx_power_max = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        verbose_name='Max Tx Power'
    )
    rx_power_min = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        verbose_name='Min Rx Power'
    )
    rx_power_max = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        verbose_name='Max Rx Power'
    )
    comments = models.TextField(
        blank=True
        )

    clone_fields = ('manufacturer')

    prerequisite_models = (
        'dcim.Manufacturer',
    )

    class Meta:
        ordering = ('manufacturer', 'model')
        constraints = (
            models.UniqueConstraint(
                fields=('manufacturer', 'model'),
                name='%(app_label)s_%(class)s_unique_manufacturer_model'
            ),
        )

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('plugins:netbox_transceiver:transceivertype', args=[self.pk])

class Transceiver(NetBoxModel):
    """
    The Transceiver represents the field-installable component within a interface. 
    One interface can house one transceiver
    """
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='interfaces'
    )
    module = models.ForeignKey(
        to='dcim.Module',
        on_delete=models.CASCADE,
        related_name='interfaces'
    )
    interface = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='transceiver'
    )
    transceiver_type = models.ForeignKey(
        to=TransceiverType,
        on_delete=models.PROTECT,
        related_name='instances'
    )
    status = models.CharField(
        max_length=50,
        choices=TransceiverStatusChoices,
        default=TransceiverStatusChoices.STATUS_PLANNED
    )
    serial = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Serial number'
    )
    description = models.CharField(
        max_length=150,
        blank=True,
    )
    asset_tag = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=True,
        verbose_name='Asset tag',
        help_text=_('A unique tag used to identify this device')
    )

    class Meta:
        ordering = ('interface',)
        verbose_name = 'Transceiver'
        verbose_name_plural = 'Transceivers'

    def __str__(self):
        return f'{self.device.name}: {self.interface.name} ({self.pk})'

    def get_absolute_url(self):
        return reverse('plugins:netbox_transceiver:transceiver', args=[self.pk])

    def get_status_color(self):
        return TransceiverStatusChoices.colors.get(self.status)