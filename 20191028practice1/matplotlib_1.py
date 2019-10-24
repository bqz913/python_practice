# インポート
import matplotlib.pyplot as plt
import numpy as np

# 配列作成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x)

# プロット
# オブジェクト指向を使用しない方法(対話モードならこれで十分)
plt.plot(x, y1, label='sin(x)', color='k')                  # プロット作成
plt.xlabel('x')                                             # x軸ラベル
plt.ylabel('y')                                             # y軸ラベル
plt.yticks([-1,0,1])                                        # y軸目盛り
plt.plot(x, y2, label='2*sin(x)', color=[0.5,1,0.5])        # プロットを重ねてみる(RGBで色の指定も可能)
plt.legend()                                                # 凡例
plt.show()                                                  # グラフ表示
