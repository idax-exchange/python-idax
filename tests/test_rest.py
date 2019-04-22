#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: test_rest.py
@time: 2019/3/25 18:14
@desc:
"""
import time

from idax.idaxRestClient import IdaxRestClient
import idax.idaxEnums as enums

# Initialize a idaxRestClient
idaxClient = IdaxRestClient("93d6db906e814ab3b0ad5c77aa69ebc2bed4390b1f87444bb040ab775d347858",
                            "13896d803ff644d2a0033580b8f86b5abf10d2c9f2d9454da0541e586b6d77d4")


# Test request server time
def test_get_time():
    resp = idaxClient.getTime()
    print(resp)


# Test Request Place Order
def test_place_order():
    param = {"pair": "ETH_BTC", "amount": 1.05, "orderSide": "buy", "orderType": "limit", "price": 0.034775,
             "timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.placeOrder(param)
    print(resp)


# Test request Cancel Order
def test_cancel_order():
    param = {"orderId": "1671032", "timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.cancelOrder(param)
    print(resp)


# Test Request Order Information
def test_order_info():
    param = {"pair": "ETH_BTC", "orderId": "-1", "pageIndex": 1, "pageSize": 10,
             "timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.orderInfo(param)
    print(resp)


# Test Request History Order
def test_order_his():
    param = {"pair": "ETH_BTC", "orderState": 0, "currentPage": 1, "pageLength": 10,
             "timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.orderHis(param)
    print(resp)


# Test requests for the latest 60 transactions
def test_trades():
    param = {"pair": "ETH_BTC"}
    resp = idaxClient.trades(param)
    print(resp)


# Request for my historical transaction information
def test_my_trades():
    param = {"currentPage": 1, "pageLength": 10, "timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.myTrades(param)
    print(resp)


# Test Request Account Information
def test_account_info():
    param = {"timestamp": int(round(time.time() * 1000))}
    resp = idaxClient.accountInfo(param)
    print(resp)


# Test request to get the price of the transaction pair。
def test_ticker():
    param = {"pair": "ETH_BTC"}
    resp = idaxClient.ticker(param)
    print(resp)


# Test Request Acquisition Market Depth
def test_depth():
    param = {"pair": "ETH_BTC"}
    resp = idaxClient.depth(param)
    print(resp)


# Test Request K-Line Data
def test_kline():
    param = {"pair": "ETH_BTC", "period": enums.Minute}
    resp = idaxClient.kline(param)
    print(resp)


# Test all trading pairs that request exchange support
def test_pairs():
    resp = idaxClient.pairs()
    print(resp)


# Maximum, minimum, price, and number of transaction pairs supported by test requests
def test_pair_limits():
    param = {"pair": "ETH_BTC"}
    resp = idaxClient.pairLimits(param)
    print(resp)


# Test Request Signature
def test_get_sign():
    param = {
        "NeedSignature": '{"key":"93d6db906e814ab3b0ad5c77aa69ebc2bed4390b1f87444bb040ab775d347858","sign":"958da9ec4c890841bc46adc11dc595f6b4666d80c97f36a489ac71b6dc8ccc5e","timestamp":1552531718000}'}
    resp = idaxClient.getSign(param)
    print(resp)
