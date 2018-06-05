#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('main_db.db')


with con:
	# set up a cursor to command any execution
    cur = con.cursor()    
	cur.execute("INSERT INTO user_info VALUES('', 'howareyou', 'hmmm')")
	
	
		
		
		
		