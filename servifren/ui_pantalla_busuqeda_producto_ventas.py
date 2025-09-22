# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_busuqeda_producto_ventastaDqyk.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(545, 485)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.busqueda_emerguente = QLineEdit(Dialog)
        self.busqueda_emerguente.setObjectName(u"busqueda_emerguente")
        self.busqueda_emerguente.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"")
        
        self.verticalLayout.addWidget(self.busqueda_emerguente)

        self.tabla_producto_trabajo = QTableView(Dialog)
        self.tabla_producto_trabajo.setObjectName(u"tabla_producto_trabajo")
        self.tabla_producto_trabajo.setStyleSheet(u"QTableView {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout.addWidget(self.tabla_producto_trabajo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.cantidad_producto_trabajo = QPushButton(Dialog)
        self.cantidad_producto_trabajo.setObjectName(u"cantidad_producto_trabajo")
        self.cantidad_producto_trabajo.setMaximumSize(QSize(100, 30))
        self.cantidad_producto_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cantidad_producto_trabajo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.busqueda_emerguente.setPlaceholderText(QCoreApplication.translate("Dialog", u"Buscar....", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.cantidad_producto_trabajo.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
    # retranslateUi

