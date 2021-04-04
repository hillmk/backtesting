import backtrader
# Create a Strategy
class TestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order=None
        # self.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        # backtrader.indicators.WeightedMovingAverage(self.datas[0], period=25).subplot = True
        # backtrader.indicators.StochasticSlow(self.datas[0])
        # backtrader.indicators.MACDHisto(self.datas[0])
        # rsi = backtrader.indicators.RSI(self.datas[0])
        # backtrader.indicators.SmoothedMovingAverage(rsi, period=10)
        # backtrader.indicators.ATR(self.datas[0]).plot = False


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED')
            elif order.issell():
                self.log('SELL EXECUTED')
            self.bar_executed = len(self)
        self.order = None
        

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log(' - position: %f' % self.position.size)

        # print(len(self))
        # print(self.order)
        # print(self.position)
        
        # buy the DIP
        if self.order:
            return
        if not self.position:     
            if ((self.dataclose[0] < self.dataclose[-1]) and (self.dataclose[-1] < self.dataclose[-2])):
                    self.log('Buying, %.2f' % self.dataclose[0])
                    self.order = self.buy()
                    # self.order = self.buy(exectype=backtrader.Order.StopTrail, trailpercent=0.02)
                    # self.order = self.buy(exectype=backtrader.Order.StopTrail, trailamount=10)
        else:
            pass
            # if len(self) >= (self.bar_executed + 5):
            #         self.order = self.sell()
