import sys
import json
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

if __name__ == '__main__':
    
	filename = sys.argv[1]
	with open("json/"+filename, 'r') as f:
		all_dates = []
		for line in f:
			tweet = json.loads(line)
			all_dates.append(tweet.get('created_at'))
   
		idx = pd.DatetimeIndex(all_dates)
		ones = np.ones(len(all_dates))
		# the actual series (at series of 1s for the moment)
		my_series = pd.Series(ones, index=idx)

		# Resampling / bucketing into 1-minute buckets
		per_minute = my_series.resample('1min').sum().fillna(0)
		# Plotting the series
		fig, ax = plt.subplots()
		ax.grid(True)
		ax.set_title("Tweet Frequencies")
		hours = mdates.MinuteLocator(interval=20)
		date_formatter = mdates.DateFormatter('%H:%M')

		datemin = datetime(2019, 10, 1, 15, 00)
		datemax = datetime(2019, 10, 1, 15, 30)

		ax.xaxis.set_major_locator(hours)
		ax.xaxis.set_major_formatter(date_formatter)
		ax.set_xlim(datemin, datemax)
		max_freq = per_minute.max()
		ax.set_ylim(0, max_freq)
		ax.plot(per_minute.index, per_minute)

		plt.savefig('graphs/twitter_time_series_analysis.png')
