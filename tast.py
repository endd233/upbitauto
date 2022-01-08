import os
import re
os.chdir(r'C:\Users\brm22\Desktop\Python_world\Upbit') 
import pyupbit
import pprint

f = open("upbit.txt", 'r')
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

upbit.buy_limit_order("KRW-XRP", 200, 100)