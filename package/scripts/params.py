#!/usr/bin/env python
from resource_management import *

# server configurations
config = Script.get_config()

stack_log = config['configurations']['ntpd-config']['ntpd.log']

