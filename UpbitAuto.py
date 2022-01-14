import pyupbit
import time
import datetime
import re
import os
import numpy as np
# os.chdir(r'C:\Users\brm22\Desktop\Python_world\Upbit')
k = 0.5
def max_k():
    ror_1 = 0
    MAK_K = 0.1
    for k in range(1, 10):
        df = pyupbit.get_ohlcv("KRW-BTC", count=5)
        # print(df)
        df['range'] = (df['high'] - df['low']) * k/10
        # print(df['range'])
        df['target'] = df['open'] + df['range'].shift(1)
        # print(df['target'])
        df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
        # print(df['ror'])
        ror = df['ror'].cumprod()[-2]
        # print(ror)
        ror = float(ror)
        if ror > ror_1:
            MAK_K = k/10
            ror_1 = ror

    return MAK_K

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    today = df.iloc[-1]
    yesterday = df.iloc[-2]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * k
    return target



# 객체 생성
# f = open("upbit.txt", 'r')
# lines = f.readlines()
access = 'ElHYnnjMrk30mo4WxbnXmTLLaKimHzZVW5TyAXi7'
secret = 'arWsPFUCtXaAoJNCxkAK1gMNX998wExSGfqRaxlx'
# f.close()
upbit = pyupbit.Upbit(access, secret)

# 변수 설정
op_mode = False
hold = False
target = 0

while True:
    price = pyupbit.get_current_price("KRW-BTC")
    now = datetime.datetime.now()

    # 목표가 갱신 k값 설정
    if now.hour == 9 and now.minute == 0 and 20 < now.second < 30: 
        k = max_k()
        target = cal_target("KRW-BTC")
        time.sleep(10)
        op_mode = True
        print(f"REFRESH! => target price :{target}, k :{k}")

    
    # 매초마다 조건확인후 매수
    if op_mode is True and hold is False and price >= target:
        krw_balance = upbit.get_balance("KRW")
        upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True
        print(f"PURCHASING! => purchase price: {krw_balance}, purchase time: {now}")

    # 매도
    if now.hour == 8 and now.minute == 59 and 0 < now.second < 10:
        if op_mode is True and hold is True:
            btc_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTC", btc_balance)
            hold = False
            print(f"SELLING! => sell price: {btc_balance}")
        op_mode = False
        time.sleep(10)

    print(f"current time: {now} target price: {target} current price: {price} hold: {hold} working: {op_mode} k value: {k}")
    

    time.sleep(1)