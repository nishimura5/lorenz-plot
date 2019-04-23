# lorenz-plot
time series data → lorenz-plot → standard deviation

心拍RRIのローレンツプロット(LP)によってRRIのゆらぎを評価することができると言われています。
lp_proc.pyは、RRIが記録されたTXTファイルを入力に受け、LPを実行するスクリプトです。
lp_proc.pyを実行するとrr-2019-04-23_10-53-52.txtの中身のRRIのLPを散布図で表示したのち、45°傾けて原点からの平均値の距離、x軸方向の標準偏差、y軸方向の標準偏差を計算します。

TXTファイルのフォーマットはPolar製V800によって記録され、PolarFlowによってエクスポートされたRR間隔データのファイルです。
