import json

import redis
import pymysql


def process_item():
    num = 0
    while True:
        rediscli = redis.Redis(host="127.0.0.1",port=6379,db=0)
        # db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='xxxxx',
        #                      charset='utf8')
        source,data = rediscli.blpop("jobbole:items")
        item = json.loads(data)
        print(item['title'])
        print(item['lead'])
        num+=1
        print(num)


if __name__ == '__main__':
    process_item()