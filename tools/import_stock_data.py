import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from numpy.fft import fft

stocks = ["TSLA", "LMT", "AAPL", "GOOGL"]
style.use('ggplot')

start = dt.datetime(2011,1,1)
end = dt.datetime.now()

print("Collecting Data from ", start, "to", end)

df = web.DataReader(stocks[2], 'yahoo', start, end)

adj_close = df[["Adj Close", "High", "Low"]]

close_hist = df["Adj Close"]

frequency_plot = fft(close_hist)
x = []
for i in range(0,len(frequency_plot)):
	x.append(i)

der_list = []
day = []
for i in range(1, len(close_hist)):
	day.append(i)
	der_list.append(close_hist[i] - close_hist[i-1])

adj_close.plot()
plt.show()

plt.subplot(1,2,1)
plt.hist(der_list, bins = 100)

plt.subplot(1,2,2)
plt.plot(day, der_list)
plt.show()

plt.plot(x, abs(frequency_plot))
plt.show()
