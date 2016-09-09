#!/usr/bin/python 
db = dict(
	host = '192.168.1.14',
	port = '27017',
	dbname = 'distsqlmap'
)

scheduler = dict(
	host = '192.168.1.14',
	port = '8786'
)
workers = dict(
        host = ['192.168.1.26', '192.168.1.24']
)
