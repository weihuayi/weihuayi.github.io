#!/usr/bin/python

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import qApp, QAction, QToolTip, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox 
from PyQt5.QtWidgets import QDesktopWidget


class AlgDemoApp(QMainWindow):
    """
    MainWindow
    """

    # noinspection PyArgumentList,PyMissingConstructor
    def __init__(self):
        # noinspection PyCompatibility
        QMainWindow.__init__(self)

        self.window_setting()

        self.central_widget_dir = {}

        self.central_widget_setting()
        self.setCentralWidget(self.central_widget_dir['start'])

        self.statusBar().showMessage('Ready')

        self.show()

    def window_setting(self):
        """
        setting size, position, icon, title and something else of main window.
        """
        # noinspection PyCallByClass,PyTypeChecker
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(100, 100, 900, 550)
        self.frameGeometry().moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(self.frameGeometry().topLeft())
        self.setWindowTitle('Algorithm Demo App')
        self.setWindowIcon(QIcon('./icons/python.png'))
        # Set the MainWindows always on the front of Desktop
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint) #  TODO: invisible frame of main window

    def central_widget_setting(self):
        import lu_page
        self.central_widget_dir['GEPP'] = lu_page.LuAlgorithmPage()

        import start_page

        def start():
            self.setCentralWidget(self.central_widget_dir['GEPP'])
            self.action = {}
            self.action_setting()
            self.menubar_setting()

        self.central_widget_dir['start'] = start_page.StartPage(activate_function=start)

    def action_setting(self):
        """
        set MainData.action
        """

        self.action["show_open_dialog"] = QAction('Open File', self)
        self.action["show_open_dialog"].setIcon(QIcon('./icons/open.png'))
        self.action["show_open_dialog"].setShortcut('Ctrl+O')
        self.action["show_open_dialog"].setStatusTip('Open File')
        self.action["show_open_dialog"].triggered.connect(self.show_open_dialog)

        self.action["qApp_quit"] = QAction('Exit application', self)
        self.action["qApp_quit"].setIcon(QIcon('./icons/exit.jpg'))
        self.action["qApp_quit"].setShortcut('Ctrl+Q')
        self.action["qApp_quit"].setStatusTip('Exit application')
        self.action["qApp_quit"].triggered.connect(qApp.quit)
        
        def swith_GEPP():
            self.setCentralWidget(self.central_widget_dir['GEPP'])
        self.action["GEPP"] = QAction('GEPP', self)
        self.action["GEPP"].setIcon(QIcon('./icons/numpy.jpg'))
        self.action["GEPP"].setShortcut('Ctrl+L')
        self.action["GEPP"].setStatusTip('GEPP')
        self.action["GEPP"].triggered.connect(swith_GEPP)

    def menubar_setting(self):
        """
        set MainWindow.menuBar
        """
        self.statusBar()

        file_menu = self.menuBar().addMenu('&File')
        file_menu.addAction(self.action["show_open_dialog"])
        file_menu.addAction(self.action["qApp_quit"])

        linear_equation_solving_menu = self.menuBar().addMenu('&Linear Equation Solving')
        linear_equation_solving_menu.addAction(self.action["GEPP"])

    def keyPressEvent(self, event):
        """
        :param event:
        :return:
        """
        # if event.key() == Qt.Key_Escape:
        #     try:
        #         if self.currentImage == "rainImage":
        #             self.orthogonalTableImage()
        #         elif self.currentImage == "orthogonalTableImage":
        #             pass
        #         elif self.currentImage == "convexHullImage":
        #             pass
        #         elif self.currentImage == "gravitationalSystemImage":
        #             self.gravitationalSystemImage()
        #         elif self.currentImage == "triangularPolynomialImage":
        #             pass
        #     except KeyError:
        #         self.startImage()
        #     self.statusBar().showMessage('Esc is pressed!')
        pass  # TODO: press esc to escape from canvas.

    def show_open_dialog(self):
        """
        @
        """
        # noinspection PyCallByClass,SpellCheckingInspection
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

    def buttonClicked(self):  # TODO: What the hell? I can't remember this!
        """
        @
        """
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        # noinspection PyCallByClass,PyTypeChecker
        QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

    def closeEvent(self, event):
        """
        @
        """
        # noinspection PyCallByClass,PyTypeChecker
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
