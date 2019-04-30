# lp_proc.py
time series data → lorenz-plot → standard deviation

心拍RRIのローレンツプロット(LP)によってRRIのゆらぎを評価することができると言われています。
lp_proc.pyは、RRIが記録されたTXTファイルを入力に受け、LPを実行するスクリプトです。
sample.pyを実行するとrr-2019-04-23_10-53-52.txtの中身のRRIのLPを散布図で表示したのち、45°傾けて原点からの平均値の距離、x軸方向の標準偏差、y軸方向の標準偏差を計算します。

## Output Image
<div align="center">
<img src="https://raw.githubusercontent.com/nishimura5/lorenz-plot/images/sample.png" width="400">
</div>

## API
### __init__(self, rri_arr, plot_size=3)
#### Parameters:
**rri_arr : array_like**　RRIのデータ、rri_arr[nデータ(X軸)][n+1データ(Y軸)]

**plot_size : int**　プロットの点の大きさ

### calc_ellipse(self)
ローレンツプロットの結果得られる楕円面積と楕円重心の距離を計算
#### Returns:
**ellipse : list**　面積Sと重心距離mean

### set_font(self, font_path)
グラフのタイトルに日本語を使用したい場合等、任意フォントをファイルパスで設定
#### Parameters:

**font_path : str**　フォントファイルのパス(Tips:たいていのフォントファイルは C:\Windows\Fontsフォルダにあります)

### draw_lp_scatter(self, fig_title)
ローレンツプロットの結果グラフを生成(このメソッドを読んだだけでは何も起こりません、write()メソッドでファイル出力してください)
#### Parameters:

**fig_title : str**　グラフのタイトル)

### write(self, file_path)
グラフをファイル出力
#### Parameters:
**file_path : str**　出力ファイル名

# polar_rri.py

rr-2019-04-23_10-53-52.txtのフォーマットは、Polar製V800によって記録されPolarFlowによってエクスポートされたRR間隔データのファイルです。
半角スペースをデリミタとして左側は計測開始時刻を00:00とした受信時刻、右側がRRIとなっています。

## API
### __init__(self, file_path)
ファイルを読み込みRRI[ms]を記録。
#### Parameters:
** file_path : str**　入力ファイルパス。ファイル名はrr-YYYY-MM-DD_hh_mm_ss.txtとなっております。

### plot_rri(self)
時系列グラフを描画


### del_outliers(self, thresh_min, thresh_max)
指定した値を外れ値としてデータから除外
#### Parameters:
** thresh_min : int**　閾値(最小値)

** thresh_max : int**　閾値(最大値)

### get_rri_df(self)
データの取得
#### Returns:
** rri_df : DataFrame**
