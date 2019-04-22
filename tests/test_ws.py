#!/usr/bin/env python
# encoding: utf-8
"""
@author: jension
@license: Node Supply Chain Manager Corporation Limited.
@contact: 1490290160@qq.com
@software: garner
@file: test_ws.py
@time: 2019/3/25 18:14
@desc: https://pypi.org/project/websocket-client/ ，
"""
import idax.idaxWsClient as idaxWsClient
import idax.idaxEnums as enums


# successful callback method for websocket connection
def on_open(ws):
    symbol = "ETH_BTC"

    """ Send subscriptions `symbol` Ticker. (sendSubXTicker)"""
    ws.sendSubXTicker(symbol)

    """Send subscriptions `symbol` Depth. (sendSubXDepth)"""
    ws.sendSubXDepth(symbol)

    """ Send subscriptions `symbol` Trades. (sendSubXTrades)"""
    ws.sendSubXTrades(symbol)

    """Send subscriptions `symbol` Depth Count[20]. (sendSubXDepthY)"""
    ws.sendSubXDepthY(symbol, 20)

    """Send subscriptions `symbol` Kline Interval[enums.Minute]. (sendSubXKlineY)"""
    ws.sendSubXKlineY(symbol, enums.Minute)

    """Send a subscription to my order message. (sendSubMyOrder)"""
    ws.sendSubMyOrder()

    """Send a subscription to my trade message. (sendSubMyTrade)"""
    ws.sendSubMyTrade()


# Receiving Message Callback Method for Websocket
def on_message(ws, message):
    print(message)


# Initialize an idax wesocket client
connect = idaxWsClient.Connect("wss://openws.idax.pro/ws", on_message=on_message, on_open=on_open)
connect.auth("93d6db906e814ab3b0ad5c77aa69ebc2bed4390b1f87444bb040ab775d347858d347858",
             "13896d803ff644d2a0033580b8f86b5abf10d2c9f2d9454da0541e586b6d77d4")

connect.run_forever()
