#!/usr/bin/env python
from resource_management import *

class Master(Script):
    def install(self, env):
        # Install packages listed in metainfo.xml
        self.install_packages(env)
        #if any other install steps were needed they can be added here

    #To stop the service, use the linux service stop command and pipe output to log file
    def stop(self, env):
        import params
        env.set_params(params)
        Execute('service ntpd stop >>' + params.stack_log)

    #To start the service, use the linux service start command and pipe output to log file
    def start(self, env):
        import params
        env.set_params(params)
        Execute('service ntpd start >>' + params.stack_log)

    #To get status of the, use the linux service status command
    def status(self, env):
        import params
        Execute('service ntpd status')

if __name__ == "__main__":
    Master().execute()
