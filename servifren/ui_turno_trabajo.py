# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_turno_trabajoDvJoMh.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(603, 593)
        Dialog.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"font: 700 12pt \"Segoe UI\";")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.fecha_turno_trabajo = QLabel(Dialog)
        self.fecha_turno_trabajo.setObjectName(u"fecha_turno_trabajo")

        self.horizontalLayout_2.addWidget(self.fecha_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.cliente_turno_trabajo = QLineEdit(Dialog)
        self.cliente_turno_trabajo.setObjectName(u"cliente_turno_trabajo")
        self.cliente_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.cliente_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.patente_turno_trabajo = QLineEdit(Dialog)
        self.patente_turno_trabajo.setObjectName(u"patente_turno_trabajo")
        self.patente_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_3.addWidget(self.patente_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.telefono_turno_trabajo = QLineEdit(Dialog)
        self.telefono_turno_trabajo.setObjectName(u"telefono_turno_trabajo")
        self.telefono_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_4.addWidget(self.telefono_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.klilometros_turno_trabajo = QLineEdit(Dialog)
        self.klilometros_turno_trabajo.setObjectName(u"klilometros_turno_trabajo")
        self.klilometros_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_5.addWidget(self.klilometros_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.trabajo_turno_trabajo = QLineEdit(Dialog)
        self.trabajo_turno_trabajo.setObjectName(u"trabajo_turno_trabajo")
        self.trabajo_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_6.addWidget(self.trabajo_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label_8)

        self.boton_buscar_turno_trabajo = QPushButton(Dialog)
        self.boton_buscar_turno_trabajo.setObjectName(u"boton_buscar_turno_trabajo")
        self.boton_buscar_turno_trabajo.setMinimumSize(QSize(0, 30))
        self.boton_buscar_turno_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout.addWidget(self.boton_buscar_turno_trabajo)

        self.boton_eliminar_turno_trabajo = QPushButton(Dialog)
        self.boton_eliminar_turno_trabajo.setObjectName(u"boton_eliminar_turno_trabajo")
        self.boton_eliminar_turno_trabajo.setMinimumSize(QSize(0, 30))
        self.boton_eliminar_turno_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout.addWidget(self.boton_eliminar_turno_trabajo)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.tabla_productos_turno_trabajo = QTableWidget(Dialog)
        self.tabla_productos_turno_trabajo.setObjectName(u"tabla_productos_turno_trabajo")
        self.tabla_productos_turno_trabajo.setStyleSheet(u"QTableView {\n"
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

        self.horizontalLayout_7.addWidget(self.tabla_productos_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.precio_turno_trabajo = QLineEdit(Dialog)
        self.precio_turno_trabajo.setObjectName(u"precio_turno_trabajo")
        self.precio_turno_trabajo.setMinimumSize(QSize(50, 0))
        self.precio_turno_trabajo.setMaximumSize(QSize(100, 16777215))
        self.precio_turno_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_8.addWidget(self.precio_turno_trabajo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.forma_pago__turno_trabajo = QComboBox(Dialog)
        self.forma_pago__turno_trabajo.addItem("")
        self.forma_pago__turno_trabajo.addItem("")
        self.forma_pago__turno_trabajo.addItem("")
        self.forma_pago__turno_trabajo.addItem("")
        self.forma_pago__turno_trabajo.setObjectName(u"forma_pago__turno_trabajo")
        self.forma_pago__turno_trabajo.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down-arrow.png); /* opcional: \u00edcono personalizado */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.forma_pago__turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.boton_guardar_turno_trabajo_ = QPushButton(Dialog)
        self.boton_guardar_turno_trabajo_.setObjectName(u"boton_guardar_turno_trabajo_")
        self.boton_guardar_turno_trabajo_.setMinimumSize(QSize(0, 30))
        self.boton_guardar_turno_trabajo_.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.boton_guardar_turno_trabajo_)

        self.boton_cancela_turno_trabajo = QPushButton(Dialog)
        self.boton_cancela_turno_trabajo.setObjectName(u"boton_cancela_turno_trabajo")
        self.boton_cancela_turno_trabajo.setMinimumSize(QSize(0, 30))
        self.boton_cancela_turno_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.boton_cancela_turno_trabajo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Fecha", None))
        self.fecha_turno_trabajo.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Cliente", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Patente", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Telefono", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Kilometros", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Trabajo", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Productos", None))
        self.boton_buscar_turno_trabajo.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.boton_eliminar_turno_trabajo.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Precio", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Forma de pago", None))
        self.forma_pago__turno_trabajo.setItemText(0, QCoreApplication.translate("Dialog", u"----------", None))
        self.forma_pago__turno_trabajo.setItemText(1, QCoreApplication.translate("Dialog", u"Efectivo", None))
        self.forma_pago__turno_trabajo.setItemText(2, QCoreApplication.translate("Dialog", u"Transferencia", None))
        self.forma_pago__turno_trabajo.setItemText(3, QCoreApplication.translate("Dialog", u"Tarjeta", None))

        self.boton_guardar_turno_trabajo_.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.boton_cancela_turno_trabajo.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

