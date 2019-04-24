================================
Welcome to python-idax v2
================================

pypi：v0.7.1

license：MIT

build：passing

coverage：58%

wheel：no

python：2.7|3.4|3.5|3.6

brief
--------
This is an unofficial Python wrapper for the `IDAX exchange REST API v2 <https://github.com/idax-exchange/idax-official-api-docs>`_. I am in no way affiliated with IDAX, use at your own risk.

If you came here looking for the `IDAX exchange <https://www.idax.global/#/exchangepro?pairname=ETH_BTC>`_ to purchase cryptocurrencies, then `go here <https://www.idax.global>`_. If you want to automate interactions with IDAX stick around.

Source code
  Not on-line to be supplemented

Documentation
  https://github.com/idax-exchange/idax-official-api-docs

Features
--------

- Implementation of all General, Market Data and Account endpoints.
- Simple handling of authentication
- No need to generate sign yourself, the wrapper does it for you
- Response exception handling
- Websocket handling with reconnection and multiplexed connections
- Symbol Depth Cache
- Historical Kline/Candle fetching function

Quick Start
-----------

`Register an account with <https://www.idax.global>`_

`Generate an API Key and assign relevant permissions  <https://www.idax.global>`_


.. code:: bash

    pip install python-idax

- REST case

.. code:: python

    from idax.idaxRestClient import IdaxRestClient

    # Test order
    def test_place_order():
        # Initialize a idaxRestClient
        idaxClient = IdaxRestClient("key","secret")

        # The following single request parameter.
        param = {"pair": "ETH_BTC", "amount": 1.05, "orderSide": "buy", "orderType": "limit", "price": 0.034775,
                 "timestamp": int(round(time.time() * 1000))}
        # Request for order
        resp = idaxClient.placeOrder(param)
        # Print the order result
        print(resp)


    # Test cancel order
    def test_cancel_order():
        param = {"orderId": "[orderId]", "timestamp": int(round(time.time() * 1000))}
        resp = idaxClient.cancelOrder(param)
        print(resp)


For more check out the documentation https://github.com/idax-exchange/idax-official-api-docs/blob/master/open-api_en.md.

- Websocket case

.. code:: python

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
    connect = idaxWsClient.Connect("url", on_message=on_message, on_open=on_open)
    connect.auth("key",
                 "secret")

    connect.run_forever()


For more check out the documentation https://github.com/idax-exchange/idax-official-api-docs/blob/master/open-ws_en.md.
