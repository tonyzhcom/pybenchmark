#coding:utf-8
import time
from tornado.httpclient import AsyncHTTPClient
from tornado import ioloop
import functools
import math

class BM:
    def __init__(self,url,c=1,n=1):
        self.c=c
        self.n=n
        self.url=url
        self.pos=0
        self.data=[]
        self.start_at=time.time()
        
        self.go()
    def start_one(self):
        self.pos += 1
        AsyncHTTPClient().fetch(self.url,functools.partial(self.handle,time.time()))
        
    def go(self):
        for i in range(min(self.c,self.n)):
            self.start_one()
        ioloop.IOLoop.instance().start()
    def handle(self,start_at,response):
        self.data.append(time.time()-start_at)
        if self.pos < self.n:
            self.start_one()
        else :
            self.end_at=time.time()
            ioloop.IOLoop.instance().stop()
            self.printStat()
    def printStat(self):
        print '并发数',self.c,'总数',self.n,'任务',self.url
        print '开始时间',self.start_at,'结束时间',self.end_at,'耗时',self.end_at-self.start_at
        print '响应耗时 最大',max(self.data),'最小',max(self.data),'平均',max(self.data)
        print '平均QPS',math.ceil(len(self.data)/(self.end_at-self.start_at))
if __name__ =='__main__':
    BM('http://www.soso.com/',c=100,n=1000)
    
