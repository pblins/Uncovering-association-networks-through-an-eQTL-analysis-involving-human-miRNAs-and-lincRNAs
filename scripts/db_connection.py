#!/usr/bin/python
import MySQLdb

def connect():
    return MySQLdb.connect(host="localhost",    # your host, usually localhost
                           user="root",         # your username
                           db="geuvadis")        # name of the data base
