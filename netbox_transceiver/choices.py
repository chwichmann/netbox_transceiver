from utilities.choices import ChoiceSet

class TransceiverTypePhysicChoices(ChoiceSet):
    key = 'TransceiverType.physic'

    TYPE_MULTIMODE = 'multimode'
    TYPE_SINGLEMODE = 'singlemode'
    TYPE_ELECTRICAL = 'electrical'
    TYPE_MULTIMODE_BIDI = 'multimode_bidi'
    TYPE_SINGLEMODE_BIDI = 'singlemode_bidi'

    CHOICES = [
        (TYPE_MULTIMODE, 'Multimode'),
        (TYPE_SINGLEMODE, 'Singlemode'),
        (TYPE_ELECTRICAL, 'Electrical'),
        (TYPE_MULTIMODE_BIDI, 'Multimode BiDi'),
        (TYPE_SINGLEMODE_BIDI, 'Singlemode BiDi'),
    ]

class TransceiverTypeFormChoices(ChoiceSet):
    key = 'TransceiverType.form'

    TYPE_GBIC = 'gbic'
    TYPE_SFP = 'sfp'
    TYPE_SFP_PLUS = 'sfp_plus'
    TYPE_XFP = 'xfp'
    TYPE_SFP28 = 'sfp28'
    TYPE_SFP56 = 'sfp56'
    TYPE_QSFP_PLUS = 'qsfp_plus'
    TYPE_QSFP28 = 'qsfp28'
    TYPE_QSFP56 = 'qsfp56'
    TYPE_QSFP_DD = 'qsfp_dd'
    TYPE_CFP = 'cfp'
    TYPE_CFP2 = 'cfp2'
    TYPE_CFP4 = 'cfp4'
    TYPE_CFP8 = 'cfp8'
    TYPE_OSFP = 'osfp'
    TYPE_CDFP = 'cdfp'

    CHOICES = [
        (TYPE_GBIC, 'GBIC'),
        (TYPE_SFP, 'SFP'),
        (TYPE_SFP_PLUS, 'SFP+'),
        (TYPE_XFP, 'XFP'),
        (TYPE_SFP28, 'SFP28'),
        (TYPE_SFP56, 'SFP56'),
        (TYPE_QSFP_PLUS, 'QSFP+'),
        (TYPE_QSFP28, 'QSFP28'),
        (TYPE_QSFP56, 'QSFP56'),
        (TYPE_QSFP_DD, 'QSFP-DD'),
        (TYPE_CFP, 'CFP'),
        (TYPE_CFP2, 'CFP2'),
        (TYPE_CFP4, 'CFP4'),
        (TYPE_CFP8, 'CFP8'),
        (TYPE_OSFP, 'OSFP'),
        (TYPE_CDFP, 'CDFP'),
    ]

class TransceiverTypeProfileGroupChoices(ChoiceSet):
    key = 'TransceiverTypeProfile.group'

    GROUP_ETHERNET = 'ethernet'
    GROUP_SONET = 'sonet'
    GROUP_FIBERCHANNEL = 'fiberchannel'
    GROUP_OTN = 'otn'
    GROUP_OTHER = 'other'
   
    CHOICES = [
        (GROUP_ETHERNET, 'Ethernet'),
        (GROUP_SONET, 'SDH / PDH'),
        (GROUP_FIBERCHANNEL,'Fiberchannel'),
        (GROUP_OTN, 'OTN'),
        (GROUP_OTHER,'Other'),
    ]
      

class TransceiverStatusChoices(ChoiceSet):
    key = 'Transceiver.status'

    STATUS_OFFLINE = 'offline'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_STAGED = 'staged'
    STATUS_FAILED = 'failed'
    STATUS_INVENTORY = 'inventory'
    STATUS_DECOMMISSIONING = 'decommissioning'

    CHOICES = [
        (STATUS_OFFLINE, 'Offline', 'gray'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_STAGED, 'Staged', 'blue'),
        (STATUS_FAILED, 'Failed', 'red'),
        (STATUS_INVENTORY, 'Inventory', 'purple'),
        (STATUS_DECOMMISSIONING, 'Decommissioning', 'yellow'),
    ]
