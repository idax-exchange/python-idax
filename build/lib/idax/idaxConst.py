#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: idaxConst.py
@time: 2019/3/26 15:10
@desc:
"""

"""
idax rest api path
"""
REST_TIME = "/api/v2/time"
REST_PLACE_ORDER = "/api/v2/placeOrder"
REST_CANCEL_ORDER = "/api/v2/cancelOrder"
REST_ORDER_INFO = "/api/v2/orderInfo"
REST_ORDER_HISTORY = "/api/v2/orderHistory"
REST_TRADES = "/api/v2/trades"
REST_MY_TRADES = "/api/v2/myTrades"
REST_USERINFO = "/api/v2/userinfo"
REST_TICKER = "/api/v2/ticker"
REST_DEPTH = "/api/v2/depth"
REST_KLINE = "/api/v2/kline"
REST_PAIRS = "/api/v2/pairs"
REST_PAIR_LIMITS = "/api/v2/pairLimits"
REST_GET_SIGN = "/api/v2/GetSign"

"""
idax ws api channel
"""
WS_X_TICKER = '{"event": "addChannel", "channel": "idax_sub_%s_ticker"}'
WS_X_DEPTH = '{"event": "addChannel", "channel": "idax_sub_%s_depth"}'
WS_X_DEPTH_Y = '{"event": "addChannel", "channel": "idax_sub_%s_depth_%s"}'
WS_X_TRADES = '{"event": "addChannel", "channel": "idax_sub_%s_trades"}'
WS_X_KLINE_Y = '{"event": "addChannel", "channel": "idax_sub_%s_kline_%s"}'
WS_MY_TRADE = '{"event": "addChannel", "channel": "idax_sub_mytrade", "parameters": %s}'
WS_MY_ORDER = '{"event": "addChannel", "channel": "idax_sub_myorder", "parameters": %s}'
