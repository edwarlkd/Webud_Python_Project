#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('main_db.db')

# 1. Selection: Login, Sign Up
# 2. 
#
#



with con:
	# set up a cursor to command any execution
	cur = con.cursor()
	query = "INSERT INTO user_info (user_id, user_password) VALUES ( 'howareyou', 'hmmm') "
	cur.execute(query);
	
	
		
		
		
		