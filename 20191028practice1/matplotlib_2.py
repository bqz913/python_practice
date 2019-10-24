# インポート
import matplotlib.pyplot as plt
import numpy as np

# 配列作成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x)
y3 = np.cos(x)
y4 = np.linspace(-1, 1, 100)

# オブジェクト指向を使ってみる(こっちのほうが汎用性が高い)
fig1 = plt.figure(1)                    # figure作成　(1)は，figureの番号。(何個もfigureを作成しない場合は指定しなくてもOK)
ax = fig1.add_subplot(111)              # ax作成(fig1の中いっぱいにaxを挿入するという命令("111"は"1,1,1"の略))
ax.plot(x, y1, label='sin(x)')
ax.set_xlabel('x')                      # axのプロパティの場合は.xlabelではなく.set_xlabel
ax.set_ylabel('sin(x)')                 # 同上
ax.set_xticks(np.linspace(0,10,10))     # .xticksも同上
ax.legend()


fig2 = plt.figure(2, figsize=[10, 5])    # figure2個目作成
ax1 = fig2.add_subplot(121)             # subplotを使ってみる。ax1作成
ax1.plot(x, y1, label='sin(x)')
ax1.plot(x, y2, label='2*sin(x)')
ax1.set_ylabel('ax1_ylabel')
ax1.legend()                            # ax1上の凡例を表示
ax2 = fig2.add_subplot(122)             # ax2作成
ax2.plot(x, y3, label='cos(x)')
ax2.plot(x, y4, label='-1 - 1')
ax2.set_ylabel('ax2_ylabel')
fig2.legend()                           # figのlegendを使えばfig上のすべてのプロットの凡例が表示される

plt.show()                              # 表示
