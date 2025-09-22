# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ver_detalletQzTdz.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(578, 485)
        Dialog.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"font: 700 12pt \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_cliente_detalle = QLineEdit(Dialog)
        self.lineEdit_cliente_detalle.setObjectName(u"lineEdit_cliente_detalle")
        self.lineEdit_cliente_detalle.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_cliente_detalle.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_cliente_detalle.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_cliente_detalle)

        self.horizontalSpacer = QSpacerItem(21, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_fecha_detalle = QLineEdit(Dialog)
        self.lineEdit_fecha_detalle.setObjectName(u"lineEdit_fecha_detalle")
        self.lineEdit_fecha_detalle.setMaximumSize(QSize(200, 200))
        self.lineEdit_fecha_detalle.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit_fecha_detalle.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_fecha_detalle)

        self.horizontalSpacer_2 = QSpacerItem(21, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.tableView_detalle = QTableView(Dialog)
        self.tableView_detalle.setObjectName(u"tableView_detalle")
        self.tableView_detalle.setStyleSheet(u"QTableView {\n"
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
        self.tableView_detalle.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableView_detalle)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_total_detalle = QLabel(Dialog)
        self.label_total_detalle.setObjectName(u"label_total_detalle")

        self.horizontalLayout_4.addWidget(self.label_total_detalle)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_forma_detalle = QLabel(Dialog)
        self.label_forma_detalle.setObjectName(u"label_forma_detalle")

        self.horizontalLayout_4.addWidget(self.label_forma_detalle)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Detalles de venta", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Cliente", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Fecha", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Productos", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total", None))
        self.label_total_detalle.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Forma Pago", None))
        self.label_forma_detalle.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cerrar", None))
    # retranslateUi

