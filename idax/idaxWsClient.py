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

"""idax websocket client"""


class Connect(websocket.WebSocketApp):
    """idax websocket To grant authorization"""

    def auth(self, key, secret):
        self.__key = key
        self.__secret = secret

    """ Get authentication messages"""

    def getAuthMsg(self, data):
        data['key'] = self.__key
        """Parametric ranking conversion aa=11&bb=22...."""
        urlEncodeStr = ""
        for key in sorted(data):
            urlEncodeStr += "&%s=%s" % (key, data[key])
        """Clear the first one in urlEncodeStr &"""
        urlEncodeStr = urlEncodeStr[1:]
        """according to secret sha256 encryption"""
        m = hmac.new(self.__secret.encode('utf-8'), urlEncodeStr.encode('utf-8'), hashlib.sha256)
        """Request parameter object add sign"""
        data['sign'] = m.hexdigest()
        print("send msg:%s\nsign:%s" % (json.dumps(data), m.hexdigest()))
        return json.dumps(data)

    def sendSubXTicker(self, symbol):
        """The symbol value is: trade pairs supported by IDAX (listening is case insensitive, but message push is case)
        :param {'event':'addChannel','channel':'idax_sub_eth_btc_ticker'}

        .. code-block:: python
            {
                "channel":"idax_sub_eth_btc_ticker",
                "data":[{
                  "open":"2466", // The opening price
                  "high":"2555", // The highest price
                  "low":"2466", // The lowest price
                  "last":"2478.51", // The Latest price
                  "timestamp":1411718074965,// The timestamp
                  "vol":"49020.30" // Volume (last 24 hours)
                }]
            }
        """
        channel = idaxConst.WS_X_TICKER % symbol
        self.send(channel)

    def sendSubXDepth(self, symbol):
        """The symbol value is: trade pairs supported by IDAX
        :param {'event':'addChannel','channel':'idax_sub_eth_btc_depth'}

        .. code-block:: python

            // After the first return of the total data (<=200), the first return of the data is performed according to the server data in the following three operations Delete (when the quantity is 0) Modification (same price, different quantity) Increase (price does not exist)
            {
                "channel":"idax_sub_eth_btc_depth",
                "data":[{
                    "bids":[ // bids data of depth
                        ["2473.88","2.025"],
                        ["2473.5","2.4"],
                        ["2470","12.203"]
                    ],
                    "asks":[ // asks data of depth
                        ["2484","17.234"],
                        ["2483.01","6"],
                        ["2482.88","3"]
                    ],
                    "timestamp":1411718972024 // Server timestamp
                }]
            }
        """
        channel = idaxConst.WS_X_DEPTH % symbol
        self.send(channel)

    def sendSubXTrades(self, symbol):
        """The symbol value is: trade pairs supported by IDAX
        :param {'event':'addChannel','channel':'idax_sub_eth_btc_trades'}

        .. code-block:: python

            // [Transaction number, price, volume, Clinch a deal the time, Clinch a deal the type（buy|sell）]
            {
                "channel":"idax_sub_eth_btc_trades",
                "data":[["1001","2463.86","0.052",1411718972024,"buy"]]
            }
        """
        channel = idaxConst.WS_X_TRADES % symbol
        self.send(channel)

    def sendSubXDepthY(self, symbol, number):
        """The symbol value is: trade pairs supported by IDAX (lower case)，The number value is: 5, 10, 20, 50(number of depth bars obtained)
        :param {'event':'addChannel','channel':'idax_sub_eth_btc_depth_20'}

        .. code-block:: python

            {
                "channel":"idax_sub_eth_btc_depth_20",
                "data":[{
                    "bids":[ // bids data of depth
                        ["2473.88","2.025"],
                        ["2473.5","2.4"],
                        ["2470","12.203"]
                    ],
                    "asks":[ // asks data of depth
                        ["2484","17.234"],
                        ["2483.01","6"],
                        ["2482.88","3"]
                    ],
                    "timestamp":1411718972024 // Server timestamp
                }]
            }
        """
        channel = idaxConst.WS_X_DEPTH_Y % (symbol, number)
        self.send(channel)

    def sendSubXKlineY(self, symbol, lineType):
        """The symbol value is: trade pairs supported by IDAX (lower case)，The lineType value is: 1min, 5min, 15min, 30min, 1hour, 2hour, 4hour, 6hour, 12hour, 1day, 1week
        :param {'event':'addChannel','channel':'idax_sub_eth_btc_kline_1min'}

        .. code-block:: python

            {
                "channel":"idax_sub_eth_btc_kline_1min",
                "data":[
                    ["1490337840000","995.37","996.75","995.36","996.75","9.112"],
                    ["1490337840000","995.37","996.75","995.36","996.75","9.112"]
                ]
            }
        """
        channel = idaxConst.WS_X_KLINE_Y % (symbol, lineType)
        self.send(channel)

    def sendSubMyTrade(self):
        """Subscribe to my trading news"""
        data = {"timestamp": int(round(time.time() * 1000))}
        channel = idaxConst.WS_MY_TRADE % self.getAuthMsg(data)
        self.send(channel)

    def sendSubMyOrder(self):
        """Subscribe to my order message"""
        data = {"timestamp": int(round(time.time() * 1000))}
        channel = idaxConst.WS_MY_ORDER % self.getAuthMsg(data)
        self.send(channel)
