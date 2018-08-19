# by licw
# -*-coding=utf-8-*-
import datetime
import logging
import time

import utils
import db

logging.basicConfig(level=logging.INFO,
                    filename='stock.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
csrc_code = ['01','02','03','04','05','06','07','08','09']

# 从同行业中获取上涨的公司比例
def get_over_code(codes):
    total = 0
    over = 0
    over_code = None
    for code in codes:
        data = utils.get_data_from_sina(code)
        if len(data)<5:
            continue
        if float(data[1]) == 0:
            continue
        total += 1
        price_per = 100*(float(data[3])-float(data[1]))/float(data[1])
        if price_per>0:
            over += 1
            if price_per < 8:
                over_code = code
    over_per = float(over)/total
    print total, over, over_per
    if over_per < 0.5:
        over_code = None
    print over_per, over_code
    return over_per, over_code
    
def get_best_company():
    total = 0
    over = 0
    best_code = None
    best_per = 0
    for zz1 in csrc_code:
        for zz2 in csrc_code:
            codes = db.get_company_by_zzcode(zz1+zz2)
            # if comany count less than 10, skip
            if len(codes) < 10:
                continue
            total += 1
            over_per, over_code = get_over_code(codes)
            if over_per > 0.5:
                over += 1
                if over_per > best_per:
                    best_per = over_per
                    best_code = over_code
    print 'best code', total, over, best_code
    return total, over, best_code

def main():
    logging.debug('main running...')
    # 工作日的9~11，每10分钟运行一次
    curr = datetime.datetime.now()
    if curr.weekday()>4:
        time.sleep(3600)
        return
    if curr.hour > 9 and curr.hour < 11:
        total, over, code = get_best_company()
        logging.info('total %d, over %d, code: %s', total, over, code)
        #超过一半行业收红
        if over*2 > total:
            header = code
            msg = 'all:'+str(total)+' over:'+str(over)+' code:'+code
            mail.sendmail(header, msg)
            logging.info('send mail: %s', msg)
        time.sleep(10*60)

if __name__ == '__main__':
    while True:
        main()
