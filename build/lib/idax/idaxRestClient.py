#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: idaxRestClient.py
@time: 2019/3/25 17:42
@desc:
"""
import requests
import hashlib
import hmac

import idax.idaxConst as idaxConst


class IdaxRestClient(object):
    API_URL = "https://qa-openapi.idax.mn"

    def __init__(self, key, secret):
        self.__key = key
        self.__secret = secret
        self.__timeout = 10

    def get(self, url, param={}):
        print(self.API_URL + url)
        getResp = requests.get(self.API_URL + url, param, timeout=self.__timeout)
        return getResp.json()

    def postAuth(self, url, param={}):
        param['key'] = self.__key

        urlEncodeStr = ""
        for key in sorted(param):
            urlEncodeStr += "&%s=%s" % (key, param[key])

        urlEncodeStr = urlEncodeStr[1:]
        m = hmac.new(self.__secret.encode('utf-8'), urlEncodeStr.encode('utf-8'), hashlib.sha256)
        param['sign'] = m.hexdigest()
        print("url:%s\nurlEncodeStr:%s\nsign:%s" % (self.API_URL + url, urlEncodeStr, m.hexdigest()))

        headers = {'Content-Type': "application/json", 'cache-control': "no-cache",}
        postResp = requests.post(self.API_URL + url, json=param, timeout=self.__timeout, headers=headers)
        return postResp.json()

    def getTime(self):
        return self.get(idaxConst.REST_TIME)

    def placeOrder(self, data):
        return self.postAuth(idaxConst.REST_PLACE_ORDER, data)

    def cancelOrder(self, data):
        return self.postAuth(idaxConst.REST_CANCEL_ORDER, data)

    def orderInfo(self, data):
        return self.postAuth(idaxConst.REST_ORDER_INFO, data)

    def orderHis(self, data):
        return self.postAuth(idaxConst.REST_ORDER_HISTORY, data)

    def trades(self, data):
        return self.get(idaxConst.REST_TRADES, data)

    def myTrades(self,data):
        return self.postAuth(idaxConst.REST_MY_TRADES,data)

    def accountInfo(self,data):
        return self.postAuth(idaxConst.REST_USERINFO,data)

    def ticker(self,data):
        return self.get(idaxConst.REST_TICKER,data)

    def depth(self,data):
        return self.get(idaxConst.REST_DEPTH,data)

    def kline(self,data):
        return self.get(idaxConst.REST_KLINE,data)

    def pairs(self):
        return self.get(idaxConst.REST_PAIRS)

    def pairLimits(self,data):
        return self.get(idaxConst.REST_PAIR_LIMITS,data)

    def getSign(self,data):
        return self.get(idaxConst.REST_GET_SIGN,data)
