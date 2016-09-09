#!/usr/bin/python
from pymongo import MongoClient
import config 
constring = config.db['host'] + ':' + config.db['port']
conn = MongoClient(constring)
name = config.db['dbname']
datab = conn[name]
res = datab.create_collection('results')

