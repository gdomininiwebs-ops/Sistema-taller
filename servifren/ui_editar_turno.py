# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_turnoMfyVbn.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(566, 508)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.label_22)

        self.fecha_turno = QDateEdit(Dialog)
        self.fecha_turno.setObjectName(u"fecha_turno")
        self.fecha_turno.setStyleSheet(u"QDateEdit, QTimeEdit, QDateTimeEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.fecha_turno.setCalendarPopup(True)

        self.horizontalLayout_23.addWidget(self.fecha_turno)

        self.hora_turno = QTimeEdit(Dialog)
        self.hora_turno.setObjectName(u"hora_turno")
        self.hora_turno.setStyleSheet(u"QDateEdit, QTimeEdit, QDateTimeEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.hora_turno.setCalendarPopup(True)

        self.horizontalLayout_23.addWidget(self.hora_turno)


        self.verticalLayout.addLayout(self.horizontalLayout_23)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_23)

        self.cliente_turno = QLineEdit(Dialog)
        self.cliente_turno.setObjectName(u"cliente_turno")
        self.cliente_turno.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.cliente_turno)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_25)

        self.telefono_turno = QLineEdit(Dialog)
        self.telefono_turno.setObjectName(u"telefono_turno")
        self.telefono_turno.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.telefono_turno)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.label_24)

        self.patente_turno = QLineEdit(Dialog)
        self.patente_turno.setObjectName(u"patente_turno")
        self.patente_turno.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.patente_turno)


        self.verticalLayout_2.addLayout(self.horizontalLayout_26)

        self.label_26 = QLabel(Dialog)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_26)

        self.Trabajo_realizar_turno = QTextEdit(Dialog)
        self.Trabajo_realizar_turno.setObjectName(u"Trabajo_realizar_turno")
        self.Trabajo_realizar_turno.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid #888;\n"
"    border-radius: 10px;\n"
"    padding: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: #333;\n"
"}\n"
"QTextEdit:focus {\n"
"    border: 2px solid #0078d7; /* color de foco */\n"
"}\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.Trabajo_realizar_turno)

        self.boton_guardar_turno = QPushButton(Dialog)
        self.boton_guardar_turno.setObjectName(u"boton_guardar_turno")
        self.boton_guardar_turno.setMinimumSize(QSize(0, 30))
        self.boton_guardar_turno.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_2.addWidget(self.boton_guardar_turno)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Cliente o vehiculo*:", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Numero Telefono:", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Patente:", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Trabajo a realizar*:", None))
        self.boton_guardar_turno.setText(QCoreApplication.translate("Dialog", u"Editar", None))
    # retranslateUi

