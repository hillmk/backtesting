# https://github.com/hackingthemarkets/backtrader/tree/master/samples

import backtrader
import datetime
from strategies import TestStrategy
import matplotlib

cerebro = backtrader.Cerebro()
cerebro.broker.set_cash(1000000)
data = backtrader.feeds.YahooFinanceCSVData(
    dataname='orcl.csv',
    fromdate=datetime.datetime(2000,1,1),
    todate=datetime.datetime(2002,12,31),
    reverse=False
)

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.addsizer(backtrader.sizers.FixedSize, stake=1000)

cerebro.run()

print ('Final portfolio value:  %.2f' % cerebro.broker.getvalue())

cerebro.plot()