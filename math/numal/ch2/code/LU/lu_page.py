import numpy as np
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class LuAlgorithm:

    @staticmethod
    def lu_0(A, loop):
        n = len(A)
        P, L, U = np.eye(n), np.zeros((n, n)), np.zeros((n, n))
        A_indexes, P_indexes, L_indexes, U_indexes = np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int)

        if loop == n - 1:
            forward_step = loop
        else:
            forward_step = loop + 1

        for i in range(forward_step):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    # exchange rows
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]
                    L[[i, m], :] = L[[m, i], :]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        A_indexes[[i, m], :] += 1
                        P_indexes[[i, m], :] += 1
                        L_indexes[[i, m], :i] += 1

                for j in range(i + 1, n):
                    # update L
                    L[j, i] = A[j, i] / A[i, i]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        L_indexes[j, i] += 1

                for j in range(i, n):
                    # update U
                    U[i, j] = A[i, j]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        U_indexes[i, j] += 1

                for j in range(i + 1, n):
                    for k in range(i + 1, n):
                        # update A
                        A[j, k] -= L[j, i] * U[i, k]
                        if i == forward_step - 1:
                            # mark the indexes of the elements changed
                            A_indexes[j, k] += 1

        if loop == n - 1:
            # update P, L, U
            P = P.T
            L += np.eye(n)
            U[-1, -1] = A[-1, -1]
            # mark the indexes of the elements changed
            A_indexes *= 0
            P_indexes *= 0
            P_indexes += 1
            L_indexes *= 0
            for i in range(n):
                L_indexes[i, i] += 1
            U_indexes *= 0
            U_indexes[-1, -1] += 1

        A_indexes, P_indexes, L_indexes, U_indexes = np.abs(A_indexes), np.abs(P_indexes), np.abs(L_indexes), np.abs(U_indexes)
        return A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes

    @staticmethod
    def lu_1(A, loop):
        n = len(A)
        P = np.eye(n)
        A_indexes, P_indexes, L_indexes, U_indexes = np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int)

        if loop == n - 1:
            forward_step = loop
        else:
            forward_step = loop + 1

        for i in range(forward_step):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    # exchange rows
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        A_indexes[[i, m], :] += 1
                        P_indexes[[i, m], :] += 1

                for j in range(i + 1, n):
                    # update A
                    A[j, i] = A[j, i] / A[i, i]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        A_indexes[j,  i] += 1

                for j in range(i + 1, n):
                    for k in range(i + 1, n):
                        # update A
                        A[j, k] -= A[j, i] * A[i, k]
                        if i == forward_step - 1:
                            # mark the indexes of the elements changed
                            A_indexes[j, k] += 1

        if loop == n - 1:
            # update P, L, U
            P = P.T
            L = np.tril(A, -1) + np.eye(n)
            U = np.triu(A, 0)
            # mark the indexes of the elements changed
            A_indexes *= 0
            P_indexes *= 0
            P_indexes += 1
            for i in range(1, n):
                L_indexes[i, :i] += 1
            for i in range(n):
                U_indexes[i, i:] += 1
        else:
            L = np.eye(n)
            U = np.zeros((n, n))

        A_indexes, P_indexes, L_indexes, U_indexes = np.abs(A_indexes), np.abs(P_indexes), np.abs(L_indexes), np.abs(U_indexes)
        return A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes

    @staticmethod
    def lu_2(A, loop):
        n = len(A)
        P = np.eye(n)
        A_indexes, P_indexes, L_indexes, U_indexes = np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int), np.zeros((n, n), dtype=int)

        if loop == n - 1:
            forward_step = loop
        else:
            forward_step = loop + 1

        for i in range(forward_step):

            m = np.argmax(np.abs(A[i:, i])) + i

            if A[m, i] == 0:
                raise ValueError("matrix is singular.")
            else:
                if m != i:
                    # exchange rows
                    A[[i, m], :] = A[[m, i], :]
                    P[[i, m], :] = P[[m, i], :]
                    if i == forward_step - 1:
                        # mark the indexes of the elements changed
                        A_indexes[[i, m], :] += 1
                        P_indexes[[i, m], :] += 1

                # update A
                A[(i + 1):, i] = A[(i + 1):, i] / A[i, i]
                A[(i + 1):, (i + 1):] -= A[(i + 1):, i][:, None] * A[i, (i + 1):]
                if i == forward_step - 1:
                    # mark the indexes of the elements changed
                    A_indexes[(i + 1):, i:] += 1

        if loop == n - 1:
            # update P, L, U
            P = P.T
            L = np.tril(A, -1) + np.eye(n)
            U = np.triu(A, 0)
            # mark the indexes of the elements changed
            A_indexes *= 0
            P_indexes *= 0
            P_indexes += 1
            for i in range(1, n):
                L_indexes[i, :i] += 1
            for i in range(n):
                U_indexes[i, i:] += 1
        else:
            L = np.eye(n)
            U = np.zeros((n, n))

        A_indexes, P_indexes, L_indexes, U_indexes = np.abs(A_indexes), np.abs(P_indexes), np.abs(L_indexes), np.abs(U_indexes)
        return A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes


