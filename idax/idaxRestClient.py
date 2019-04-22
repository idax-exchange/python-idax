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

"""idax rest Request client"""


class IdaxRestClient(object):
    API_URL = "https://qa-openapi.idax.mn"

    """Initialization parameter is key,secret"""

    def __init__(self, key, secret):
        self.__key = key
        self.__secret = secret
        self.__timeout = 10

    """get Mode request"""

    def get(self, url, param={}):
        print(self.API_URL + url)
        getResp = requests.get(self.API_URL + url, param, timeout=self.__timeout)
        return getResp.json()

    """post Request for authentication mode"""

    def postAuth(self, url, param={}):
        param['key'] = self.__key
        """Parametric sorting is converted to aa = 11 & bb = 22...."""
        urlEncodeStr = ""
        for key in sorted(param):
            urlEncodeStr += "&%s=%s" % (key, param[key])
        """Clear the first one in urlEncodeStr &;"""
        urlEncodeStr = urlEncodeStr[1:]
        """according to secret sha256 encryption"""
        m = hmac.new(self.__secret.encode('utf-8'), urlEncodeStr.encode('utf-8'), hashlib.sha256)
        """Request parameter object add sign"""
        param['sign'] = m.hexdigest()
        print("url:%s\nurlEncodeStr:%s\nsign:%s" % (self.API_URL + url, urlEncodeStr, m.hexdigest()))
        """Setting HTTP header information"""
        headers = {'Content-Type': "application/json", 'cache-control': "no-cache",}
        """Send a request and receive a response with a request timeout of 10 seconds"""
        postResp = requests.post(self.API_URL + url, json=param, timeout=self.__timeout, headers=headers)
        return postResp.json()

    """Get Server timestamp"""

    def getTime(self):
        """return Server timestamp
        :returns: Object

        .. code-block:: python
            {
                "code":10000,
                "msg":"Successful request processing",
                "timestamp":1536318118202 --server timestamp
            }

        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_TIME)

    """Place Orders"""

    def placeOrder(self, data):
        """return Order Id
        :param key: required apiKey of the user.
        :type key: str
        :returns: Object

        .. code-block:: python
            {
                "code":10000,
                "msg":"Successful request processing",
                "orderId":"2000000000008832432"  //type String  order ID
            }

            {
                "code":10000,
                "msg":"Successful request processing",
                "timestamp":1536318118202 --server timestamp
            }

        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_PLACE_ORDER, data)

    def cancelOrder(self, data):
        """Cancel orders (Support multiple orders per request)
        :returns: Object

        .. code-block:: python
            {
                "code":10000,
                "msg":"Successful request processing",
                "orderId":"2000000000008832432"  //type String  order ID
            }

            {
                "code":10000,
                "msg":"Successful request processing",
                "timestamp":1536318118202 --server timestamp
            }

        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_CANCEL_ORDER, data)

    def orderInfo(self, data):
        """Get Order Info
        :param key: required apiKey of the user.
        :type key: str
        :param pair: required IDAX supports trade pairs.
        :type pair: str
        :param orderId: required if order_id is -1, then return all unfilled orders, otherwise return the order specified.
        :type orderId: str
        :param pageIndex: required current page number
        :type pageIndex: int
        :param pageSize: required number of orders returned per page.
        :type pageSize: int
        :param timestamp: required request timestamp (valid for 3 minutes)
        :type timestamp: long
        :param sign: required signature of request parameters.
        :type sign: str
        :returns: Object

        .. code-block:: python
            {
                "code":10000,
                "msg":"Successful request processing",
                "orders": [
                    {
                        "quantity": "0.1", // order quantity
                        "avgPrice": "0", // average transaction price
                        "timestamp": 1418008467000,// order time
                        "dealQuantity": "0", // filled quantity
                        "orderId": 10000591, // order ID
                        "price": "500", // order price
                        "orderState":1, // 1 = unfilled,2 = partially filled, 9 = fully filled, 19 = cancelled
                        "orderSide":"buy" // buy/sell
                    },
                    {
                        "quantity": "0.2",
                        "avgPrice": "0",
                        "timestamp": 1417417957000,
                        "dealQuantity": "0",
                        "orderId": 10000724,
                        "price": "0.1",
                        "orderState":1,
                        "orderSide":"sell"
                    }],
                    "total": 1
            }

        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_ORDER_INFO, data)

    def orderHis(self, data):
        """Order information within the last 24 hours
        :param key: required apiKey of the user.
        :type key: str
        :param pair: required IDAX supports trade pairs.
        :type pair: str
        :param orderState: required query status: 0 for all orders,query status: 0 for unfilled orders, 1 for filled orders (only the data of the last two days are returned)
        :type orderState: int
        :param currentPage: required current page number
        :type currentPage: int
        :param pageLength: required number of orders returned per page, maximum 100
        :type pageLength: int
        :param timestamp: required request timestamp (valid for 3 minutes)
        :type timestamp: long
        :param sign: required signature of request parameters.
        :type sign: str
        :returns: Object

        .. code-block:: python
            {
                "code":10000,
                "msg":"Successful request processing",
                "currentPage": 1, // current page number
                "orders": // detailed order information
                [
                    {
                        "quantity": "0.2", // order quantity
                        "avgPrice": "0", // average transaction price
                        "timestamp": 1417417957000, // order time
                        "dealQuantity": "0", // filled quantity
                        "orderId": 10000724, // order ID
                        "price": "0.1", // order price
                        "orderState":1, // orderState: 1 = unfilled,2 = partially filled, 9 = fully filled, 19 = cancelled
                        "pair": "ETH_BTC",
                        "orderSide":"buy" // buy/sell
                    }
                ],
                "pageLength": 1, // number of orders per page
                "total": 3 // The total number of records
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_ORDER_HISTORY, data)

    def trades(self, data):
        """The default total does not return one, and returns up to 2000 at a time.
        :param pair: required IDAX supports trade pairs.
        :type pair: str
        :param total: optional Number of items; no default display 1
        :type total: int
        :returns: Object

        .. code-block:: python
            {
                "code": 10000,
                "msg": "Successful request processing",
                "trades": [
                    {
                        "timestamp": 1536322351000, //trade time
                        "price": "0.03428800", //deal price
                        "quantity": "1.19400000", //qty in base coin
                        "id": "6ce36df8-c87a-4517-8a6f-a67affe0481b", //trade id
                        "maker": "Sell" //deal direction Buy/Sell
                    },
                    {
                        "timestamp": 1536322353000,
                        "price": "0.03428800",
                        "quantity": "0.97200000",
                        "id": "a1870119-fdd1-484e-b86b-794554075326",
                        "maker": "Buy"
                    },
                    {
                        "timestamp": 1536322354000,
                        "price": "0.03428700",
                        "quantity": "0.96700000",
                        "id": "c0e752c4-f20c-48ac-8cd9-c65823b1ea01",
                        "maker": "Sell"
                    },
                    //.....
                ]
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_TRADES, data)

    def myTrades(self, data):
        """Get my historical trading information
        :param key: required apiKey of the user.
        :type key: str
        :param pair: optional IDAX supports trade pairs.
        :type pair: str
        :param orderSide: str buy，sell
        :type orderSide: str
        :param currentPage: required current page number
        :type currentPage: int
        :param pageLength: required number of orders returned per page, maximum 100
        :type pageLength: int
        :param startDate: optional start date and timestamp (Millisecond)
        :type startDate: long
        :param endDate: optional end date and timestamp (Millisecond)
        :type endDate: long
        :param timestamp: required request timestamp (valid for 3 minutes)
        :type timestamp: long
        :param sign: required signature of request parameters.
        :type sign: str
        :returns: Object

        .. code-block:: python

            {
                "code":10000,
                "msg":"request success",
                "trades":[{
                    "timestamp": 1367130137,
                    "price": "787.71",    // order price
                    "quantity": "0.003", //order quantity
                    "pair": "ETH_BTC",
                    "maker":"buy"  // buy/sell
                },
                {
                    "timestamp": 1367130137,
                    "price": "787.71",
                    "quantity": "0.003",
                    "pair": "EOS_BTC",
                    "maker":"sell"
                }],
                 "total": 2 // The total number of records
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_MY_TRADES, data)

    def accountInfo(self, data):
        """Get account info
        :param key: required apiKey of the user.
        :type key: str
        :param timestamp: required request timestamp (valid for 3 minutes)
        :type timestamp: long
        :param sign: required signature of request parameters.
        :type sign: str
        :returns: Object

        .. code-block:: python

            {
                "code":10000,
                "msg":"Successful request processing",
                "total": { //total fund
                    "BTC": "0",
                    "ETH": "0",
                    "USDT": "0"
                },
                "free": {  //available fund
                    "BTC": "0",
                    "ETH": "0",
                    "USDT": "0"
                },
                "freezed": { //frozen fund
                    "BTC": "0",
                    "ETH": "0",
                    "USDT": "0"
                }
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.postAuth(idaxConst.REST_USERINFO, data)

    def ticker(self, data):
        """Get the price of specific ticker.
        :param pair: optional IDAX supports trade pairs.
        :type pair: str
        :returns: Object

        .. code-block:: python

            {
                "code":10000,
                "msg":"Successful request processing",
                "timestamp":1536320917805, //server time for returned data
                "ticker":
                [
                    {
                        "pair":"ETH_BTC", //pair
                        "open":"0.03528700", //open price
                        "high":"0.03587400", //high price
                        "low":"0.03389300",//low price
                        "last":"0.03428700",//last price
                        "vol":"18484.75200000"//volume(in the last 24hours sliding window)
                    }
                ]
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_TICKER, data)

    def depth(self, data):
        """Get the market depth for specific market.
        :param pair: required IDAX supports trade pairs. Returns a specific trade against the market when specifying a pair,Returns all trading to market prices without specifying pair;
        :type pair: str
        :param size: optional 	how many price level should be response. must be between 1 - 200
        :type size: int
        :param merge: optional price decimal price should be merged
        :type merge: int
        :returns: Object

        .. code-block:: python

            {
                "code": 10000,
                "msg": "Successful request processing",
                "asks": [ //ask depth
                    [
                        "0.03434400",
                        "0.31100000"
                    ],
                    [
                        "0.03436300",
                        "0.18900000"
                    ],
                    [
                        "0.03436400",
                        "1.01900000"
                    ],
                    [
                        "0.03437100",
                        "0.17200000"
                    ],
                    [
                        "0.03437400", //sell price
                        "0.43400000"  //sell qty
                    ]
                ],
                "bids": [ //bid depth
                    [
                        "0.03427400", //buy price
                        "0.21100000"  //buy qty
                    ],
                    [
                        "0.03427100",
                        "22.05400000"
                    ],
                    [
                        "0.03427000",
                        "0.44700000"
                    ],
                    [
                        "0.03426800",
                        "2.95100000"
                    ],
                    [
                        "0.03426700",
                        "0.94900000"
                    ]
                ]
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_DEPTH, data)

    def kline(self, data):
        """Get kline data
        :param pair: required IDAX supports trade pairs.
        :type pair: str
        :param period: required 1min,5min,15min,30min,1hour,2hour,4hour,6hour,12hour,1day,1week
        :type period: str
        :param size: optional 	specify data size to be acquired
        :type size: int
        :param since: optional timestamp(eg:1417536000000). Data before returning timestamp
        :type since: long
        :returns: Object

        .. code-block:: python
            // approximately 2000 pieces of data are returned each cycle
            {
                "code": 10000,
                "msg": "Successful request processing",
                "kline": [
                    [
                        1536323160000, //timestamp
                        "0.03449400", //open price
                        "0.03449400", //high price
                        "0.03449400", //low price
                        "0.03449400", //close price
                        "0.71900000"  //volume
                    ],
                    [
                        1536323220000,
                        "0.03448500",
                        "0.03448500",
                        "0.03448500",
                        "0.03448500",
                        "1.48500000"
                    ],
                    //...
                ]
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_KLINE, data)

    def pairs(self):
        """All trading pairs supported by exchanges
        :returns: Object

        .. code-block:: python

            {
                "code": 10000,
                "msg": "Successful request processing",
                "pairs": ["DROP_BTC", "VIBE_ETH", "PAT_ETH", "ELEC_ETH", "TRX_USDT", "ANON_ETH", "LTC_BTC", "NER_ETH", "FML_ETH",
                    "C2C_BTC", "MTV_USDT", "AE_ETH", "EOS_BTC", "REN_ETH", "RET_USDT", "LRN_BTC", "MRPH_BTC", "VRS_ETH", "LINDA_BTC",
                    "WT_ETH", "ZAT_BTC", "SDL_ETH", "FTL_ETH", "OCT_BTC", "VEX_BTC", "TPP_BTC", "WIRE_BTC", "SPD_BTC", "GBC_BTC",
                    "STORJ_BTC", "BRN_ETH", "WIRE_USDT", "HERC_ETH", "WT_BTC", ...] //pair name
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_PAIRS)

    def pairLimits(self, data):
        """Gets the maximum, minimum, price, and quantity of the supported transaction pairs.
        :param pair: optional IDAX supports trade pairs.
        :type pair: str
        :returns: Object

        .. code-block:: python

            {
                "code": 10000,
                "msg": "Successful request processing",
                "pairRuleVo": [{
                    "pairName": "ETH_BTC",  //pair
                    "maxAmount": "1000000000000.00000000",  //max amount
                    "minAmount": "0.00100000", //min amount
                    "priceDecimalPlace": 6,  // price decimal
                    "qtyDecimalPlace": 3  //quantity decimal
                }]
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_PAIR_LIMITS, data)

    def getSign(self, data):
        """Developers use getsign to verify that the signature algorithm is correct. The secret is fixed as: otcyACN3wfloCLpAHGcf6jIdHErASs4m7Rbi4ei0QgQRI7TwxhF54hJeV905lnkd.
        :param needSignature: required The string to be signed must be in JSON format
        :type needSignature: str
        :returns: Object

        .. code-block:: python

            {
                "code": 10000,
                "msg": "Successful request processing",
                "sign": "907ab44a485727b604354da47acc6e54e1abeff73defcaa282f38c50b21877ec"
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        return self.get(idaxConst.REST_GET_SIGN, data)
