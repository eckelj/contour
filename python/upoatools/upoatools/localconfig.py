import os

from appdirs import user_config_dir
from configobj import ConfigObj

# Create configuration directory in case it does not exist.
try:
    os.makedirs(user_config_dir('upoatools'))
except OSError:
    if not os.path.isdir(user_config_dir('upoatools')):
        raise

# Determine cross-platform configuration file path.
configfile = os.path.join(user_config_dir('upoatools'), 'config')

# Create configuration object.
config = ConfigObj(configfile)

# Initialise configuration.
if 'btckeys' not in config:
    config['btckeys'] = {}
