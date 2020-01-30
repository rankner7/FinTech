import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from numpy import fft

style.use('ggplot')

start = dt.datetime(2015,1,1)
end = dt.datetime.now()

print("Collecting Data from ", start, "to", end)

df = web.DataReader("TSLA", 'yahoo', start, end)

adj_close = df[["Adj Close", "High", "Low"]]

print(adj_close.head)

adj_close.plot()
plt.show()
