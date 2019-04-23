import pandas as pd
import numpy as np
import datetime
import math
from decimal import Decimal, ROUND_HALF_UP
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as pat

import polar_rri

from numpy.random import *

def rotate_data(src_data, rot_deg):
    rad = np.radians(rot_deg)
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                  [np.sin(rad), np.cos(rad)]])

    rotated = []
    for i in range(0, len(src_data[0])):
        rotated.append(np.dot(rot, [src_data[0,i], src_data[1,i]]))

    return  np.array(rotated).transpose()

def lorenz_plot(src_arr):
    rri_arr = np.array([src_arr[:-1,1] , src_arr[1:,1]])
    rri_arr_t = rri_arr.transpose()
    rri_arr_t = rri_arr_t[~np.isnan(rri_arr_t).any(axis=1), :]
    rri_arr = rri_arr_t.transpose()
    return rri_arr

def draw_lp_scatter(fig_title, src_arr, mean, x_std, y_std):
    range_ms = 1250
    S = np.pi * x_std * y_std
    text = r"$S=$" +"%d\n"%(S)+ r"$m=$" + "%d"%(mean)
    ellipse = pat.Ellipse(
            xy=(mean/math.sqrt(2),mean/math.sqrt(2)),
            width=x_std*2,
            height=y_std*2,
            alpha=0.9,
            angle=45,
            lw=1,
            ec='black',
            fill=False,
            zorder=3)
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
    ax.scatter(src_arr[0], src_arr[1], s=3, lw=0, c='dimgray', zorder=2)
    ax.add_patch(ellipse)
    ax.text(50, 1000, text)
    ax.set_title(fig_title)
    ax.set_xlabel('$RR_{n}$[ms]')
    ax.set_ylabel('$RR_{n+1}$[ms]')
    ax.set_xticks(np.arange(0,range_ms+1,300))
    ax.set_yticks(np.arange(0,range_ms+1,300))
    plt.subplots_adjust(left=0.23,right=0.93,bottom=0.15,top=0.85)
    plt.savefig('dst.png')
    plt.show()

def gen_test_data():
    data = randn(2, 200)*100 + 500
    return data.astype(int)

if __name__ == "__main__":
    src_file_path = './rr-2019-04-23_10-53-52.txt'

    prri = polar_rri.PolarRRI(src_file_path)
    prri.del_outliers(300, 1200)
    prri.plot_rri()
    rri_df = prri.get_rri_df()


    rri_arr = rri_df[['time','rri']].values
    lp_arr = lorenz_plot(rri_arr)

#    lp_arr = gen_test_data()

    rot_rri_arr = rotate_data(lp_arr, -45)
    mean = rot_rri_arr[0].mean()
    x_std = rot_rri_arr[0].std()
    y_std = rot_rri_arr[1].std()
    draw_lp_scatter('myLP', lp_arr, mean, x_std, y_std)

    print("mean:%.3f x_std:%.3f y_std:%.3f" % (mean, x_std, y_std))
