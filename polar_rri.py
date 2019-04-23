import pandas as pd
from pandas.plotting import register_matplotlib_converters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime

class PolarRRI:
    def __init__(self, file_path):
        file_name = os.path.basename(file_path)
        src_df = pd.read_csv(file_name, header=None, sep=' ')
        src_df = src_df.rename(columns={0:'time', 1:'rri'})
        src_df['rri'] = src_df['rri'] * 1000

        file_date, file_time = file_name.split('.')[0].split('_')
        _, yy, MM ,dd = file_date.split('-')
        hh, mm ,ss = file_time.split('-')
        start_datetime = datetime.datetime(int(yy), int(MM), int(dd), int(hh), int(mm), int(ss), 0, tzinfo=None)

        func = lambda x: start_datetime + datetime.timedelta(seconds=x[0])
        src_df['datetime'] = src_df.apply(func, axis=1)
        self.rri_df = src_df.set_index(['datetime'])

    def plot_rri(self):
        register_matplotlib_converters()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
        ax.plot(self.rri_df.index.values, self.rri_df['rri'].values, marker='.')
        plt.show()

    def del_outliers(self, thresh_min, thresh_max):
        self.rri_df['rri'] = self.rri_df['rri'].where(self.rri_df['rri'] < thresh_max)
        self.rri_df['rri'] = self.rri_df['rri'].where(self.rri_df['rri'] > thresh_min)

    def get_rri_df(self):
        return self.rri_df

