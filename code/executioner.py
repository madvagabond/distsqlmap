#!/usr/bin/python
from distributed import Executor 
import config
import argparse
def inject(url): 
	import config 
	from pymongo import MongoClient
	import os 
        #connstring = config.db['host'] + ":" + config.db['port']
        run = "sqlmap -u " + url + ' --batch '
        command = os.popen(run).read()
        data = {'url' : url, 'output' : command}
        client = MongoClient('192.168.1.14:27017')
        dbn = config.db['dbname']
        db = client[dbn]
        results = db.results
        results.insert(data)
	return command

executor = Executor()
parser = argparse.ArgumentParser()
parser.add_argument("-f")
args = parser.parse_args()
links = []
s = open(args.f, 'r')
for x in s:
    links.append(x.rstrip().replace("\n", ""))

job = executor.map(inject, links)
print executor.gather(job)
