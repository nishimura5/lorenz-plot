# lorenz-plot
time series data → lorenz-plot → standard deviation

心拍RRIのローレンツプロット(LP)によってRRIのゆらぎを評価することができると言われています。
lp_proc.pyは、RRIが記録されたTXTファイルを入力に受け、LPを実行するスクリプトです。
lp_proc.pyを実行するとrr-2019-04-23_10-53-52.txtの中身のRRIのLPを散布図で表示したのち、45°傾けて原点からの平均値の距離、x軸方向の標準偏差、y軸方向の標準偏差を計算します。

TXTファイルのフォーマットはPolar製V800によって記録され、PolarFlowによってエクスポートされたRR間隔データのファイルです。

## Output Image
<img src="https://raw.githubusercontent.com/nishimura5/lorenz-plot/images/sample.png" width="400">

## API
### __init__(self, x_arr, y_arr, plot_size=3)
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

