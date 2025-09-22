# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_trabajogreVAx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(585, 637)
        Dialog.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"font: 700 12pt \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_28)

        self.fecha_trabajo_editar = QLabel(self.frame_3)
        self.fecha_trabajo_editar.setObjectName(u"fecha_trabajo_editar")
        self.fecha_trabajo_editar.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.fecha_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_29)

        self.Cliente_trabajo_editar = QLineEdit(self.frame_3)
        self.Cliente_trabajo_editar.setObjectName(u"Cliente_trabajo_editar")
        self.Cliente_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_34.addWidget(self.Cliente_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_33.addWidget(self.label_30)

        self.patente_trabajo_editar = QLineEdit(self.frame_3)
        self.patente_trabajo_editar.setObjectName(u"patente_trabajo_editar")
        self.patente_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_33.addWidget(self.patente_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_31)

        self.telefono_trabajo_editar = QLineEdit(self.frame_3)
        self.telefono_trabajo_editar.setObjectName(u"telefono_trabajo_editar")
        self.telefono_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_32.addWidget(self.telefono_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.label_32)

        self.kilometro_trabajo_editar = QLineEdit(self.frame_3)
        self.kilometro_trabajo_editar.setObjectName(u"kilometro_trabajo_editar")
        self.kilometro_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_31.addWidget(self.kilometro_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_33)

        self.realizado_trabajo_editar = QLineEdit(self.frame_3)
        self.realizado_trabajo_editar.setObjectName(u"realizado_trabajo_editar")
        self.realizado_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_30.addWidget(self.realizado_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_30)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_34)

        self.btn_buscar_producto_trabajo = QPushButton(self.frame_3)
        self.btn_buscar_producto_trabajo.setObjectName(u"btn_buscar_producto_trabajo")
        self.btn_buscar_producto_trabajo.setMinimumSize(QSize(0, 30))
        self.btn_buscar_producto_trabajo.setMaximumSize(QSize(16777215, 30))
        self.btn_buscar_producto_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_buscar_producto_trabajo)

        self.btn_eliminar_editar_producto = QPushButton(self.frame_3)
        self.btn_eliminar_editar_producto.setObjectName(u"btn_eliminar_editar_producto")
        self.btn_eliminar_editar_producto.setMinimumSize(QSize(0, 30))
        self.btn_eliminar_editar_producto.setMaximumSize(QSize(16777215, 30))
        self.btn_eliminar_editar_producto.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_eliminar_editar_producto)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tabla_producto_buscado_editar = QTableView(self.frame_3)
        self.tabla_producto_buscado_editar.setObjectName(u"tabla_producto_buscado_editar")
        self.tabla_producto_buscado_editar.setStyleSheet(u"QTableView {\n"
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

        self.horizontalLayout.addWidget(self.tabla_producto_buscado_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_35)

        self.precio_trabajo_editar = QLineEdit(self.frame_3)
        self.precio_trabajo_editar.setObjectName(u"precio_trabajo_editar")
        self.precio_trabajo_editar.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_29.addWidget(self.precio_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.seleccionar_pago_editar_producto = QComboBox(self.frame_3)
        self.seleccionar_pago_editar_producto.addItem("")
        self.seleccionar_pago_editar_producto.addItem("")
        self.seleccionar_pago_editar_producto.addItem("")
        self.seleccionar_pago_editar_producto.setObjectName(u"seleccionar_pago_editar_producto")

        self.horizontalLayout_2.addWidget(self.seleccionar_pago_editar_producto)

        self.guardar_trabajo_editar = QPushButton(self.frame_3)
        self.guardar_trabajo_editar.setObjectName(u"guardar_trabajo_editar")
        self.guardar_trabajo_editar.setMinimumSize(QSize(0, 30))
        self.guardar_trabajo_editar.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.guardar_trabajo_editar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Fecha:", None))
        self.fecha_trabajo_editar.setText(QCoreApplication.translate("Dialog", u"Fecha", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Cliente o Vehiculo:", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Patente:", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Telefono:", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Kilometros", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Trabajo realizado:", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Producto usado:", None))
        self.btn_buscar_producto_trabajo.setText(QCoreApplication.translate("Dialog", u"Buscar productos", None))
        self.btn_eliminar_editar_producto.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"Precio", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Forma de pago", None))
        self.seleccionar_pago_editar_producto.setItemText(0, QCoreApplication.translate("Dialog", u"Efectivo", None))
        self.seleccionar_pago_editar_producto.setItemText(1, QCoreApplication.translate("Dialog", u"Transferencia", None))
        self.seleccionar_pago_editar_producto.setItemText(2, QCoreApplication.translate("Dialog", u"Tarjeta", None))

        self.guardar_trabajo_editar.setText(QCoreApplication.translate("Dialog", u"Guardar Trabajo", None))
    # retranslateUi

