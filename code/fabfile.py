#!/usr/bin/python
from fabric.api import env
from fabric.operations import run, put
import config
env.hosts = [] 
for x in config.workers['host']:
    env.hosts.append(x.rstrip().replace("\n",""))

#def upload():
#	put('../code', '/home/vagrant')
def worker(): 
	command = 'dask-worker ' + config.scheduler['host'] + ':' + config.scheduler['port'] + ' &'
	run(command) 

def scheduler(): 
    command = 'dask-scheduler ' + config.scheduler['host'] + ' &'
    run(command)




