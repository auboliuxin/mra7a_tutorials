# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'publish_pose_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(231, 134, 195, 263))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 2, -1, 3)
        self.verticalLayout_2.setSpacing(13)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_x = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_x.setObjectName("le_x")
        self.verticalLayout.addWidget(self.le_x)
        self.le_y = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_y.setObjectName("le_y")
        self.verticalLayout.addWidget(self.le_y)
        self.le_z = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_z.setObjectName("le_z")
        self.verticalLayout.addWidget(self.le_z)
        self.le_R = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_R.setObjectName("le_R")
        self.verticalLayout.addWidget(self.le_R)
        self.le_P = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_P.setObjectName("le_P")
        self.verticalLayout.addWidget(self.le_P)
        self.le_Y = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_Y.setObjectName("le_Y")
        self.verticalLayout.addWidget(self.le_Y)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X："))
        self.label_2.setText(_translate("MainWindow", "Y："))
        self.label_3.setText(_translate("MainWindow", "Z："))
        self.label_4.setText(_translate("MainWindow", "Roll："))
        self.label_5.setText(_translate("MainWindow", "Pitch："))
        self.label_6.setText(_translate("MainWindow", "Yaw："))
        self.le_x.setText(_translate("MainWindow", "0.4"))
        self.le_y.setText(_translate("MainWindow", "0"))
        self.le_z.setText(_translate("MainWindow", "0.4"))
        self.le_R.setText(_translate("MainWindow", "0"))
        self.le_P.setText(_translate("MainWindow", "90"))
        self.le_Y.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Publish"))

