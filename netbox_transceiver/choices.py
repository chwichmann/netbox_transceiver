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

class TransceiverTypeProfileChoices(ChoiceSet):
    # key = 'TransceiverType.profile'

    PROFILE_ETHERNET_100M = 'ethernet_100m'
    PROFILE_ETHERNET_1G = 'ethernet_1g'
    PROFILE_ETHERNET_10G = 'ethernet_10g'

    PROFILE_SONET_STM1 = 'stm1'
    PROFILE_SONET_STM4 = 'stm4'
    PROFILE_SONET_STM16 = 'stm16'
    PROFILE_SONET_STM64 = 'stm64'

    PROFILE_FIBERCHANNEL_1G = 'fc1'
    PROFILE_FIBERCHANNEL_4G = 'fc4'
    PROFILE_FIBERCHANNEL_8G = 'fc8'
    PROFILE_FIBERCHANNEL_10G = 'fc10'
    PROFILE_FIBERCHANNEL_16G = 'fc16'
    PROFILE_FIBERCHANNEL_32G = 'fc32'
    PROFILE_FIBERCHANNEL_64G = 'fc64'
    PROFILE_FIBERCHANNEL_128G = 'fc128'

    PROFILE_OTN_OTU1 = 'otu1'
    PROFILE_OTN_OTU2 = 'otu2'
    PROFILE_OTN_OTU2e = 'otu2e'
    PROFILE_OTN_OTU25 = 'otu25'
    PROFILE_OTN_OTU3 = 'otu3'
    PROFILE_OTN_OTU3e = 'otu3e'
    PROFILE_OTN_OTU50 = 'otu50'
    PROFILE_OTN_OTU4 = 'otu4'
    PROFILE_OTN_OTUC2 = 'otuc2'
    PROFILE_OTN_OTUC4 = 'otuc4'
   
    CHOICES = (
        ('Ethernet', (
            (PROFILE_ETHERNET_100M, '100M'),
            (PROFILE_ETHERNET_1G, '1G'),
            (PROFILE_ETHERNET_10G, '10G'),
            (PROFILE_ETHERNET_10G, '100G'),
            )),
        ('SDH / PDH', (
            (PROFILE_SONET_STM1, 'STM1'),
            (PROFILE_SONET_STM4, 'STM4'),
            (PROFILE_SONET_STM16, 'STM16'),
            (PROFILE_SONET_STM64, 'STM64'),
            )),
        ('Fiberchannel', (
            (PROFILE_FIBERCHANNEL_1G, 'FC1'),
            (PROFILE_FIBERCHANNEL_4G, 'FC4'),
            (PROFILE_FIBERCHANNEL_8G, 'FC8'),
            (PROFILE_FIBERCHANNEL_10G, 'FC10'),
            (PROFILE_FIBERCHANNEL_16G, 'FC16'),
            (PROFILE_FIBERCHANNEL_32G, 'FC32'),
            (PROFILE_FIBERCHANNEL_64G, 'FC64'),
            (PROFILE_FIBERCHANNEL_128G, 'FC128'),
            )),
        ('OTN', (
            (PROFILE_OTN_OTU1, 'OTU1'),
            (PROFILE_OTN_OTU2, 'OTU2'),
            (PROFILE_OTN_OTU2e, 'OTU2e'),
            (PROFILE_OTN_OTU25, 'OTU25'),
            (PROFILE_OTN_OTU3, 'OTU3'),
            (PROFILE_OTN_OTU3e, 'OTU3e'),
            (PROFILE_OTN_OTU50, 'OTU50'),
            (PROFILE_OTN_OTU4, 'OTU4'),
            (PROFILE_OTN_OTUC2, 'OTUC2'),
            (PROFILE_OTN_OTUC4, 'OTUC4'),
            )),
        )

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
