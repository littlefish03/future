import os
import sys
import time

path = '/home/code/test/export'

above = 0
below = 0
profit_all = 0
for fname in os.listdir(path):
 with open(path+'/'+fname, 'r') as f:
    profit = 0
    p_start = 0
    p_prev = 0
    a_prev = 0
    count = 0
    count_all = 0

    for line in f:
        data = line.split()
        date = data[0]
        try:
            time.strptime(date, '%m/%d/%Y')
            price = float(data[4])
            amount = float(data[6])
            count_all += 1
            if p_prev == 0:
                p_prev = price
                a_prev = amount
                continue
            if a_prev == 0:
                p_prev = price
                a_prev = amount
                continue
            # buy each time
            ''' 
            if p_start == 0:
                p_start = price
                p_prev = price
                a_prev = amount
                continue
            if p_start > 0:
                #profit += price - p_start
                profit += (price - p_start*1.0003)*10000/p_start
                p_start = 0
                count += 1
            # p increase a increase
            '''
            if p_prev < price and a_prev < amount:
                if p_start == 0:
                    p_start = price
            else:
                if p_start > 0:
                    money = (price - p_start)*10000/p_start
                    # profit += price - p_start
                    profit += money
                    p_start = 0
                    count += 1
            ###
            p_prev = price
            a_prev = amount
        except:
            continue
    if profit > 0:
        above += 1
    else:
        below += 1
    profit_all += profit
    print 'profit %f' % profit
    print 'count all %d, valid %d' % (count_all, count)

print 'above %d, below %d, profit: %f' %(above, below, profit_all)
