from django.urls import reverse

from django.db import models
from netbox.models import NetBoxModel

from .choices import *

class TransceiverTypeProfile(NetBoxModel):
    profile = models.CharField(
        max_length=50,
        unique=True,
    )
    group = models.CharField(
        max_length=50,
        choices=TransceiverTypeProfileGroupChoices)

    class Meta:
        ordering = ('group', 'profile')
        constraints = (
            models.UniqueConstraint(
                fields=('group', 'profile'),
                name='%(app_label)s_%(class)s_unique_group_profile'
            ),
        )

    def __str__(self):
        return self.profile

    def get_absolute_url(self):
        return reverse('plugins:netbox_transceiver:transceivertypeprofile', args=[self.pk])

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
        help_text=('Discrete part number (optional)')
    )
    physic = models.CharField(
        max_length=50,
        choices=TransceiverTypePhysicChoices,
        blank=True,
        null=True,
        verbose_name='Physical connection',
        help_text=('The pyhsical connection of the transceiver (optional)')
    )
    form = models.CharField(
        max_length=50,
        choices=TransceiverTypeFormChoices,
        blank=True,
        null=True,
        verbose_name='Form factor',
        help_text=('The form factor of the transceiver (optional)')
    )
    tx_power_min = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name='Min Tx Power (dBm)'
    )
    tx_power_max = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name='Max Tx Power (dBm)'
    )
    rx_power_min = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name='Min Rx Power (dBm)'
    )
    rx_power_max = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name='Max Rx Power (dBm)'
    )
    profiles = models.ManyToManyField(
        to=TransceiverTypeProfile,
        related_name='profiles',
        blank=True,
        verbose_name='Profiles',
        )
    comments = models.TextField(
        blank=True
        )

    #clone_fields = ('manufacturer')

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

    def power_budget_max(self):
        if self.rx_power_min and self.tx_power_min:
            budget = self.rx_power_min - self.tx_power_min
            if budget < 0:
                budget = budget * -1
            return budget

    def power_budget_min(self):
        if self.rx_power_max and self.tx_power_max:
            budget = self.rx_power_max - self.tx_power_max
            if budget < 0:
                budget = budget * -1
            return budget

class Transceiver(NetBoxModel):
    """
    The Transceiver represents the field-installable component within a interface. 
    One interface can house one transceiver
    """
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='transceivers'
    )
    interface = models.OneToOneField(
        to='dcim.Interface',
        on_delete=models.CASCADE,
        related_name='transceivers'
    )
    transceiver_type = models.ForeignKey(
        to=TransceiverType,
        on_delete=models.PROTECT,
        related_name='instances'
    )
    profile = models.ForeignKey(
            to=TransceiverTypeProfile,
            on_delete=models.PROTECT,
            related_name='transceiver_profile'
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
        help_text=('A unique tag used to identify this device')
    )

    class Meta:
        ordering = ('interface',)
        verbose_name = 'Transceiver'
        verbose_name_plural = 'Transceivers'

    def __str__(self):
        return f'{self.device.name}: {self.interface} ({self.pk})'

    #def save(self, *args, **kwargs):
    #    is_new = not bool(self.pk)

    def get_absolute_url(self):
        return reverse('plugins:netbox_transceiver:transceiver', args=[self.pk])

    def get_status_color(self):
        return TransceiverStatusChoices.colors.get(self.status)

    def name(self):
        return f'{self.device.name}: {self.interface}'