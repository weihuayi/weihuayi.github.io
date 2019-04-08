from __future__ import unicode_literals
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import collections
from mpl_toolkits.mplot3d import axes3d, art3d
from matplotlib.animation import FuncAnimation


class Text:
    def __init__(self):
        pass


class RainCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(0, 1)
        self.axes.set_xticks([])
        self.axes.set_yticks([])

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        # 创建“雨”的数据结构
        self.n_drops = 50
        self.rain_drops = np.zeros(self.n_drops, dtype=[('position', float, 2),
                                                        ('size', float, 1),
                                                        ('growth', float, 1),
                                                        ('color', float, 4)])

        # 设置“雨”以随机位置落下并且以随机速度增加
        self.rain_drops['position'] = np.random.uniform(0, 1, (self.n_drops, 2))
        self.rain_drops['growth'] = np.random.uniform(50, 200, self.n_drops)

        # 随着“雨”在动画中的播放，更新数据（散点集）
        self.scat = self.axes.scatter(self.rain_drops['position'][:, 0],
                                      self.rain_drops['position'][:, 1],
                                      s=self.rain_drops['size'],
                                      lw=0.5,
                                      edgecolors=self.rain_drops['color'],
                                      facecolors='none')

        # 添加字幕信息
        subtitle_up = ("Welcome",
                       "Making Information:",
                       "Operating Environment:",
                       "Making Tools:",
                       "This application is compiled by:")
        subtitle_down = ("It's will take you a few secounds\n to read my introduction",
                         "Created on Jan 2017\n@author Zheng.Li",
                         "CentOS 7\nPython 3.6",
                         "Eclipse-PyDev\nPyQt5-Without QtDesigner\nCanvas Draw-matpltlib2",
                         "Pure code\nSelf created framework\nSelf created scientific algorithm")
        self.subtitle = (subtitle_up, subtitle_down)
        self.subtitle_up = self.axes.text(0.1, 0.8, s=self.subtitle[0][0],
                                          color="blue", alpha=0, fontsize=25)
        self.subtitle_down = self.axes.text(0.2, 0.4, s=self.subtitle[1][0],
                                            color="blue", alpha=0, fontsize=25)

        self.count = 0
        self.ani = FuncAnimation(self.fig, self.update_scat, interval=10)

        self.fig.canvas.mpl_connect('button_press_event', self.button_press)

    def update_scat(self, frame_number):
        """
        update data of animation
        """
        # 获得一个新的index，并且用来生成旧的“落雨”
        current_index = frame_number % self.n_drops
        # 使得颜色随着时间的推移变淡
        self.rain_drops['color'][:, 3] -= 1.0 / len(self.rain_drops)
        self.rain_drops['color'][:, 3] = np.clip(self.rain_drops['color'][:, 3], 0, 1)
        # 使得半径随着时间的推移变大
        self.rain_drops['size'] += self.rain_drops['growth']
        # 为之前的落雨选择新的出现位置，并且初始化半径、颜色和增长速率
        self.rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
        self.rain_drops['size'][current_index] = 5
        self.rain_drops['color'][current_index] = (0, 0, 0, 1)
        self.rain_drops['growth'][current_index] = np.random.uniform(50, 200)
        # 更新散点集的颜色、半径和位置
        self.scat.set_edgecolors(self.rain_drops['color'])
        self.scat.set_sizes(self.rain_drops['size'])
        self.scat.set_offsets(self.rain_drops['position'])
        # 更新字幕的位置，以100为动画单位是因为前面设定了的FuncAnimation参数interval=10
        x, y = divmod(self.count // 100, 4)
        # 一共五段话，所以这边最后一段话的标识最大只能是4
        if x < 5:
            # 在动画的预设的播放结点上重置每段字幕的位置、透明度
            if self.count // 400 == self.count / 400:
                self.subtitle_up._x = 0.1
                self.subtitle_up._text = self.subtitle[0][x]
                self.subtitle_down._x = 0.2
                self.subtitle_down._text = self.subtitle[1][x]
            # 设置每段字幕的位置、透明度随着时间变化而变化
            if y == 0:
                self.subtitle_up._alpha += 0.01
            elif y == 1:
                self.subtitle_down._alpha += 0.01
            elif y == 3:
                self.subtitle_up._alpha -= 0.01
                self.subtitle_up._x += 0.001
                self.subtitle_down._alpha -= 0.01
                self.subtitle_down._x += 0.001
        else:
            self.subtitle_down._x = 0.45
            self.subtitle_down._y = 0.05
            self.subtitle_down._text = "Press Esc to continue..."
            if y == 1 or y == 3:
                self.subtitle_down._alpha += 0.01
            else:
                self.subtitle_down._alpha -= 0.01
        self.count += 1

    def button_press(self, event):
        """
        change subtitle
        """
        x, y = divmod(self.count // 100, 4)
        if x < 5:
            self.count = 400 * (x + 1)
            self.subtitle_up._alpha = 0
            self.subtitle_down._alpha = 0