import pandas as pd
import numpy as np
import datetime
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

def get_1sec_interval_data(src_df):
    src_df = src_df.reset_index()
    src_df['datetime'] = pd.to_datetime(src_df['datetime'])
    src_df['sec'] = (src_df['datetime'] - src_df['datetime'][0]) / np.timedelta64(1, 's')
    src_df['sec'] = src_df['sec'].map(lambda x: float(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)))

    dst_df = src_df.drop_duplicates(['sec'])
    last_time = int(dst_df['sec'].values[-1])+1
    dst_df = dst_df.set_index(['sec']).reindex(np.arange(last_time), axis='index').drop(['index'], axis=1)
    dst_df = dst_df.reset_index()

    return dst_df

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

if __name__ == "__main__":
    src_file_name = 'sample.csv'
    src_df = pd.read_csv(src_file_name)
    src_df = get_1sec_interval_data(src_df)

    rri = src_df[['sec','rri']].values
    rri_arr = lorenz_plot(rri)

    ## plot
    fig, ax = plt.subplots()
    plt.xlim(0, 1200)
    plt.ylim(0, 1200)
    ax.scatter(rri_arr[0],rri_arr[1])
    ax.set_title('LP')
    ax.set_xlabel('ms')
    ax.set_ylabel('ms')
    plt.show()

    ## calc
    rot_rri_arr = rotate_data(rri_arr, -45)

    mean = rot_rri_arr[0].mean()
    x_std = rot_rri_arr[0].std()
    y_std = rot_rri_arr[1].std()

    print("mean:%.3f x_std:%.3f y_std:%.3f" % (mean, x_std, y_std))
