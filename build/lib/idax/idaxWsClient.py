#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: idaxWsClient.py
@time: 2019/3/26 13:55
@desc:
"""
import time
import websocket
import hashlib
import hmac
import json
import idax.idaxConst as idaxConst

class Connect(websocket.WebSocketApp):
    def auth(self, key, secret):
        self.__key = key
        self.__secret = secret

    def getAuthMsg(self, data):
        data['key'] = self.__key
        urlEncodeStr = ""
        for key in sorted(data):
            urlEncodeStr += "&%s=%s" % (key, data[key])

        urlEncodeStr = urlEncodeStr[1:]
        m = hmac.new(self.__secret.encode('utf-8'), urlEncodeStr.encode('utf-8'), hashlib.sha256)
        data['sign'] = m.hexdigest()
        print("send msg:%s\nsign:%s" % (json.dumps(data), m.hexdigest()))
        return json.dumps(data)

    def sendSubXTicker(self, symbol):
        channel = idaxConst.WS_X_TICKER % symbol
        self.send(channel)

    def sendSubXDepth(self, symbol):
        channel = idaxConst.WS_X_DEPTH % symbol
        self.send(channel)

    def sendSubXTrades(self, symbol):
        channel = idaxConst.WS_X_TRADES % symbol
        self.send(channel)

    def sendSubXDepthY(self, symbol, number):
        channel = idaxConst.WS_X_DEPTH_Y % (symbol, number)
        self.send(channel)

    def sendSubXKlineY(self, symbol, lineType):
        channel = idaxConst.WS_X_KLINE_Y % (symbol, lineType)
        self.send(channel)

    def sendSubMyTrade(self):
        data = {"timestamp": int(round(time.time() * 1000))}
        channel = idaxConst.WS_MY_TRADE % self.getAuthMsg(data)
        self.send(channel)

    def sendSubMyOrder(self):
        data = {"timestamp": int(round(time.time() * 1000))}
        channel = idaxConst.WS_MY_ORDER % self.getAuthMsg(data)
        self.send(channel)
