# 1.
# 下面定义了一个CandleShop类：
#
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        self.stock[color] = self.stock[color] - 1
        try:
            if(self.stock[color]<0):
                raise OutOfStack('当购买{}蜡烛的量超出库存,抛出OutOfStack异常'.format(color))
        except OutOfStack as e:
            print("超出库存：", e)


class OutOfStack(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
candle_shop = CandleShop({'blue': 6, 'red': 1, 'green': 0})
candle_shop.buy('blue')
candle_shop.buy('green')
candle_shop.buy('red')
candle_shop.buy('red')

# 1）自定义一个异常类OutOfStack
# 2）请修改实例buy当购买蜡烛的量超出库存时会抛出OutOfStack异常
# 3）想办法在主程序中加一个代码会引起程序抛出OutOfStack
# 4）捕获该异常，并输出异常的具体信息。
#

