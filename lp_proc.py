import pandas as pd
import numpy as np
import datetime
import math
from decimal import Decimal, ROUND_HALF_UP
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.patches as pat

from numpy.random import *

class LpProc:
    def __init__(self, rri_arr, plot_size=3):
        rri_arr = np.array([rri_arr[:-1,1] , rri_arr[1:,1]])
        rri_arr_t = rri_arr.transpose()
        rri_arr_t = rri_arr_t[~np.isnan(rri_arr_t).any(axis=1), :]
        rri_arr = rri_arr_t.transpose()
#        self.lp_arr = gen_test_data()
        self.lp_arr = rri_arr
        self.plot_size = plot_size
        self.fp = FontProperties()

    def calc_ellipse(self):
        rot_rri_arr = self.__rotate_data(self.lp_arr, -45)
        self.mean = rot_rri_arr[0].mean()
        x_std = rot_rri_arr[0].std()
        y_std = rot_rri_arr[1].std()
        self.S = np.pi * x_std * y_std

        self.ellipse = pat.Ellipse(
                xy=(self.mean/math.sqrt(2),self.mean/math.sqrt(2)),
                width=x_std*2,
                height=y_std*2,
                alpha=0.9,
                angle=45,
                lw=1,
                ec='black',
                fill=False,
                zorder=3)

        return [self.S, self.mean]

    def set_font(self, font_path):
        self.fp = FontProperties(fname=font_path)

    def draw_lp_scatter(self, fig_title):
        range_ms = 1250
        text = r"$S=$" +"%d\n"%(self.S)+ r"$m=$" + "%d"%(self.mean)
        base_line = np.linspace(0,range_ms,10)

        fig = plt.figure(figsize=(3, 3), dpi=300)
        ax = fig.add_subplot(111)
        plt.tight_layout()
        plt.xlim(0, range_ms)
        plt.ylim(0, range_ms)
        ax.plot(
                base_line,
                base_line,
                color='darkgray',
                linestyle='solid',
                lw=0.6,
                zorder=1)
        ax.scatter(
                self.lp_arr[0],
                self.lp_arr[1],
                s=self.plot_size,
                lw=0,
                c='dimgray',
                zorder=2)
        ax.add_patch(self.ellipse)
        ax.text(50, 1000, text)
        ax.set_title(fig_title, fontproperties=self.fp)
        ax.set_xlabel('$RR_{n}$[ms]')
        ax.set_ylabel('$RR_{n+1}$[ms]')
        ax.set_xticks(np.arange(0,range_ms+1,300))
        ax.set_yticks(np.arange(0,range_ms+1,300))
        plt.subplots_adjust(left=0.23,right=0.93,bottom=0.15,top=0.85)

    def write(self, file_path):
        plt.savefig(file_path)
        plt.close()

    def __rotate_data(self, src_data, rot_deg):
        rad = np.radians(rot_deg)
        rot = np.array([[np.cos(rad), -np.sin(rad)],
                      [np.sin(rad), np.cos(rad)]])
        rotated = []
        for i in range(0, len(src_data[0])):
            rotated.append(np.dot(rot, [src_data[0,i], src_data[1,i]]))
        return  np.array(rotated).transpose()

def gen_test_data():
    data = randn(2, 200)*100 + 500
    return data.astype(int)

