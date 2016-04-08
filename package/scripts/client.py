#!/usr/bin/env python
from resource_management import *

class Client(Script):
    def install(self, env):
        self.install_packages(env)
        self.configure(env)

    def configure(self, env):
        import params
        env.set_params(params)
        # This is actually not a service, it just syncs system time instantly
        Execute('service ntpdate start')
        pass

    # Start means configure for the client
    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        self.configure(env)
        pass

    # Do nothing, no need to stop the client
    def stop(self, env, upgrade_type=None):
        pass

    def status(self, env):
        raise ClientComponentHasNoStatus()

if __name__ == "__main__":
    Client().execute()
