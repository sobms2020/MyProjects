# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foton_display2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 203, 2);\n"
"gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.tabWidget.setObjectName("tabWidget")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.splitter_2 = QtWidgets.QSplitter(self.tab3)
        self.splitter_2.setGeometry(QtCore.QRect(0, 0, 871, 581))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setStyleSheet("color: rgb(255, 203, 2);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setStyleSheet("color: rgb(255, 203, 2);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setStyleSheet("color: rgb(255, 203, 2);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setStyleSheet("color: rgb(255, 203, 2);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setStyleSheet("font: 75 17pt \"Sitka Text\";\n"
"border:3px solid rgb(0,0,0);\n"
"border-radius: 18px;\n"
"border-color:#6C6B6A;\n"
"color: rgb(255, 203, 2);")
        self.pushButton_6.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.lineEdit_4.raise_()
        self.label_5.raise_()
        self.lineEdit_5.raise_()
        self.label_6.raise_()
        self.lineEdit_6.raise_()
        self.label_7.raise_()
        self.lineEdit_7.raise_()
        self.groupBox.raise_()
        self.tabWidget.addTab(self.tab3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 861, 551))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView_2 = QtWidgets.QListView(self.tab_2)
        self.listView_2.setGeometry(QtCore.QRect(590, 10, 261, 571))
        self.listView_2.setObjectName("listView_2")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(600, 20, 221, 21))
        self.label_12.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(600, 40, 91, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(600, 60, 91, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(600, 80, 71, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(690, 60, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 100, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(600, 130, 251, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(600, 150, 91, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 150, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(600, 170, 71, 16))
        self.label_18.setObjectName("label_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 190, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(600, 220, 161, 21))
        self.label_19.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(600, 240, 71, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(600, 260, 81, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(690, 260, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(600, 280, 61, 16))
        self.label_22.setObjectName("label_22")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 300, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(600, 330, 131, 21))
        self.label_23.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(600, 360, 161, 16))
        self.label_24.setObjectName("label_24")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(760, 360, 81, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(600, 380, 141, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(760, 380, 81, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(600, 400, 81, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(600, 420, 251, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(600, 440, 61, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(600, 460, 221, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(600, 480, 47, 13))
        self.label_30.setObjectName("label_30")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 500, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(30, 10, 551, 191))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(30, 200, 551, 191))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(30, 390, 551, 191))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(690, 40, 47, 16))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(690, 80, 47, 16))
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(690, 170, 47, 16))
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(690, 240, 47, 16))
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(690, 280, 47, 16))
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(700, 400, 47, 21))
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(660, 440, 47, 16))
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab_2)
        self.label_39.setGeometry(QtCore.QRect(650, 476, 47, 20))
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Год"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Месяц"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "День"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Час"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Нагрузка"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "+dE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "-dE"))
        self.label_4.setText(_translate("MainWindow", "А1"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.0010332"))
        self.label_5.setText(_translate("MainWindow", "А2"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.00087737"))
        self.label_6.setText(_translate("MainWindow", "В1"))
        self.lineEdit_6.setText(_translate("MainWindow", "0.73"))
        self.label_7.setText(_translate("MainWindow", "В2"))
        self.lineEdit_7.setText(_translate("MainWindow", "0.5691056"))
        self.lineEdit.setText(_translate("MainWindow", "200"))
        self.label.setText(_translate("MainWindow", "Параметр солнечного модуля, Вт"))
        self.label_2.setText(_translate("MainWindow", "КПД инвертора"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Максимальное число панелей, шт"))
        self.lineEdit_3.setText(_translate("MainWindow", "6000"))
        self.label_8.setText(_translate("MainWindow", "Результаты вычислений"))
        self.label_9.setText(_translate("MainWindow", "P_max(кВт*ч) ="))
        self.label_10.setText(_translate("MainWindow", "Оптимальное кол-во панелей, шт"))
        self.pushButton_6.setText(_translate("MainWindow", "Рассчитать"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить данные"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Рассчёт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "График"))
        self.label_12.setText(_translate("MainWindow", "Электролизные установки (ЭУ)"))
        self.label_13.setText(_translate("MainWindow", "Nmax ЭУ, кВт ="))
        self.label_14.setText(_translate("MainWindow", "Av, кВт*ч/нм3 ="))
        self.label_15.setText(_translate("MainWindow", "V_h2, нм3/ч ="))
        self.pushButton_2.setText(_translate("MainWindow", "Рассчитать V"))
        self.label_16.setText(_translate("MainWindow", "Подбор электролизера с производительностью:"))
        self.label_17.setText(_translate("MainWindow", "V_h2_ЭУ, нм3/ч ="))
        self.label_18.setText(_translate("MainWindow", "К ЭУ, шт ="))
        self.pushButton_3.setText(_translate("MainWindow", "Рассчитать К ЭУ"))
        self.label_19.setText(_translate("MainWindow", "Топливные элементы (ТЭ)"))
        self.label_20.setText(_translate("MainWindow", "N1 ТЭ, кВт ="))
        self.label_21.setText(_translate("MainWindow", "Nном ТЭ, кВт ="))
        self.label_22.setText(_translate("MainWindow", "К ТЭ, шт ="))
        self.pushButton_4.setText(_translate("MainWindow", "Рассчитать К ТЭ"))
        self.label_23.setText(_translate("MainWindow", "Количество баллонов"))
        self.label_24.setText(_translate("MainWindow", "Давление H2 в баллоне, бар ="))
        self.label_25.setText(_translate("MainWindow", "Объём баллона Vб Н2, м3 ="))
        self.label_26.setText(_translate("MainWindow", "E max H2,кВт ="))
        self.label_27.setText(_translate("MainWindow", "Максимальная масса H2 в системе хранения, кг"))
        self.label_28.setText(_translate("MainWindow", "MH2, кг ="))
        self.label_29.setText(_translate("MainWindow", "Количество баллонов в системе хранения"))
        self.label_30.setText(_translate("MainWindow", "Кб, шт ="))
        self.pushButton_5.setText(_translate("MainWindow", "Рассчитать Кб и МH2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Подбор оборудования"))
