#!/usr/bin/python3
#coding=utf-8
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","990701","akski")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)
