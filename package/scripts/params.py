#!/usr/bin/env python
from resource_management import *

# config object that holds the configurations declared in the config xml file
config = Script.get_config()

# store the log file for the service from the 'ntpd.log' property of the 'ntpd-config.xml' file
stack_log = config['configurations']['ntpd-config']['ntpd.log']

