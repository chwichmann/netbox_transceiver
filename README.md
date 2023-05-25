# Netbox Transceiver plugin

<p align="center"><i>NetBox Transceiver is a NetBox plugin for managing Transceivers on interfaces.</i></p>

## Features

* Create Transceiver Types with specifications, part number and asset tag
* Create your format profiles
* Assign transceiver with serial number on an interface

## Requirements

* NetBox 3.5 or higher
* Python 3.11 or higher

It may run with older versions as well...

## Installation & Configuration

### Installation

```
$ source /opt/netbox/venv/bin/activate
# Not yet! (venv) $ pip install netbox-transceiver
```

### Configuration

Add the plugin to the NetBox config. `~/netbox/configuration.py`

```python
PLUGINS = [
    "netbox_transceiver",
]
```

To permanently mount the plugin when updating NetBox:

```
echo netbox-transceiver >> ~/netbox/local_requirements.txt
```

To add the required netbox_transceiver tables to your database run the following command from your NetBox directory:

```
./manage.py migrate
```

Full reference: [Using Plugins - NetBox Documentation](https://docs.netbox.dev/en/stable/plugins/)

## Screenshots


## Contribute

Contributions are always welcome! Please see: [contributing guide](CONTRIBUTING.md)

## License

Apache 2.0