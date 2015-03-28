import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):
  
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    
    #Run any other install steps needed

  def stop(self, env):
    import params
    Execute('service ntpd stop >>' + params.stack_log)
      
  def start(self, env):
    import params
    Execute('service ntpd start >>' + params.stack_log)
	

  def status(self, env):
    import params
    Execute('service ntpd status >>' + params.stack_log)

if __name__ == "__main__":
  Master().execute()
