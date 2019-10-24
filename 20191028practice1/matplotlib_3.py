# インポート
import matplotlib.pyplot as plt
import numpy as np

# 配列作成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x)
y3 = np.cos(x)
y4 = np.linspace(-1, 1, 100)

# グラフ描画def
def superplotmachine(x, y, fig):
    ax = fig.add_subplot(111)
    ax.plot(x,y)

# 色々やってみる
fig1 = plt.figure(1)
fig2 = plt.figure(2)
fig3 = plt.figure(3)
superplotmachine(x, y1, fig1)
superplotmachine(x, y1, fig2)
superplotmachine(x, y1, fig3)
superplotmachine(x, y2, fig3)
superplotmachine(x, y3, fig1)