class LuAlgorithmPage(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # layout
        self.layout = QGridLayout()
        self.layout.setSpacing(10)

        self.widget, self.label = [], []
        self.combobox, self.radiobutton, self.pushbutton, self.tablewidget, self.tabwidget = [], [], [], [], []

        self.decimal_digits = '%.3f'

        self.widget_setting()

        self.table_write(dim=int(self.combobox[0].currentText()), table=self.tablewidget[0], matrix=np.array([[4, 2, 1, 5], [8, 7, 2, 10], [4, 8, 3, 6], [6, 8, 4, 9]], dtype=float))

        self.widget_connet()

    def widget_setting(self):

        # label 0 := matrix size
        self.label.append(QLabel('matrix size'))
        self.label[0].setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label[0], 0, 0, 1, 1)

        # combobox 0 := matrix size
        self.combobox.append(QComboBox())
        self.combobox[0].addItems(list(map(str, range(3, 10))))
        self.combobox[0].setCurrentIndex(1)
        self.layout.addWidget(self.combobox[0], 0, 1, 1, 1)

        # label 1 := loop
        self.label.append(QLabel('loop'))
        self.label[1].setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label[1], 1, 0, 1, 1)

        # combobox 1 := loop
        self.combobox.append(QComboBox())
        self.combobox[1].addItems(list(map(str, range(int(self.combobox[0].currentText())))))
        self.combobox[1].setCurrentIndex(int(self.combobox[0].currentText()) - 1)
        self.layout.addWidget(self.combobox[1], 1, 1, 1, 1)

        # radiobutton 0 := matrix create
        self.radiobutton.append(QRadioButton('user-defined'))
        self.radiobutton[0].setChecked(True)
        self.layout.addWidget(self.radiobutton[0], 2, 0, 1, 1)

        # radiobutton 1 := matrix create
        self.radiobutton.append(QRadioButton('random matrix'))
        self.radiobutton[1].setChecked(False)
        self.layout.addWidget(self.radiobutton[1], 2, 1, 1, 1)

        # tablewidget 0 := analysis of lu algorithm
        self.tablewidget.append(QTableWidget(int(self.combobox[0].currentText()), int(self.combobox[0].currentText())))
        self.tablewidget[-1].setHorizontalHeaderLabels(list(map(str, range(int(self.combobox[0].currentText())))))
        self.tablewidget[-1].setVerticalHeaderLabels(list(map(str, range(int(self.combobox[0].currentText())))))
        self.tablewidget[-1].resizeColumnsToContents()
        self.layout.addWidget(self.tablewidget[0], 4, 0, 4, 2)

        # tabwidget 0
        class WidgetInner(QTabWidget):
            def __init__(self, dim):
                QTabWidget.__init__(self)

                self.layout, self.widget, self.tablewidget = [], [], []
                self.color = np.random.randint(100, 200, 3)

                for i in range(3):
                    # layout i
                    self.layout.append(QGridLayout())
                    self.layout[i].setSpacing(10)
                    # tablewidget := origin matrix A_0 in lu_0
                    self.tablewidget.append(QTableWidget(dim, dim))
                    self.tablewidget[-1].setHorizontalHeaderLabels(list(map(str, range(dim))))
                    self.tablewidget[-1].setVerticalHeaderLabels(list(map(str, range(dim))))
                    self.layout[i].addWidget(self.tablewidget[-1], 0, 0, 1, 1)
                    # tablewidget := origin matrix P in lu_0
                    self.tablewidget.append(QTableWidget(dim, dim))
                    self.tablewidget[-1].setHorizontalHeaderLabels(list(map(str, range(dim))))
                    self.tablewidget[-1].setVerticalHeaderLabels(list(map(str, range(dim))))
                    self.layout[i].addWidget(self.tablewidget[-1], 0, 1, 1, 1)
                    # tablewidget := origin matrix L in lu_0
                    self.tablewidget.append(QTableWidget(dim, dim))
                    self.tablewidget[-1].setHorizontalHeaderLabels(list(map(str, range(dim))))
                    self.tablewidget[-1].setVerticalHeaderLabels(list(map(str, range(dim))))
                    self.layout[i].addWidget(self.tablewidget[-1], 1, 0, 1, 1)
                    # tablewidget := origin matrix U in lu_0
                    self.tablewidget.append(QTableWidget(dim, dim))
                    self.tablewidget[-1].setHorizontalHeaderLabels(list(map(str, range(dim))))
                    self.tablewidget[-1].setVerticalHeaderLabels(list(map(str, range(dim))))
                    self.layout[i].addWidget(self.tablewidget[-1], 1, 1, 1, 1)
                    # widget 0
                    self.widget.append(QWidget())
                    self.widget[i].setLayout(self.layout[i])

                self.addTab(self.widget[0], '&Algorithm_2_2')
                self.addTab(self.widget[1], '&Algorithm_2_3')
                self.addTab(self.widget[2], '&Algorithm_2_4')
        self.tabwidget.append(WidgetInner(dim=int(self.combobox[0].currentText())))
        self.layout.addWidget(self.tabwidget[0], 0, 2, 8, 5)

        self.setLayout(self.layout)

    def widget_connet(self):
        # change matrix size
        self.combobox[0].currentIndexChanged.connect(self.function_combobox_0)
        # change step
        self.combobox[1].currentIndexChanged.connect(self.function_combobox_1)
        # change origin matrix by user-defined
        self.radiobutton[0].clicked.connect(self.function_radiobutton_0)
        # change origin matrix by random it
        self.radiobutton[1].clicked.connect(self.function_radiobutton_0)
        # # show us the information of LU algorithm TODO: undefined action of pushbutton
        # self.pushbutton[0].clicked.connect(self.function_4)
        # change origin matrix
        self.tablewidget[0].itemChanged.connect(self.matrix_calulate)

    def widget_disconnet(self):
        # change matrix size
        self.combobox[0].currentIndexChanged.disconnect(self.function_combobox_0)
        # change step
        self.combobox[1].currentIndexChanged.disconnect(self.function_combobox_1)
        # change origin matrix by user-defined
        self.radiobutton[0].clicked.disconnect(self.function_radiobutton_0)
        # change origin matrix by random it
        self.radiobutton[1].clicked.disconnect(self.function_radiobutton_0)
        # # show us the information of LU algorithm TODO: undefined action of pushbutton
        # self.pushbutton[0].clicked.disconnect(self.function_4)
        # change origin matrix
        self.tablewidget[0].itemChanged.disconnect(self.matrix_calulate)

    @staticmethod
    def table_read(table):
        n = table.rowCount()
        matrix = np.zeros((n, n), dtype=float)
        for i in range(n):
            for j in range(n):
                try:
                    matrix[i, j] = float(table.item(i, j).text())
                except ValueError:
                    matrix[i, j] = 0
        return matrix

    @staticmethod
    def table_write(dim, table, matrix, decimal_digits=None, color_indexes=None, color=None):
        table.setColumnCount(dim)
        table.setRowCount(dim)
        for i in range(dim):
            for j in range(dim):
                try:
                    if decimal_digits is None:
                        new_item = QTableWidgetItem(str(matrix[i, j]))
                    else:
                        if abs(matrix[i, j]) < 0.001:
                            new_item = QTableWidgetItem('0')
                        else:
                            new_item = QTableWidgetItem(decimal_digits % matrix[i, j])
                except IndexError:
                    if decimal_digits is None:
                        new_item = QTableWidgetItem(str(1.0 * np.random.randint(0, 10)))
                    else:
                        new_item = QTableWidgetItem(decimal_digits % np.random.randint(0, 10))

                if color_indexes is not None:
                    max_index = np.max(color_indexes)
                    if color_indexes[i, j] != 0:
                        new_item.setBackground(QColor((max_index - color_indexes[i, j] // 2) * (color[0] // max_index), (max_index - color_indexes[i, j] // 2) * (color[1] // max_index), (max_index - color_indexes[i, j] // 2) * (color[2] // max_index)))

                table.setItem(i, j, new_item)

        table.resizeColumnsToContents()

    def matrix_calulate(self):
        """
        calculate A P L U by using Gaussian elimination with partial pivoting.
        """
        for i in range(3):
            if i == 0:
                A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes = LuAlgorithm().lu_0(A=self.table_read(self.tablewidget[0]), loop=int(self.combobox[1].currentText()))
            elif i == 1:
                A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes = LuAlgorithm().lu_1(A=self.table_read(self.tablewidget[0]), loop=int(self.combobox[1].currentText()))
            else:
                A, P, L, U, A_indexes, P_indexes, L_indexes, U_indexes = LuAlgorithm().lu_2(A=self.table_read(self.tablewidget[0]), loop=int(self.combobox[1].currentText()))
            self.table_write(dim=int(self.combobox[0].currentText()), table=self.tabwidget[0].tablewidget[0+4*i], matrix=A, decimal_digits=self.decimal_digits, color_indexes=A_indexes, color=self.tabwidget[0].color)
            self.table_write(dim=int(self.combobox[0].currentText()), table=self.tabwidget[0].tablewidget[1+4*i], matrix=P, decimal_digits='%d', color_indexes=P_indexes, color=self.tabwidget[0].color)
            self.table_write(dim=int(self.combobox[0].currentText()), table=self.tabwidget[0].tablewidget[2+4*i], matrix=L, decimal_digits=self.decimal_digits, color_indexes=L_indexes, color=self.tabwidget[0].color)
            self.table_write(dim=int(self.combobox[0].currentText()), table=self.tabwidget[0].tablewidget[3+4*i], matrix=U, decimal_digits=self.decimal_digits, color_indexes=U_indexes, color=self.tabwidget[0].color)

        self.tablewidget[0].resizeColumnsToContents()

    def function_combobox_0(self):
        self.widget_disconnet()

        # change combobox 1
        dim = int(self.combobox[0].currentText())
        self.combobox[1].clear()
        self.combobox[1].addItems(list(map(str, range(dim))))

        self.function_combobox_1()

        self.widget_connet()

    def function_combobox_1(self):
        # resize all the tables
        self.table_write(dim=int(self.combobox[0].currentText()), table=self.tablewidget[0], matrix=self.table_read(self.tablewidget[0]))

        # change table 1~12
        self.matrix_calulate()

    def function_radiobutton_0(self):
        self.widget_disconnet()

        if self.radiobutton[1].isChecked():

            n = self.tablewidget[0].columnCount()
            for i in range(n):
                for j in range(n):
                    new_item = QTableWidgetItem(str(1.0 * np.random.randint(0, 10)))
                    self.tablewidget[0].setItem(i, j, new_item)
            self.tablewidget[0].resizeColumnsToContents()

        # change table 0~11 inside the tabwidget.
        self.matrix_calulate()

        self.widget_connet()
