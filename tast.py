import os
import re
import pyupbit
import pprint

access = 'ElHYnnjMrk30mo4WxbnXmTLLaKimHzZVW5TyAXi7'
secret = 'arWsPFUCtXaAoJNCxkAK1gMNX998wExSGfqRaxlx'
upbit = pyupbit.Upbit(access, secret)

upbit.buy_limit_order("KRW-XRP", 200, 100)

while True:
    upbit.buy_limit_order("KRW-XRP", 200, 100)