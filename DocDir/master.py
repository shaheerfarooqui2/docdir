# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lenovo\Desktop\DocDir\ui\master.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 551)
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(620, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.add_patient = QtWidgets.QPushButton(self.centralwidget)
        self.add_patient.setStyleSheet("color: rgb(255, 255, 255);")
        self.add_patient.setObjectName("add_patient")
        self.gridLayout.addWidget(self.add_patient, 0, 1, 1, 1)
        self.datatree = QtWidgets.QTreeWidget(self.centralwidget)
        self.datatree.setStyleSheet("QHeaderView::section {                          \n"
"    color: white;\n"
"    resize:both;\n"
"    overflow:auto;                               \n"
"    padding: 2px;                               \n"
"    height:20px;                                \n"
"    border: 1px white;                  \n"
"    border-left:1px;                            \n"
"    border-right:1px;                           \n"
"    background: black;                        \n"
"}\n"
"QTreeWidget::item\n"
"{\n"
"    color : white;\n"
"    padding-left:10px;\n"
"    padding-top: 1px;\n"
"    padding-bottom: 1px;\n"
"    border-left: 10px;\n"
"}")
        self.datatree.setIndentation(40)
        self.datatree.setAnimated(True)
        self.datatree.setWordWrap(True)
        self.datatree.setObjectName("datatree")
        self.datatree.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.datatree.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.datatree.headerItem().setTextAlignment(2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.datatree.headerItem().setTextAlignment(3, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.datatree.header().setDefaultSectionSize(150)
        self.datatree.header().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.datatree, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medical Records"))
        self.add_patient.setText(_translate("MainWindow", "Add"))
        self.datatree.setSortingEnabled(True)
        self.datatree.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.datatree.headerItem().setText(1, _translate("MainWindow", "Address"))
        self.datatree.headerItem().setText(2, _translate("MainWindow", "Contact"))
        self.datatree.headerItem().setText(3, _translate("MainWindow", "Prescription"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
