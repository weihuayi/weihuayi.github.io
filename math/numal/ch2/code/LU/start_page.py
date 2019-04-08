from __future__ import unicode_literals
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QWidget, QGridLayout


class Text:
    def __init__(self, axes):
        strsets = ["Hi. I'm Computational Mathematics.",
                   'Welcome to new world!',
                   'H', 'a', 'v', 'e', ' ', 'f', 'u', 'n', ' ', 'h', 'e', 'r', 'e', '.']

        offsets = np.zeros((len(strsets), 2)) + 0.5
        offsets[:2, :] = np.array([[.4, -1], [.4, -2]])
        offsets[2:16, :] = np.zeros((14, 2), dtype=float)
        offsets[2:16, 0] += .4 + .55 * np.linspace(0, 1, 14)
        offsets[2:16, 1] += .5

        rotations = np.zeros(len(strsets))

        colors = [tuple(np.random.rand(3)) for i in range(len(strsets))]
        colors[:2] = [(0, .6, 1), (0, .6, 1)]

        alphas = np.zeros(len(strsets), dtype=float)
        alphas[:2] = np.array([1, 1])

        fontsizies = 20 * np.ones(len(strsets), dtype=float)
        fontsizies[:2] = np.array([20, 30])
        fontsizies[2:16] = 50 * np.ones(14)

        self.text = [axes.text(offsets[i, 0], offsets[i, 1], s=strsets[i], rotation=rotations[i],
                               verticalalignment='center', color=colors[i],
                               alpha=alphas[i], fontsize=fontsizies[i]) for i in range(len(strsets))]

    def update_offsets(self, frame_number):
        offsets = np.array([[self.text[i]._x, self.text[i]._y] for i in range(len(self.text))])

        # 251~300 frame
        if 250 < frame_number < 301:
            offsets[0, 1] = 0.55 - 0.9 * (0.55 - offsets[0, 1])
            offsets[1, 1] = 0.45 - 0.9 * (0.45 - offsets[1, 1])
        # 401~450 frame
        elif 400 < frame_number < 451:
            offsets[0, 1] += .01
            offsets[1, 1] -= .01

        for i in range(len(self.text)):
            self.text[i]._x, self.text[i]._y = [offsets[i, 0], offsets[i, 1]]

    def update_alphas(self, frame_number):
        # 401~450 frame
        if 400 < frame_number < 451:
            self.text[0].set_alpha(self.text[0].get_alpha() - 0.02)
            self.text[1].set_alpha(self.text[1].get_alpha() - 0.02)
            for i in range(2, 16):
                self.text[i].set_alpha(self.text[i].get_alpha() + 0.02)
        # 451~460 frame
        elif 450 < frame_number < 461:
            self.text[2].set_alpha(self.text[2].get_alpha() - 0.1)
        # 461~470 frame
        elif 460 < frame_number < 471:
            self.text[2].set_alpha(self.text[2].get_alpha() + 0.1)
            self.text[3].set_alpha(self.text[3].get_alpha() - 0.1)
        # 471~480 frame
        elif 470 < frame_number < 481:
            self.text[3].set_alpha(self.text[3].get_alpha() + 0.1)
            self.text[4].set_alpha(self.text[4].get_alpha() - 0.1)
        # 481~490 frame
        elif 480 < frame_number < 491:
            self.text[4].set_alpha(self.text[4].get_alpha() + 0.1)
            self.text[5].set_alpha(self.text[5].get_alpha() - 0.1)
        # 491~500 frame
        elif 490 < frame_number < 501:
            self.text[5].set_alpha(self.text[5].get_alpha() + 0.1)
            self.text[6].set_alpha(self.text[6].get_alpha() - 0.1)
        # 501~510 frame
        elif 500 < frame_number < 511:
            self.text[6].set_alpha(self.text[6].get_alpha() + 0.1)
            self.text[7].set_alpha(self.text[7].get_alpha() - 0.1)
        # 511~520 frame
        elif 510 < frame_number < 521:
            self.text[7].set_alpha(self.text[7].get_alpha() + 0.1)
            self.text[8].set_alpha(self.text[8].get_alpha() - 0.1)
        # 521~530 frame
        elif 520 < frame_number < 531:
            self.text[8].set_alpha(self.text[8].get_alpha() + 0.1)
            self.text[9].set_alpha(self.text[9].get_alpha() - 0.1)
        # 531~540 frame
        elif 530 < frame_number < 541:
            self.text[9].set_alpha(self.text[9].get_alpha() + 0.1)
            self.text[10].set_alpha(self.text[10].get_alpha() - 0.1)
        # 541~550 frame
        elif 540 < frame_number < 551:
            self.text[10].set_alpha(self.text[10].get_alpha() + 0.1)
            self.text[11].set_alpha(self.text[11].get_alpha() - 0.1)
        # 551~560 frame
        elif 550 < frame_number < 561:
            self.text[11].set_alpha(self.text[11].get_alpha() + 0.1)
            self.text[12].set_alpha(self.text[12].get_alpha() - 0.1)
        # 561~570 frame
        elif 560 < frame_number < 571:
            self.text[12].set_alpha(self.text[12].get_alpha() + 0.1)
            self.text[13].set_alpha(self.text[13].get_alpha() - 0.1)
        # 571~580 frame
        elif 570 < frame_number < 581:
            self.text[13].set_alpha(self.text[13].get_alpha() + 0.1)
            self.text[14].set_alpha(self.text[14].get_alpha() - 0.1)
        # 581~590 frame
        elif 580 < frame_number < 591:
            self.text[14].set_alpha(self.text[14].get_alpha() + 0.1)
            self.text[15].set_alpha(self.text[15].get_alpha() - 0.1)
        # 591~600 frame
        elif 590 < frame_number < 601:
            self.text[15].set_alpha(self.text[15].get_alpha() + 0.1)
        # 601~650 frame
        elif 600 < frame_number < 651:
            for i in range(2, 16):
                self.text[i].set_alpha(self.text[i].get_alpha() - 0.02)

    def update_fontsizes(self, frame_number):
        # 451~460 frame
        if 450 < frame_number < 461:
            self.text[2].set_fontsize(1.1 * self.text[2].get_fontsize())
        # 461~470 frame
        if 460 < frame_number < 471:
            self.text[2].set_fontsize(self.text[2].get_fontsize() / 1.1)
            self.text[3].set_fontsize(1.1 * self.text[3].get_fontsize())
        # 471~480 frame
        elif 470 < frame_number < 481:
            self.text[3].set_fontsize(self.text[3].get_fontsize() / 1.1)
            self.text[4].set_fontsize(1.1 * self.text[4].get_fontsize())
        # 481~490 frame
        elif 480 < frame_number < 491:
            self.text[4].set_fontsize(self.text[4].get_fontsize() / 1.1)
            self.text[5].set_fontsize(1.1 * self.text[5].get_fontsize())
        # 491~500 frame
        elif 490 < frame_number < 501:
            self.text[5].set_fontsize(self.text[5].get_fontsize() / 1.1)
            self.text[6].set_fontsize(1.1 * self.text[6].get_fontsize())
        # 501~510 frame
        elif 500 < frame_number < 511:
            self.text[6].set_fontsize(self.text[6].get_fontsize() / 1.1)
            self.text[7].set_fontsize(1.1 * self.text[7].get_fontsize())
        # 511~520 frame
        elif 510 < frame_number < 521:
            self.text[7].set_fontsize(self.text[7].get_fontsize() / 1.1)
            self.text[8].set_fontsize(1.1 * self.text[8].get_fontsize())
        # 521~530 frame
        elif 520 < frame_number < 531:
            self.text[8].set_fontsize(self.text[8].get_fontsize() / 1.1)
            self.text[9].set_fontsize(1.1 * self.text[9].get_fontsize())
        # 531~540 frame
        elif 530 < frame_number < 541:
            self.text[9].set_fontsize(self.text[9].get_fontsize() / 1.1)
            self.text[10].set_fontsize(1.1 * self.text[10].get_fontsize())
        # 541~550 frame
        elif 540 < frame_number < 551:
            self.text[10].set_fontsize(self.text[10].get_fontsize() / 1.1)
            self.text[11].set_fontsize(1.1 * self.text[11].get_fontsize())
        # 551~560 frame
        elif 550 < frame_number < 561:
            self.text[11].set_fontsize(self.text[11].get_fontsize() / 1.1)
            self.text[12].set_fontsize(1.1 * self.text[12].get_fontsize())
        # 561~570 frame
        elif 560 < frame_number < 571:
            self.text[12].set_fontsize(self.text[12].get_fontsize() / 1.1)
            self.text[13].set_fontsize(1.1 * self.text[13].get_fontsize())
        # 571~580 frame
        elif 570 < frame_number < 581:
            self.text[13].set_fontsize(self.text[13].get_fontsize() / 1.1)
            self.text[14].set_fontsize(1.1 * self.text[14].get_fontsize())
        # 581~590 frame
        elif 580 < frame_number < 591:
            self.text[14].set_fontsize(self.text[14].get_fontsize() / 1.1)
            self.text[15].set_fontsize(1.1 * self.text[15].get_fontsize())
        # 591~600 frame
        elif 590 < frame_number < 601:
            self.text[15].set_fontsize(self.text[15].get_fontsize() / 1.1)


