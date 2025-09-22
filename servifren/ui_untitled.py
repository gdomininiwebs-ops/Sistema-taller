# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledLGBFLS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QDateEdit, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        def resource_path(relative_path):
                if hasattr(sys, "_MEIPASS"):
                        return os.path.join(sys._MEIPASS, relative_path)
                return os.path.join(os.path.abspath("."), relative_path)
        MainWindow.resize(946, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(200, 0))
        self.menu.setMaximumSize(QSize(0, 16777215))
        self.menu.setStyleSheet(u"background:#d9bf11")
        self.menu.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.btn_inicio = QPushButton(self.menu)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(0, 30))
        self.btn_inicio.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon = QIcon()
        icon.addFile(resource_path("asest/3643769-building-home-house-main-menu-start_113416.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_inicio.setIcon(icon)
        self.btn_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_inicio)

        self.btn_uno = QPushButton(self.menu)
        self.btn_uno.setObjectName(u"btn_uno")
        self.btn_uno.setMinimumSize(QSize(0, 30))
        self.btn_uno.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(resource_path("asest/products_items_icon_142979.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_uno.setIcon(icon1)
        self.btn_uno.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_uno)

        self.btn_dos = QPushButton(self.menu)
        self.btn_dos.setObjectName(u"btn_dos")
        self.btn_dos.setMinimumSize(QSize(0, 30))
        self.btn_dos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_dos.setAutoFillBackground(False)
        self.btn_dos.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(resource_path("asest/business_analysis_market_financial_report_sales_performance_icon_260976.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dos.setIcon(icon2)
        self.btn_dos.setIconSize(QSize(32, 32))
        self.btn_dos.setCheckable(False)
        self.btn_dos.setAutoRepeat(False)
        self.btn_dos.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.btn_dos)

        self.btn_tres = QPushButton(self.menu)
        self.btn_tres.setObjectName(u"btn_tres")
        self.btn_tres.setMinimumSize(QSize(0, 30))
        self.btn_tres.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(resource_path("asest/calendar-with-a-clock-time-tools_icon-icons.com_56831.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tres.setIcon(icon3)
        self.btn_tres.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_tres)

        self.btn_cuatro = QPushButton(self.menu)
        self.btn_cuatro.setObjectName(u"btn_cuatro")
        self.btn_cuatro.setMinimumSize(QSize(0, 30))
        self.btn_cuatro.setMaximumSize(QSize(200, 16777215))
        self.btn_cuatro.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(resource_path("asest/work-tools-crossed_icon-icons.com_68107.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cuatro.setIcon(icon4)
        self.btn_cuatro.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_cuatro)

        self.btn_cinco = QPushButton(self.menu)
        self.btn_cinco.setObjectName(u"btn_cinco")
        self.btn_cinco.setMinimumSize(QSize(0, 30))
        self.btn_cinco.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A9A9A9;\n"
"border-top-left-radius:15px;\n"
"border-bottom-left-radius:15px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(resource_path("asest/settingscog_87317.png"),
             QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cinco.setIcon(icon5)
        self.btn_cinco.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_cinco)

        self.verticalSpacer = QSpacerItem(20, 106, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 80))
        self.label_2.setMaximumSize(QSize(16777215, 80))
        self.label_2.setPixmap(QPixmap(resource_path("asest/logo_servi.png")))
        self.label_2.setScaledContents(True)


        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.menu)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_3 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_inicio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.fecha_inicio = QLabel(self.page_inicio)
        self.fecha_inicio.setObjectName(u"fecha_inicio")
        self.fecha_inicio.setStyleSheet(u"font:75 12pt;")

        self.horizontalLayout_3.addWidget(self.fecha_inicio)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.turnosinicio = QTableView(self.page_inicio)
        self.turnosinicio.setObjectName(u"turnosinicio")
        self.turnosinicio.setStyleSheet(u"QTableView {\n"
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
        self.turnosinicio.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.turnosinicio)

        self.stackedWidget.addWidget(self.page_inicio)
        self.page_productos = QWidget()
        self.page_productos.setObjectName(u"page_productos")
        self.verticalLayout_4 = QVBoxLayout(self.page_productos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_15 = QLabel(self.page_productos)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_17.addWidget(self.label_15)

        self.codigo_producto = QLineEdit(self.page_productos)
        self.codigo_producto.setObjectName(u"codigo_producto")
        self.codigo_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_17.addWidget(self.codigo_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.page_productos)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.nombre_producto = QLineEdit(self.page_productos)
        self.nombre_producto.setObjectName(u"nombre_producto")
        self.nombre_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.nombre_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.page_productos)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.descripcion_producto = QLineEdit(self.page_productos)
        self.descripcion_producto.setObjectName(u"descripcion_producto")
        self.descripcion_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_14.addWidget(self.descripcion_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_13 = QLabel(self.page_productos)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.categoria_producto = QLineEdit(self.page_productos)
        self.categoria_producto.setObjectName(u"categoria_producto")
        self.categoria_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_15.addWidget(self.categoria_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.page_productos)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.stock_producto = QLineEdit(self.page_productos)
        self.stock_producto.setObjectName(u"stock_producto")
        self.stock_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_12.addWidget(self.stock_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_39 = QLabel(self.page_productos)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_41.addWidget(self.label_39)

        self.precio_producto = QLineEdit(self.page_productos)
        self.precio_producto.setObjectName(u"precio_producto")
        self.precio_producto.setMaximumSize(QSize(16777215, 40))
        self.precio_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_41.addWidget(self.precio_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.page_productos)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.precio_producto_2 = QLineEdit(self.page_productos)
        self.precio_producto_2.setObjectName(u"precio_producto_2")
        self.precio_producto_2.setMaximumSize(QSize(16777215, 40))
        self.precio_producto_2.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_13.addWidget(self.precio_producto_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_16 = QLabel(self.page_productos)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_42.addWidget(self.label_16)

        self.buscador_producto = QLineEdit(self.page_productos)
        self.buscador_producto.setObjectName(u"buscador_producto")
        self.buscador_producto.setMaximumSize(QSize(16777215, 30))
        self.buscador_producto.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_42.addWidget(self.buscador_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_editar_producto = QPushButton(self.page_productos)
        self.boton_editar_producto.setObjectName(u"boton_editar_producto")
        self.boton_editar_producto.setMinimumSize(QSize(0, 30))
        self.boton_editar_producto.setMaximumSize(QSize(200, 16777215))
        self.boton_editar_producto.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")
        self.boton_editar_producto.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.boton_editar_producto)

        self.boton_borrar_producto = QPushButton(self.page_productos)
        self.boton_borrar_producto.setObjectName(u"boton_borrar_producto")
        self.boton_borrar_producto.setMinimumSize(QSize(100, 30))
        self.boton_borrar_producto.setMaximumSize(QSize(200, 30))
        self.boton_borrar_producto.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")
        self.boton_borrar_producto.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.boton_borrar_producto)

        self.boton_crear_producto = QPushButton(self.page_productos)
        self.boton_crear_producto.setObjectName(u"boton_crear_producto")
        self.boton_crear_producto.setMinimumSize(QSize(100, 30))
        self.boton_crear_producto.setMaximumSize(QSize(200, 30))
        self.boton_crear_producto.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")
        self.boton_crear_producto.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.boton_crear_producto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tabla_producto = QTableView(self.page_productos)
        self.tabla_producto.setObjectName(u"tabla_producto")
        self.tabla_producto.setStyleSheet(u"QTableView {\n"
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
        self.tabla_producto.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla_producto.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tabla_producto.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_4.addWidget(self.tabla_producto)

        self.stackedWidget.addWidget(self.page_productos)
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.verticalLayout_5 = QVBoxLayout(self.page_ventas)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.page_ventas)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.Cliente_ventas = QLineEdit(self.tab)
        self.Cliente_ventas.setObjectName(u"Cliente_ventas")
        self.Cliente_ventas.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_4.addWidget(self.Cliente_ventas)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.Fecha_ventas = QLineEdit(self.tab)
        self.Fecha_ventas.setObjectName(u"Fecha_ventas")
        self.Fecha_ventas.setStyleSheet(u"QLineEdit {\n"
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
        self.Fecha_ventas.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.Fecha_ventas)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.codigo_venta = QLineEdit(self.tab)
        self.codigo_venta.setObjectName(u"codigo_venta")
        self.codigo_venta.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_7.addWidget(self.codigo_venta)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.Product_ventas = QLineEdit(self.tab)
        self.Product_ventas.setObjectName(u"Product_ventas")
        self.Product_ventas.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_7.addWidget(self.Product_ventas)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.cantidad_ventas = QLineEdit(self.tab)
        self.cantidad_ventas.setObjectName(u"cantidad_ventas")
        self.cantidad_ventas.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_7.addWidget(self.cantidad_ventas)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.precio_ventas = QLineEdit(self.tab)
        self.precio_ventas.setObjectName(u"precio_ventas")
        self.precio_ventas.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_8.addWidget(self.precio_ventas)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.boton_buscar_venta = QPushButton(self.tab)
        self.boton_buscar_venta.setObjectName(u"boton_buscar_venta")
        self.boton_buscar_venta.setMinimumSize(QSize(150, 0))
        self.boton_buscar_venta.setMaximumSize(QSize(150, 30))
        self.boton_buscar_venta.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../asets/searchmagnifierinterfacesymbol1_79893.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_buscar_venta.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.boton_buscar_venta)

        self.boton_agregar_venta = QPushButton(self.tab)
        self.boton_agregar_venta.setObjectName(u"boton_agregar_venta")
        self.boton_agregar_venta.setMinimumSize(QSize(150, 0))
        self.boton_agregar_venta.setMaximumSize(QSize(150, 30))
        self.boton_agregar_venta.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../asets/plus_icon-icons.com_61187.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boton_agregar_venta.setIcon(icon7)

        self.horizontalLayout_8.addWidget(self.boton_agregar_venta)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.boton_eliminar_venta = QPushButton(self.tab)
        self.boton_eliminar_venta.setObjectName(u"boton_eliminar_venta")
        self.boton_eliminar_venta.setMinimumSize(QSize(150, 30))
        self.boton_eliminar_venta.setMaximumSize(QSize(150, 30))
        self.boton_eliminar_venta.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.boton_eliminar_venta)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_6.addWidget(self.tableWidget)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.combox_forma_pago_venta = QComboBox(self.tab)
        self.combox_forma_pago_venta.addItem("")
        self.combox_forma_pago_venta.addItem("")
        self.combox_forma_pago_venta.addItem("")
        self.combox_forma_pago_venta.addItem("")
        self.combox_forma_pago_venta.setObjectName(u"combox_forma_pago_venta")
        self.combox_forma_pago_venta.setStyleSheet(u"QComboBox {\n"
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
"}")

        self.horizontalLayout_10.addWidget(self.combox_forma_pago_venta)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.lebel_total_venta = QLabel(self.tab)
        self.lebel_total_venta.setObjectName(u"lebel_total_venta")
        self.lebel_total_venta.setStyleSheet(u"font: 700 11pt \"Palatino Linotype\";\n"
"text-decoration: underline;")

        self.horizontalLayout_9.addWidget(self.lebel_total_venta)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)

        self.boton_registrar_ventas = QPushButton(self.tab)
        self.boton_registrar_ventas.setObjectName(u"boton_registrar_ventas")
        self.boton_registrar_ventas.setMinimumSize(QSize(0, 30))
        self.boton_registrar_ventas.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_19.addWidget(self.boton_registrar_ventas)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_23 = QLabel(self.tab_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_20)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_20.addWidget(self.label_21)

        self.fecha_desde_venta = QDateEdit(self.tab_2)
        self.fecha_desde_venta.setObjectName(u"fecha_desde_venta")
        self.fecha_desde_venta.setStyleSheet(u"QDateEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.fecha_desde_venta.setCalendarPopup(True)

        self.horizontalLayout_20.addWidget(self.fecha_desde_venta)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_21.addWidget(self.label_22)

        self.fecha_hasta_venta = QDateEdit(self.tab_2)
        self.fecha_hasta_venta.setObjectName(u"fecha_hasta_venta")
        self.fecha_hasta_venta.setStyleSheet(u"QDateEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.fecha_hasta_venta.setCalendarPopup(True)

        self.horizontalLayout_21.addWidget(self.fecha_hasta_venta)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.tabla_registro_venta = QTableWidget(self.tab_2)
        self.tabla_registro_venta.setObjectName(u"tabla_registro_venta")
        self.tabla_registro_venta.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_7.addWidget(self.tabla_registro_venta)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_ventas)
        self.page_turnos = QWidget()
        self.page_turnos.setObjectName(u"page_turnos")
        self.verticalLayout_8 = QVBoxLayout(self.page_turnos)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget_2 = QTabWidget(self.page_turnos)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_10 = QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.fecha_turno = QDateEdit(self.tab_3)
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

        self.hora_turno = QTimeEdit(self.tab_3)
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


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_25)

        self.cliente_turno = QLineEdit(self.tab_3)
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

        self.horizontalLayout_27.addWidget(self.cliente_turno)


        self.verticalLayout_10.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.patente_turno = QLineEdit(self.tab_3)
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


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.label_27)

        self.telefono_turno = QLineEdit(self.tab_3)
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

        self.horizontalLayout_25.addWidget(self.telefono_turno)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_11.addWidget(self.label_28)

        self.Trabajo_realizar_turno = QTextEdit(self.tab_3)
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

        self.verticalLayout_11.addWidget(self.Trabajo_realizar_turno)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.boton_guardar_turno = QPushButton(self.tab_3)
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

        self.verticalLayout_10.addWidget(self.boton_guardar_turno)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_13 = QVBoxLayout(self.tab_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_29 = QLabel(self.tab_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_29)

        self.calendario_turno = QCalendarWidget(self.tab_4)
        self.calendario_turno.setObjectName(u"calendario_turno")
        self.calendario_turno.setMaximumSize(QSize(16777215, 250))
        self.calendario_turno.setStyleSheet(u"QCalendarWidget {\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 10px;\n"
"    background-color: #fdfdfd;\n"
"    color: #333;\n"
"    font-family: 'Segoe UI';\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #eaf2f8;\n"
"    border-bottom: 1px solid #ccc;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #2E86C1;\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #1B4F72;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    selection-background-color: #AED6F1;\n"
"    selection-color: black;\n"
"    background-color: #ffffff"
                        ";\n"
"    gridline-color: #eee;\n"
"}")

        self.verticalLayout_12.addWidget(self.calendario_turno)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.tabla_registro_turno = QTableWidget(self.tab_4)
        self.tabla_registro_turno.setObjectName(u"tabla_registro_turno")
        self.tabla_registro_turno.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_13.addWidget(self.tabla_registro_turno)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.boton_editar_turno = QPushButton(self.tab_4)
        self.boton_editar_turno.setObjectName(u"boton_editar_turno")
        self.boton_editar_turno.setMaximumSize(QSize(16777215, 30))
        self.boton_editar_turno.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.boton_editar_turno)

        self.boton_borrar_turno = QPushButton(self.tab_4)
        self.boton_borrar_turno.setObjectName(u"boton_borrar_turno")
        self.boton_borrar_turno.setMinimumSize(QSize(0, 30))
        self.boton_borrar_turno.setMaximumSize(QSize(16777215, 30))
        self.boton_borrar_turno.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.boton_borrar_turno)

        self.boton_realizado_turno = QPushButton(self.tab_4)
        self.boton_realizado_turno.setObjectName(u"boton_realizado_turno")
        self.boton_realizado_turno.setMinimumSize(QSize(0, 30))
        self.boton_realizado_turno.setMaximumSize(QSize(16777215, 30))
        self.boton_realizado_turno.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.boton_realizado_turno)


        self.verticalLayout_13.addLayout(self.horizontalLayout_24)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_8.addWidget(self.tabWidget_2)

        self.stackedWidget.addWidget(self.page_turnos)
        self.page_trabajos = QWidget()
        self.page_trabajos.setObjectName(u"page_trabajos")
        self.verticalLayout_14 = QVBoxLayout(self.page_trabajos)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tabWidget_3 = QTabWidget(self.page_trabajos)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_9 = QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_30)

        self.label_fecha_trabajo = QLabel(self.tab_5)
        self.label_fecha_trabajo.setObjectName(u"label_fecha_trabajo")
        self.label_fecha_trabajo.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_fecha_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_31 = QLabel(self.tab_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_34.addWidget(self.label_31)

        self.cliente_trabajo = QLineEdit(self.tab_5)
        self.cliente_trabajo.setObjectName(u"cliente_trabajo")
        self.cliente_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_34.addWidget(self.cliente_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_32 = QLabel(self.tab_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_33.addWidget(self.label_32)

        self.patente_trabajo = QLineEdit(self.tab_5)
        self.patente_trabajo.setObjectName(u"patente_trabajo")
        self.patente_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_33.addWidget(self.patente_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_33 = QLabel(self.tab_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_33)

        self.telefono_trabajo = QLineEdit(self.tab_5)
        self.telefono_trabajo.setObjectName(u"telefono_trabajo")
        self.telefono_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_32.addWidget(self.telefono_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_34 = QLabel(self.tab_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.label_34)

        self.kilometro_trabajo = QLineEdit(self.tab_5)
        self.kilometro_trabajo.setObjectName(u"kilometro_trabajo")
        self.kilometro_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_31.addWidget(self.kilometro_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_35 = QLabel(self.tab_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_35)

        self.realizado_trabajo = QLineEdit(self.tab_5)
        self.realizado_trabajo.setObjectName(u"realizado_trabajo")
        self.realizado_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_30.addWidget(self.realizado_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_36 = QLabel(self.tab_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_15.addWidget(self.label_36)

        self.btn_buscar_producto_trabajo = QPushButton(self.tab_5)
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

        self.verticalLayout_15.addWidget(self.btn_buscar_producto_trabajo)

        self.btn_eliminar_producto_trabajo = QPushButton(self.tab_5)
        self.btn_eliminar_producto_trabajo.setObjectName(u"btn_eliminar_producto_trabajo")
        self.btn_eliminar_producto_trabajo.setMinimumSize(QSize(0, 30))
        self.btn_eliminar_producto_trabajo.setMaximumSize(QSize(16777215, 30))
        self.btn_eliminar_producto_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_15.addWidget(self.btn_eliminar_producto_trabajo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.horizontalLayout_36.addLayout(self.verticalLayout_15)

        self.tableWidget_2 = QTableWidget(self.tab_5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.horizontalLayout_36.addWidget(self.tableWidget_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_37 = QLabel(self.tab_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_37)

        self.precio_trabajo = QLineEdit(self.tab_5)
        self.precio_trabajo.setObjectName(u"precio_trabajo")
        self.precio_trabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_29.addWidget(self.precio_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_40 = QLabel(self.tab_5)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_35.addWidget(self.label_40)

        self.forma_pago_trabajo = QComboBox(self.tab_5)
        self.forma_pago_trabajo.addItem("")
        self.forma_pago_trabajo.addItem("")
        self.forma_pago_trabajo.addItem("")
        self.forma_pago_trabajo.addItem("")
        self.forma_pago_trabajo.setObjectName(u"forma_pago_trabajo")
        self.forma_pago_trabajo.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_35.addWidget(self.forma_pago_trabajo)

        self.guardar_trabajo = QPushButton(self.tab_5)
        self.guardar_trabajo.setObjectName(u"guardar_trabajo")
        self.guardar_trabajo.setMinimumSize(QSize(0, 30))
        self.guardar_trabajo.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_35.addWidget(self.guardar_trabajo)


        self.verticalLayout_9.addLayout(self.horizontalLayout_35)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_17 = QVBoxLayout(self.tab_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.buscar_listatrabajo = QLineEdit(self.tab_6)
        self.buscar_listatrabajo.setObjectName(u"buscar_listatrabajo")
        self.buscar_listatrabajo.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_37.addWidget(self.buscar_listatrabajo)


        self.verticalLayout_17.addLayout(self.horizontalLayout_37)

        self.tableWidget_3 = QTableWidget(self.tab_6)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_17.addWidget(self.tableWidget_3)

        self.tabWidget_3.addTab(self.tab_6, "")

        self.verticalLayout_14.addWidget(self.tabWidget_3)

        self.stackedWidget.addWidget(self.page_trabajos)
        self.page_configuracion = QWidget()
        self.page_configuracion.setObjectName(u"page_configuracion")
        self.verticalLayout_18 = QVBoxLayout(self.page_configuracion)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget_4 = QTabWidget(self.page_configuracion)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_21 = QVBoxLayout(self.tab_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_46 = QLabel(self.tab_9)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_47.addWidget(self.label_46)

        self.sincronizar_2 = QPushButton(self.tab_9)
        self.sincronizar_2.setObjectName(u"sincronizar_2")
        self.sincronizar_2.setMinimumSize(QSize(0, 30))
        self.sincronizar_2.setStyleSheet(u"QPushButton{\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_47.addWidget(self.sincronizar_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_38 = QLabel(self.tab_9)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_46.addWidget(self.label_38)

        self.whatsapp_2 = QPushButton(self.tab_9)
        self.whatsapp_2.setObjectName(u"whatsapp_2")
        self.whatsapp_2.setMinimumSize(QSize(0, 30))
        self.whatsapp_2.setStyleSheet(u"QPushButton{\n"
"	background-color: #5FFC7B;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"border-radius:15px;\n"
"font:75 12pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_46.addWidget(self.whatsapp_2)

        self.instagram_2 = QPushButton(self.tab_9)
        self.instagram_2.setObjectName(u"instagram_2")
        self.instagram_2.setMinimumSize(QSize(0, 30))
        self.instagram_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #feda75,\n"
"        stop:0.5 #d62976,\n"
"        stop:1 #962fbf\n"
"    );\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(203, 0, 0);\n"
"border-radius:15px;\n"
"}")

        self.horizontalLayout_46.addWidget(self.instagram_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_5 = QSpacerItem(20, 452, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)

        self.tabWidget_4.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_22 = QVBoxLayout(self.tab_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_47 = QLabel(self.tab_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_47)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_48 = QLabel(self.tab_10)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_49.addWidget(self.label_48)

        self.fecha_desde_reporte = QDateEdit(self.tab_10)
        self.fecha_desde_reporte.setObjectName(u"fecha_desde_reporte")
        self.fecha_desde_reporte.setStyleSheet(u"QDateEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.fecha_desde_reporte.setCalendarPopup(True)

        self.horizontalLayout_49.addWidget(self.fecha_desde_reporte)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_49 = QLabel(self.tab_10)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_50.addWidget(self.label_49)

        self.fecha_hasta_reposrte = QDateEdit(self.tab_10)
        self.fecha_hasta_reposrte.setObjectName(u"fecha_hasta_reposrte")
        self.fecha_hasta_reposrte.setStyleSheet(u"QDateEdit {\n"
"    border: 1px solid #888;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"    font-weight: bold;\n"
"}")
        self.fecha_hasta_reposrte.setCalendarPopup(True)

        self.horizontalLayout_50.addWidget(self.fecha_hasta_reposrte)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_50)


        self.verticalLayout_22.addLayout(self.horizontalLayout_48)

        self.combox_reporte = QComboBox(self.tab_10)
        self.combox_reporte.addItem("")
        self.combox_reporte.addItem("")
        self.combox_reporte.addItem("")
        self.combox_reporte.addItem("")
        self.combox_reporte.addItem("")
        self.combox_reporte.setObjectName(u"combox_reporte")
        self.combox_reporte.setStyleSheet(u"QComboBox {\n"
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
"}")

        self.verticalLayout_22.addWidget(self.combox_reporte)

        self.tabla_reporte = QTableWidget(self.tab_10)
        self.tabla_reporte.setObjectName(u"tabla_reporte")
        self.tabla_reporte.setStyleSheet(u"QTableWidget {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"    gridline-color: #eeeeee;\n"
"}\n"
"\n"
"QHeaderWidget::section {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_22.addWidget(self.tabla_reporte)

        self.tabWidget_4.addTab(self.tab_10, "")

        self.verticalLayout_18.addWidget(self.tabWidget_4)

        self.stackedWidget.addWidget(self.page_configuracion)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.btn_uno.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.btn_dos.setText(QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.btn_tres.setText(QCoreApplication.translate("MainWindow", u"TURNOS", None))
        self.btn_cuatro.setText(QCoreApplication.translate("MainWindow", u"TRABAJOS", None))
        self.btn_cinco.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACION", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"GDomininiWebs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Turnos del dia", None))
        self.fecha_inicio.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Codigo*:", None))
        self.codigo_producto.setText("")
        self.codigo_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Producto*:", None))
        self.nombre_producto.setText("")
        self.nombre_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.descripcion_producto.setText("")
        self.descripcion_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Categoria:", None))
        self.categoria_producto.setText("")
        self.categoria_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stock:", None))
        self.stock_producto.setText("")
        self.stock_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.precio_producto.setText("")
        self.precio_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Precio*:", None))
        self.precio_producto_2.setText("")
        self.precio_producto_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.buscador_producto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por nombre, codigo, descripcion......", None))
        self.boton_editar_producto.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.boton_borrar_producto.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.boton_crear_producto.setText(QCoreApplication.translate("MainWindow", u"CREAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cliente*:", None))
        self.Cliente_ventas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Codigo:", None))
        self.codigo_venta.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Producto:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cant:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.boton_buscar_venta.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.boton_agregar_venta.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Productos seleccionados", None))
        self.boton_eliminar_venta.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Forma de pago:", None))
        self.combox_forma_pago_venta.setItemText(0, QCoreApplication.translate("MainWindow", u"------------", None))
        self.combox_forma_pago_venta.setItemText(1, QCoreApplication.translate("MainWindow", u"Efectivo", None))
        self.combox_forma_pago_venta.setItemText(2, QCoreApplication.translate("MainWindow", u"Transferencia", None))
        self.combox_forma_pago_venta.setItemText(3, QCoreApplication.translate("MainWindow", u"Tarjeta", None))

        self.combox_forma_pago_venta.setCurrentText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.lebel_total_venta.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.boton_registrar_ventas.setText(QCoreApplication.translate("MainWindow", u"Registrar venta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Regiastro ventas", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Registro de ventas", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Filtrar por fecha:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Hasta:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Listado ventas", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Cliente o vehiculo*:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Patente:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Numero Telefono:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Trabajo a realizar*:", None))
        self.boton_guardar_turno.setText(QCoreApplication.translate("MainWindow", u"Guardar Turno", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cargar Turnos", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Seleccionar fecha", None))
        self.boton_editar_turno.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.boton_borrar_turno.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.boton_realizado_turno.setText(QCoreApplication.translate("MainWindow", u"Pasar a realizado", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Turnos", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_fecha_trabajo.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Cliente o Vehiculo:", None))
        self.cliente_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Patente:", None))
        self.patente_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patente", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.telefono_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Kilometros", None))
        self.kilometro_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kilometros", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Trabajo realizado:", None))
        self.realizado_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Trabajo a realizar", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Producto usado:", None))
        self.btn_buscar_producto_trabajo.setText(QCoreApplication.translate("MainWindow", u"Buscar productos", None))
        self.btn_eliminar_producto_trabajo.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.precio_trabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Forma de pago", None))
        self.forma_pago_trabajo.setItemText(0, QCoreApplication.translate("MainWindow", u"------------", None))
        self.forma_pago_trabajo.setItemText(1, QCoreApplication.translate("MainWindow", u"Efectivo", None))
        self.forma_pago_trabajo.setItemText(2, QCoreApplication.translate("MainWindow", u"Transferencia", None))
        self.forma_pago_trabajo.setItemText(3, QCoreApplication.translate("MainWindow", u"Tarjeta", None))

        self.guardar_trabajo.setText(QCoreApplication.translate("MainWindow", u"Guardar Trabajo", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cargar trabajo", None))
        self.buscar_listatrabajo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por cliente o patente ", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Lista Trabajo", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Sincronizacion:", None))
        self.sincronizar_2.setText(QCoreApplication.translate("MainWindow", u"Sincronizar", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Soporte:", None))
        self.whatsapp_2.setText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        self.instagram_2.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Configuracion", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Filtrar por fecha:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Hasta:", None))
        self.combox_reporte.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar reporte", None))
        self.combox_reporte.setItemText(1, QCoreApplication.translate("MainWindow", u"Productos Vendidos", None))
        self.combox_reporte.setItemText(2, QCoreApplication.translate("MainWindow", u"Forma de pagos", None))
        self.combox_reporte.setItemText(3, QCoreApplication.translate("MainWindow", u"Trabajos realizados", None))
        self.combox_reporte.setItemText(4, QCoreApplication.translate("MainWindow", u"Ventas", None))

        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Reportes", None))
    # retranslateUi

