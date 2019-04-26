# -*- coding: utf-8 -*-
import polar_rri
import lp_proc

if __name__ == "__main__":
    src_file_path = './rr-2019-04-23_10-53-52.txt'

    prri = polar_rri.PolarRRI(src_file_path)
    prri.del_outliers(300, 1200)
    prri.plot_rri()
    rri_df = prri.get_rri_df()

    rri_arr = rri_df[['time','rri']].values

    lp = lp_proc.LpProc(rri_arr)
    S, mean = lp.calc_ellipse()
    lp.set_font('C:/Windows/Fonts/meiryo.ttc')
    lp.draw_lp_scatter('サンプル')
    lp.write('dst.png')

    print("mean:%.3f S:%.1f" % (mean, S))