class Scatter:
    def __init__(self, axes):
        x, y = 0.5 * np.ones(5), 0.5 * np.ones(5)
        c = [(0, .75, 1),
             (0, .6, 1),
             (0, 0, 0),
             (0, .75, 1),
             (0, 0, 0)]  # [tuple(np.random.rand(3)) for i in range(len(x))]
        s = [0, 0, 0, 0, 0]  # list(map(lambda var: var * 10000, x))
        self.scatter = axes.scatter(x, y, c=c, alpha=1, edgecolor=None, sizes=s)

    def update_sizes(self, frame_number):
        sizes = self.scatter.get_sizes()

        # 1~50 frame
        if 0 < frame_number < 51:
            sizes[0] += 500
            sizes[1] += 500
            if frame_number > 25:
                sizes[2] += 450
        # 51~100 frame
        elif 50 < frame_number < 101:
            sizes[3] += 225
            if frame_number > 75:
                sizes[4] += 112.5
        # 101~150 frame
        elif 100 < frame_number < 151:
            sizes[0] += 300
            if frame_number > 125:
                pass
        # 151~200 frame
        elif 150 < frame_number < 201:
            if frame_number < 176:
                pass
            sizes[0] += 1500
        # 201~250 frame
        elif 200 < frame_number < 251:
            sizes[4] += sizes[3] / 50
            sizes[0] -= (sizes[0] - sizes[1]) / 30
        # 251~300 frame
        elif 250 < frame_number < 301:
            sizes = list(map(lambda var: 0.98 * var, sizes))
        # 601~650 frame
        elif 600 < frame_number < 651:
            sizes[1] = sizes[1] + 0.1 * (sizes[0] - sizes[1])
            sizes[2] = sizes[2] + 0.1 * (0.9 * sizes[0] - sizes[2])
        else:
            pass

        self.scatter.set_sizes(sizes)

    def update_offsets(self, frame_number):
        offsets = self.scatter.get_offsets()

        # 251~300 frame
        if 250 < frame_number < 301:
            offsets[:, 0] = list(map(lambda var: var - 0.005, offsets[:, 0]))
        # 601~650 frame
        elif 600 < frame_number < 651:
            offsets[:, 0] = list(map(lambda var: var + 0.005, offsets[:, 0]))

        self.scatter.set_offsets(offsets)

    def update_colors(self, frame_number):
        colors = self.scatter.get_facecolors()

        # 601~650 frame
        if 600 < frame_number < 651:
            colors[1, :] = (0.02 * (frame_number - 600), .6 + 0.008 * (frame_number - 600), 1, 1)

        self.scatter.set_facecolors(colors)


class Line:
    def __init__(self, axes):
        x = np.linspace(0, 0.05, 10, endpoint=False)
        x = np.append(x, np.linspace(0.05, 0.1, 40, endpoint=False))
        x = np.append(x, np.linspace(0.1, 0.15, 10, endpoint=False))
        y = np.linspace(0, 0, 10, endpoint=False)
        y = np.append(y, np.linspace(0, 0.95, 40, endpoint=False))
        y = np.append(y, np.linspace(0.95, 1, 10, endpoint=False))
        self.segments = list()
        self.segments.append(np.vstack((0.4325 + 0.15 * x, 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.455 + 0.15 * x[::-1], 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.4775 + 0.15 * x, 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.455 + 0.15 * x[::-1], 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.5 + 0.15 * x[::-1], 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.5225 + 0.15 * x, 0.45 + 0.15 * y)).T)
        self.segments.append(np.vstack((0.545 + 0.15 * x[::-1], 0.45 + 0.15 * y)).T)

        self.line = [axes.plot([], [], c=(0, .6, 1), linewidth=3)[0] for i in range(len(self.segments))]

    def update_segments(self, frame_number):
        # 651~850 frame
        if 650 < frame_number < 851:
            n = (frame_number - 600) // 2
            for i in range(len(self.segments)):
                self.line[i].set_data(self.segments[i][:n, 0], self.segments[i][:n, 1])


class Canvas(FigureCanvasQTAgg):

    def __init__(self, activate_function, parent=None, width=5, height=4, dpi=100):
        self.activate_function = activate_function

        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='black')
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        self.text = Text(self.ax)
        self.scatter = Scatter(self.ax)
        self.line = Line(self.ax)

        self.ani = FuncAnimation(self.fig, self.update_page, interval=10)

        self.connect = False
        self.fig.canvas.mpl_connect('button_press_event', self.button_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self.motion_notify)

        # self.fig.canvas.mpl_connect('button_press_event', self.button_press)

    def update_page(self, frame_number):
        """
        update data of animation
        """
        self.scatter.update_sizes(frame_number=frame_number)
        self.scatter.update_offsets(frame_number=frame_number)
        self.scatter.update_colors(frame_number=frame_number)
        self.text.update_offsets(frame_number=frame_number)
        self.text.update_alphas(frame_number=frame_number)
        self.text.update_fontsizes(frame_number=frame_number)
        self.line.update_segments(frame_number=frame_number)
        if frame_number > 750:
            self.connect = True

    def motion_notify(self, event):
        if self.connect:
            if (event.x - 445) ** 2 + (event.y - 250) ** 2 < 85 ** 2:
                sizes = self.scatter.scatter.get_sizes()
                sizes[0] = 1.25 * sizes[1]
                self.scatter.scatter.set_sizes(sizes)
            else:
                sizes = self.scatter.scatter.get_sizes()
                sizes[0] = sizes[1] / 1.25
                self.scatter.scatter.set_sizes(sizes)

    def button_press(self, event):
        if self.connect and (event.x - 445) ** 2 + (event.y - 250) ** 2 < 85 ** 2:
            self.activate_function()


class StartPage(QWidget):
    def __init__(self, activate_function):
        QWidget.__init__(self)

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.canvas = Canvas(activate_function=activate_function, parent=self)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
