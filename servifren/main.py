## GDomininiWebs
#Telefono : +54 3516966161
import sys
import sqlite3
from ui_untitled import *
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, QDate
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QTimer
from datetime import datetime, date
import webbrowser
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import QSortFilterProxyModel
import bbdd as db
from ui_error_mismo_codigo import Ui_Dialog as Ui_mismo_codigo
from ui_error_campos_vacio import Ui_Dialog as Ui_campos_vacios
from ui_error_eliminar import Ui_Dialog as Ui_Dialog_error_eliminar
from ui_pantalla_busuqeda_producto_ventas import Ui_Dialog as Ui_busqueda_producto_ventas
from ui_confirmar_eliminar import Ui_Dialog as Ui_Dialog_confirmar_eliminar
from ui_ver_detalle import Ui_Dialog as Ui_detalle_ventas
from ui_editar_turno import Ui_Dialog as ui_editarturno
from ui_turno_trabajo import Ui_Dialog as ui_turno_realizado
from ui_detalle_trabajo import Ui_Dialog as Ui_detalletrabajo

class Ventanaerrorcampovacio(QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.ui = Ui_campos_vacios()
        self.ui.setupUi(self)
        self.ui.label.setText(mensaje)
        self.ui.pushButton.clicked.connect(self.accept)

class VentanaErrormismocodigo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mismo_codigo()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.accept)

class ventanaconfirmareliminar(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_confirmar_eliminar()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.accept)

class ventanaerroreliminar(QDialog):
    def __init__(self, mensaje):
        super().__init__()
        self.ui = Ui_Dialog_error_eliminar()
        self.ui.setupUi(self)
        self.ui.label.setText(mensaje)
        self.ui.pushButton.clicked.connect(self.close)

class VentanaBusquedaProductoVentas(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_busqueda_producto_ventas()
        self.ui.setupUi(self)

        self.ui.busqueda_emerguente.textChanged.connect(self.filtrar_productos)
        self.ui.tabla_producto_trabajo.doubleClicked.connect(self.seleccionar_producto)
        self.ui.cantidad_producto_trabajo.clicked.connect(self.seleccionar_producto)

        self.producto_seleccionado = None
        self.modelo = QStandardItemModel()
        self.ui.tabla_producto_trabajo.setModel(self.modelo)

        self.modelo.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Precio"])
        self.cargar_todos_los_productos()

    def cargar_todos_los_productos(self):
        productos = db.obtener_productos()
        self.modelo.clear()
        self.modelo.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Precio"])

        for fila in productos:
            items = [
                QStandardItem(str(fila[0])),  # ID
                QStandardItem(fila[1]),       # Código
                QStandardItem(fila[2]),       # Nombre
                QStandardItem(str(fila[7])),  # Precio
            ]
            for item in items:
                item.setEditable(False)
            self.modelo.appendRow(items)

        self.ui.tabla_producto_trabajo.resizeColumnsToContents()

    def filtrar_productos(self):
        texto = self.ui.busqueda_emerguente.text().strip()
        productos = db.buscar_productos(texto)
        self.modelo.clear()
        self.modelo.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Precio"])

        for fila in productos:
            items = [
                QStandardItem(str(fila[0])),
                QStandardItem(fila[1]),
                QStandardItem(fila[2]),
                QStandardItem(str(fila[7])),
            ]
            for item in items:
                item.setEditable(False)
            self.modelo.appendRow(items)

        self.ui.tabla_producto_trabajo.resizeColumnsToContents()

    def seleccionar_producto(self):
        index = self.ui.tabla_producto_trabajo.currentIndex()
        if not index.isValid():
            return

        fila = index.row()
        modelo = self.ui.tabla_producto_trabajo.model()

        try:
            cantidad = int(self.ui.lineEdit.text())
        except ValueError:
            cantidad = 1  # Valor por defecto si no se ingresa nada

        self.producto_seleccionado = {
            "id": int(modelo.item(fila, 0).text()),
            "codigo": modelo.item(fila, 1).text(),
            "nombre": modelo.item(fila, 2).text(),
            "precio": float(modelo.item(fila, 3).text()),
            "cantidad": cantidad
        }

        self.accept()

class Ui_detalleventas(QDialog):
    def __init__(self, datos_venta, parent=None):
        super().__init__(parent)
        self.ui = Ui_detalle_ventas()
        self.ui.setupUi(self)
        self.ventanaapp = parent

        # Labels
        self.ui.lineEdit_cliente_detalle.setText(datos_venta["cliente"])
        self.ui.lineEdit_fecha_detalle.setText(str(datos_venta["fecha"]))
        self.ui.label_total_detalle.setText(f"${datos_venta['total']:.2f}")
        self.ui.label_forma_detalle.setText(datos_venta["forma_pago"])

        # Crear modelo para QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio", "Subtotal"])

        for prod in datos_venta["productos"]:
            fila = [
                QStandardItem(str(prod[0])),
                QStandardItem(str(prod[1])),
                QStandardItem(str(prod[2])),
                QStandardItem(str(prod[3]))
            ]
            model.appendRow(fila)

        self.ui.tableView_detalle.setModel(model)

        # Conectar botón
        self.ui.pushButton.clicked.connect(self.ejecutar_acciones_A)

    def ejecutar_acciones_A(self):
        if self.ventanaapp:
            self.ventanaapp.actualizar_tabla_ventas()
        self.close()

class VentanaEditarTurno(QDialog):
        def __init__(self):
            super().__init__()
            self.ui = ui_editarturno()
            self.ui.setupUi(self)  # 👉 Aquí self es un QDialog válido con objectName()

            self.ui.boton_guardar_turno.clicked.connect(self.aceptar_edicion)

        def aceptar_edicion(self):
            self.accept()  # Esto cierra el QDialog con resultado "aceptado"

        def obtener_datos_actualizados(self):
            nombre = self.ui.cliente_turno.text()		
            patente = self.ui.patente_turno.text()
            fecha = self.ui.fecha_turno.date().toPython()
            hora = self.ui.hora_turno.time().toString("HH:mm")
            telefono = self.ui.telefono_turno.text()
            trabajo = self.ui.Trabajo_realizar_turno.toPlainText()
            fecha_original = fecha
            # Si es string
            fecha_formateada = fecha_original.strftime("%d/%m/%Y")

            fecha_str = f"{fecha.day}/{fecha.month}/{fecha.year}"  # Para coincidir con tu base        
            return (nombre, patente, fecha_formateada, hora, telefono, trabajo)

class VentanaTrabajoRealizado(QDialog):

    def __init__(self, datos_turno, id_turno):
        super().__init__()
        self.ui = ui_turno_realizado()
        self.ui.setupUi(self)
        self.id_turno = id_turno

        

        self.cargar_datos(datos_turno)
        self.actualizar_reloj()
        self.ui.boton_buscar_turno_trabajo.clicked.connect(self.abrir_busqueda_producto)
        self.ui.boton_eliminar_turno_trabajo.clicked.connect(self.eliminar_producto_tabla)
        self.ui.boton_guardar_turno_trabajo_.clicked.connect(self.guardar_trabajo_turno)
        self.ui.boton_cancela_turno_trabajo.clicked.connect(self.salir_turno_trabajo)

    def cargar_datos(self, datos):
        fecha = datos[3]  # Suponiendo que es un objeto datetime.date


        self.ui.cliente_turno_trabajo.setText(datos[1])
        self.ui.patente_turno_trabajo.setText(datos[2])
        self.ui.fecha_turno_trabajo.setText(fecha.strftime("%d/%m/%Y"))
        self.ui.telefono_turno_trabajo.setText(datos[5])
        self.ui.trabajo_turno_trabajo.setText(datos[6])

    def abrir_busqueda_producto(self, ventana=None):
        ventana = VentanaBusquedaProductoVentas()

        if ventana.exec() == QDialog.Accepted:
            producto = ventana.producto_seleccionado
            print(producto)
            if producto:
                self.agregar_producto_a_tabla(producto)

    def agregar_producto_a_tabla(self, producto):
        if producto is None:
            ventana_error = ventanaconfirmareliminar(mensaje="No se seleccionó ningún producto.")
            ventana_error.exec()
            return

        print(producto)
        self.ui.tabla_productos_turno_trabajo.setColumnCount(4)
        self.ui.tabla_productos_turno_trabajo.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Cantidad"])
        codigo = producto["codigo"]
        nombre = producto["nombre"]
        cantidad = str(producto["cantidad"])
        producto_id = db.buscar_id_producto_trabajo(codigo)

        tabla = self.ui.tabla_productos_turno_trabajo
        fila = tabla.rowCount()
        tabla.insertRow(fila)

        # Crear y alinear cada celda
        item_id = QTableWidgetItem(str(producto_id))
        item_id.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 0, item_id)

        item_codigo = QTableWidgetItem(codigo)
        item_codigo.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 1, item_codigo)

        item_nombre = QTableWidgetItem(nombre)
        tabla.setItem(fila, 2, item_nombre)

        item_cantidad = QTableWidgetItem(cantidad)
        item_cantidad.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 3, item_cantidad)

    def eliminar_producto_tabla(self):
        fila = self.ui.tabla_productos_turno_trabajo.currentRow()
        self.ui.tabla_productos_turno_trabajo.removeRow(fila)

    def actualizar_reloj(self):
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ui.fecha_turno_trabajo.setText(ahora)

    def guardar_trabajo_turno(self):
        # Obtener datos del formulario
        fecha = date.today()
        fecha_str = f"{fecha.day}/{fecha.month}/{fecha.year}"
        cliente = self.ui.cliente_turno_trabajo.text()
        patente = self.ui.patente_turno_trabajo.text()
        telefono = self.ui.telefono_turno_trabajo.text()
        kilometros = self.ui.klilometros_turno_trabajo.text()
        trabajo_realizado = self.ui.trabajo_turno_trabajo.text()
        precio = self.ui.precio_turno_trabajo.text()
        forma_pago= self.ui.forma_pago__turno_trabajo.currentText()
        modelo = self.ui.tabla_productos_turno_trabajo.model()
        


        # Validación básica
        if not cliente or not trabajo_realizado or not precio:
            ventana = Ventanaerrorcampovacio(mensaje="Complete al menos Cliente, trabajo realizado y precio para guardar.")
            ventana.exec()
            return
        productos_usados = []
        tabla = self.ui.tabla_productos_turno_trabajo

        if tabla.rowCount() > 0:
            for fila in range(tabla.rowCount()):
                item_id = tabla.item(fila, 0)
                item_cantidad = tabla.item(fila, 3)

                if item_id and item_cantidad:
                    try:
                        producto_id = int(item_id.text())
                        cantidad = int(item_cantidad.text())
                        print(f"Producto ID: {producto_id}, Cantidad: {cantidad}")

                        productos_usados.append({
                            "producto_id": producto_id,
                            "cantidad": cantidad,
                        })
                    except ValueError:
                        print(f"⚠️ Error de conversión en fila {fila}")
            # Llamar a la función de base de datos
        exito = db.guardar_trabajo(fecha_str, cliente, patente, kilometros, telefono, trabajo_realizado, precio, productos_usados, forma_pago)
        self.borrar_turno_trabajado(self.id_turno)

        if exito:
            ventana = Ventanaerrorcampovacio(mensaje="El trabajo fue registrado correctamente.")
            ventana.exec()
        
            self.limpiar_campos_turno_trabajo()
            self.limpiar_tabla(self.ui.tabla_productos_turno_trabajo)
            #ventana.actualizar_tabla_trabajo()
            self.close()
        else:
            ventana = Ventanaerrorcampovacio(mensaje="No se pudo guardar el trabajo ")
            ventana.exec()
        
    def limpiar_campos_turno_trabajo(self):
        self.ui.cliente_turno_trabajo.clear()
        self.ui.patente_turno_trabajo.clear()
        self.ui.telefono_turno_trabajo.clear()
        self.ui.precio_turno_trabajo.clear()
        self.ui.klilometros_turno_trabajo.clear()
        self.ui.trabajo_turno_trabajo.clear()
        self.ui.forma_pago__turno_trabajo.setMaxCount(0)

    def limpiar_tabla(self, tabla):
        modelo = tabla.model()
        if modelo:
            modelo.removeRows(0, modelo.rowCount())

    def borrar_turno_trabajado(self, id_turno):

        db.eliminar_turno_en_db(id_turno)
        ventana = Ventanaerrorcampovacio(mensaje="Turno Eliminado")
        ventana.exec()
        return
    
    def salir_turno_trabajo(self):
        self.close()

class Ui_detalle_trabajo(QDialog):
	def __init__(self, datos_trabajo, parent=None):
		super().__init__(parent)
		self.ui = Ui_detalletrabajo()  # tu clase de Qt Designer
		self.ui.setupUi(self)
		self.ventanaapp = parent  # ← ahora sí apunta al main real


		# Labels
		print(datos_trabajo)
		id_trabajo = datos_trabajo["id"]
		self.ui.label_2.setText(str(datos_trabajo["fecha"]))
		self.ui.lineEdit.setText(datos_trabajo["cliente"])
		self.ui.lineEdit_2.setText(datos_trabajo["patente"])
		self.ui.lineEdit_3.setText(datos_trabajo["telefono"])
		self.ui.lineEdit_4.setText(datos_trabajo["kilometros"])
		self.ui.lineEdit_5.setText(datos_trabajo["trabajo_realizar"])
		self.ui.label_11.setText(f"{datos_trabajo['precio']:.2f}")
		self.ui.label_12.setCurrentText(datos_trabajo["forma_pago"])




		# Crear modelo para QTableView
		model = QStandardItemModel()
		model.setHorizontalHeaderLabels(["ID","Producto", "Cantidad"])

		for productos in datos_trabajo["productos"]:
			print(productos)
			fila = [
				QStandardItem(str(productos[0])),  # Id
				QStandardItem(str(productos[1])),  # Producto
				QStandardItem(str(productos[2])),  # Cantidad
			]
			model.appendRow(fila)
		def editar_trabajo():
			id_trabajo = datos_trabajo["id"]
			cliente = self.ui.lineEdit.text()
			patente = self.ui.lineEdit_2.text()
			telefono = self.ui.lineEdit_3.text()
			kilometros = self.ui.lineEdit_4.text()
			trabajo_realizado = self.ui.lineEdit_5.text()
			precio = self.ui.label_11.text()
			forma_pago = self.ui.label_12.currentText()  # si es QComboBox

			# Validar campos obligatorios
			if not cliente or not precio:
				ventana = Ventanaerrorcampovacio(mensaje="Campo obligatorio en blanco")
				ventana.exec()
				return

			# Llamar a la función de base de datos que **no toca productos**
			db.actualizar_trabajo(
				id_trabajo,
				cliente,
				patente,
				kilometros,
				telefono,
				trabajo_realizado,
				precio,
				forma_pago
			)
		def ejecutar_acciones():
			editar_trabajo()
			if self.ventanaapp:
				self.ventanaapp.actualizar_tabla_trabajo()
			self.accept()


		self.ui.pushButton_2.clicked.connect(ejecutar_acciones)


		self.ui.tableView.setModel(model)
		self.ui.pushButton.clicked.connect(self.accept)

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        #db.crear_base_datos()  # crea tablas si no existen
        #db.borrar_turnos_vencidos()  # tu función actual
        #db.sincronizar_todo()  # sincroniza la base local con Supabase
        #eliminar barra y de titulo - opacidad
        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # mover ventana
        #acceder a las paginas
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio)  # Muestra la página de inicio
        self.ui.btn_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))			
        self.ui.btn_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_productos))
        self.ui.btn_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ventas))
        self.ui.btn_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_turnos))
        self.ui.btn_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_trabajos))
        self.ui.btn_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_configuracion))

        self.iniciar_reloj()
        self.actualizar_reloj()
        self.set_fecha_actual()
        self.set_fechas_reportes()
        self.ui.whatsapp_2.clicked.connect(self.abrir_whatsapp)
        self.ui.instagram_2.clicked.connect(self.abrir_instagram)


        #### botones productos

        self.ui.boton_crear_producto.clicked.connect(self.guardar_producto)
        self.actualizar_tabla()
        self.ui.tabla_producto.doubleClicked.connect(self.cargar_producto_para_editar)
        self.ui.boton_borrar_producto.clicked.connect(self.eliminar_producto_confirmado)
        self.ui.boton_editar_producto.clicked.connect(self.editar_producto)	
        self.ui.buscador_producto.textChanged.connect(self.filtrar_productos)



        ##Botones ventas
        self.actualizar_tabla_ventas()
        self.ui.boton_buscar_venta.clicked.connect(self.abrir_busqueda_producto_ventas)
        self.ui.boton_agregar_venta.clicked.connect(self.agregar_producto_a_tabla)
        self.ui.boton_eliminar_venta.clicked.connect(self.eliminar_producto_seleccionado)
        self.ui.boton_registrar_ventas.clicked.connect(self.guardar_venta)
        self.ui.tabla_registro_venta.doubleClicked.connect(self.mostrar_detalle_venta)
        self.ui.fecha_desde_venta.dateChanged.connect(self.filtrar_ventas_por_rango)
        self.ui.fecha_hasta_venta.dateChanged.connect(self.filtrar_ventas_por_rango)



        ##Botones turnos
        self.cargar_turnos_del_dia_en_inicio()
        self.iniciar_actualizacion_automatica()
        self.ui.boton_guardar_turno.clicked.connect(self.guardar_turnos)
        self.actualizar_tabla_turnos()
        self.ui.calendario_turno.clicked.connect(self.filtrar_turno_fecha)
        self.ui.boton_borrar_turno.clicked.connect(self.borrar_turno_seleccionado)
        self.ui.boton_realizado_turno.clicked.connect(self.abrir_ventana_trabajo)
        self.ui.boton_editar_turno.clicked.connect(self.editar_turno_ventana)



        ##Botones Trabajo
        self.actualizar_tabla_trabajo()
        self.ui.guardar_trabajo.clicked.connect(self.guardar_trabajo)
        self.ui.buscar_listatrabajo.textChanged.connect(self.filtrar_trabajo)
        self.ui.tableWidget_3.doubleClicked.connect(self.mostrar_detalle_trabajo)
        self.ui.btn_buscar_producto_trabajo.clicked.connect(self.abrir_busqueda_producto)
        self.ui.btn_eliminar_producto_trabajo.clicked.connect(self.eliminar_producto_tabla)
        


        ##botones configuracion 
        self.ui.combox_reporte.currentTextChanged.connect(self.mostrar_reporte)
        self.ui.fecha_desde_reporte.dateChanged.connect(self.mostrar_reporte_fecha)
        self.ui.fecha_hasta_reposrte.dateChanged.connect(self.mostrar_reporte_fecha)






        









###############################################################################
		#funciones prinicpales
##################################################################################


    def iniciar_reloj(self):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.actualizar_reloj)
            self.timer.start(1000)  # cada 1000 ms = 1 segundo

    def actualizar_reloj(self):
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        ahora1 = datetime.now().strftime("%d/%m/%Y")
        self.ui.fecha_inicio.setText(ahora)
        self.ui.label_fecha_trabajo.setText(ahora)
        self.ui.Fecha_ventas.setText(ahora1)
        
    def set_fecha_actual(self):
        hoy = QDate.currentDate()
        self.ui.fecha_turno.setDate(hoy)
        self.ui.hora_turno.setTime(QtCore.QTime.currentTime())

    def set_fechas_reportes(self):
        hoy = QDate.currentDate()

    # Primer día del mes actual
        primer_dia_mes = QDate(hoy.year(), hoy.month(), 1)

    # Setear en los QDateEdit de tu interfaz
        self.ui.fecha_desde_reporte.setDate(primer_dia_mes)
        self.ui.fecha_hasta_reposrte.setDate(hoy)
        self.ui.fecha_hasta_venta.setDate(hoy)
        self.ui.fecha_desde_venta.setDate(primer_dia_mes)

    def abrir_whatsapp(self):
        numero = "543516966161"  # <- reemplazá con el número (formato internacional sin + ni 0)
        mensaje = "Hola GDomininiWebs...."  
        url = f"https://wa.me/{numero}?text={mensaje}"
        webbrowser.open(url)

    def abrir_instagram(self):
        url = "https://www.instagram.com/gdomininiwebs/"  # ← poné el link de tu Instagram
        webbrowser.open(url)


###############################################################################
		#funciones inicio
##################################################################################





###############################################################################
		#funciones productos
##################################################################################

    def guardar_producto(self):
        codigo = self.ui.codigo_producto.text().strip()
        precio = self.ui.precio_producto_2.text().strip()
        nombre = self.ui.nombre_producto.text().strip()
        if not codigo or not nombre or not precio:
            ventana = Ventanaerrorcampovacio(mensaje="Rellene campos obligatorios (codigo, nombre, precio)")
            ventana.exec()
            return

        if db.codigo_existe(codigo):
            ventana = VentanaErrormismocodigo()
            ventana.exec()
            return

        # continuar con el guardado si no existe
        nombre = self.ui.nombre_producto.text()
        descripcion = self.ui.descripcion_producto.text()
        precio = float(self.ui.precio_producto_2.text())
        stock = int(self.ui.stock_producto.text()) if self.ui.stock_producto.text() else None
        categoria_id = self.ui.categoria_producto.text()
        proveedor_id = self.ui.precio_producto.text()

        db.agregar_producto(codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id)
        self.actualizar_tabla()
        self.ui.codigo_producto.clear()
        self.ui.nombre_producto.clear()
        self.ui.descripcion_producto.clear()
        self.ui.precio_producto.clear()
        self.ui.stock_producto.clear()
        self.ui.categoria_producto.clear()
        self.ui.precio_producto_2.clear()
        
    def actualizar_tabla(self):
        productos = db.obtener_productos()  # lista de tu base de datos

        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Descripción", "Categoría", "Stock", "Proveedor", "Precio"])

        for fila in productos:
            items = [QStandardItem(str(dato)) for dato in fila]
            modelo.appendRow(items)

        self.ui.tabla_producto.setModel(modelo)

    def editar_producto(self):
        index = self.ui.tabla_producto.currentIndex()
        
        codigo = self.ui.codigo_producto.text()
        if not codigo:
            ventana = Ventanaerrorcampovacio(mensaje="seleccione un producto para editar")
            ventana.exec()
            return
        nombre = self.ui.nombre_producto.text()
        descripcion = self.ui.descripcion_producto.text()
        precio = float(self.ui.precio_producto_2.text())
        stock = self.ui.stock_producto.text()
        categoria_id = self.ui.categoria_producto.text()
        proveedor_id = self.ui.precio_producto.text()
        

        db.actualizar_producto(codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id)
        self.ui.codigo_producto.clear()
        self.ui.nombre_producto.clear()
        self.ui.descripcion_producto.clear()
        self.ui.precio_producto.clear()
        self.ui.stock_producto.clear()
        self.ui.categoria_producto.clear()
        self.ui.precio_producto_2.clear()
        self.actualizar_tabla()

    def cargar_producto_para_editar(self, index):
        fila = index.row()
        modelo = self.ui.tabla_producto.model()

        id_producto      = modelo.item(fila, 0).text()
        codigo           = modelo.item(fila, 1).text()
        nombre           = modelo.item(fila, 2).text()
        descripcion      = modelo.item(fila, 3).text()
        precio           = modelo.item(fila, 7).text()
        stock            = modelo.item(fila, 5).text()
        categoria_id     = modelo.item(fila, 4).text()
        proveedor_id     = modelo.item(fila, 6).text()  # ✅ Este es el correcto

        self.ui.codigo_producto.setText(codigo)
        self.ui.nombre_producto.setText(nombre)
        self.ui.descripcion_producto.setText(descripcion)
        self.ui.precio_producto_2.setText(precio)
        self.ui.stock_producto.setText(stock)
        self.ui.categoria_producto.setText(categoria_id)
        self.ui.precio_producto.setText(proveedor_id)

        self.id_producto_actual = int(id_producto)

    def eliminar_producto_confirmado(self, fila):
        codigo = self.ui.codigo_producto.text()
        if not codigo:
            ventana = Ventanaerrorcampovacio(mensaje="seleccione un producto para eliminar")
            ventana.exec()
            return
        dialogo = ventanaconfirmareliminar()
        if dialogo.exec() == QDialog.Accepted:
            index = self.ui.tabla_producto.model().index(fila, 0)
            id_producto = int(self.ui.tabla_producto.model().data(index))
            


            if db.producto_tiene_relaciones(id_producto):
                dialogo = ventanaerroreliminar(mensaje="Producto cargado en ventas o trabajos")
                dialogo.exec()
                self.ui.codigo_producto.clear()
                self.ui.nombre_producto.clear()
                self.ui.descripcion_producto.clear()
                self.ui.precio_producto.clear()
                self.ui.stock_producto.clear()
                self.ui.categoria_producto.clear()
                self.ui.precio_producto_2.clear()
                self.actualizar_tabla()
                return

            else:
                db.eliminar_producto(id_producto)
                self.ui.codigo_producto.clear()
                self.ui.nombre_producto.clear()
                self.ui.descripcion_producto.clear()
                self.ui.precio_producto.clear()
                self.ui.stock_producto.clear()
                self.ui.categoria_producto.clear()
                self.ui.precio_producto_2.clear()
                self.actualizar_tabla()
        else:
            self.actualizar_tabla()
            return
        
    def eliminar_producto(self):
        fila = self.tabla_producto.currentRow()
        if fila >= 0:
            id_producto = int(self.tabla_producto.item(fila, 0).text())
            db.eliminar_producto(id_producto)
            self.actualizar_tabla()

    def filtrar_productos(self):
        texto = self.ui.buscador_producto.text().strip()
        productos = db.buscar_productos(texto)

        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels([
            "ID", "Código", "Nombre", "Descripción", "Precio", "Stock", "Categoría", "Proveedor"
        ])

        for fila in productos:
            items = [QStandardItem(str(dato) if dato is not None else "") for dato in fila]
            for item in items:
                item.setEditable(False)
            modelo.appendRow(items)

        self.ui.tabla_producto.setModel(modelo)
        self.ui.tabla_producto.resizeColumnsToContents()

    def actualizar_tabla(self):
            productos = db.obtener_productos()

            modelo = QStandardItemModel()
            modelo.setHorizontalHeaderLabels([
                "ID", "Código", "Nombre", "Descripción", "Categoria", "Stock", "Proveedor", "Precio"
            ])

            for fila in productos:
                items = [QStandardItem(str(dato) if dato is not None else "") for dato in fila]
                for item in items:
                    item.setEditable(False)
                modelo.appendRow(items)

            self.ui.tabla_producto.setModel(modelo)
            self.ui.tabla_producto.resizeColumnsToContents()



###############################################################################
		#funciones ventas
##################################################################################



    def limpiar_campos_venta(self):
        self.ui.Cliente_ventas.clear()
        self.ui.combox_forma_pago_venta.setCurrentIndex(0)
        self.ui.tableWidget.setRowCount(0)
        self.ui.lebel_total_venta.setText("$0.00")

    def abrir_busqueda_producto_ventas(self):
        ventana = VentanaBusquedaProductoVentas()
        

        if ventana.exec() == QDialog.Accepted:
            producto = ventana.producto_seleccionado
            if producto:
                item = QTableWidgetItem(str(producto["codigo"]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.tableWidget.setItem(0, 0, item)
                self.ui.codigo_venta.setText(producto["codigo"])
                self.ui.Product_ventas.setText(producto["nombre"])
                self.ui.precio_ventas.setText(str(producto["precio"]))
                self.ui.cantidad_ventas.setText(str(producto["cantidad"]))

    def agregar_producto_a_tabla(self):
        codigo   = self.ui.codigo_venta.text().strip()
        nombre   = self.ui.Product_ventas.text().strip()
        precio   = self.ui.precio_ventas.text().strip()
        cantidad = self.ui.cantidad_ventas.text().strip()

        # Validación de campos vacíos
        if not codigo or not nombre or not precio or not cantidad:
            ventana = ventanaerroreliminar(mensaje="Todos los campos del producto deben estar completos.")
            ventana.exec()
            return

        # Validación de tipos numéricos
        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            ventana = ventanaerroreliminar(mensaje="Precio o cantidad inválidos.")
            ventana.exec()
            return

        total = precio * cantidad

        # Validación de existencia del producto
        producto_id = db.buscar_id_producto(codigo)
        if producto_id is None:
            ventana = ventanaconfirmareliminar(mensaje="El código ingresado no corresponde a ningún producto.")
            ventana.exec()
            return

        # Inicializar columnas si es la primera vez
        if self.ui.tableWidget.columnCount() == 0:
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Código", "Nombre", "Precio", "Cantidad", "Total"])

        # Insertar nueva fila
        fila = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(fila)

        datos = [codigo, nombre, f"{precio:.2f}", str(cantidad), f"{total:.2f}"]
        for col, texto in enumerate(datos):
            item = QTableWidgetItem(texto)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(QFont("Segoe UI", 10))
            item.setForeground(QColor("#2c3e50"))  # Azul oscuro ServiFren
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(fila, col, item)

        # Actualizar total y limpiar campos
        self.limpiar_campos_producto()
        self.actualizar_total_venta()
        
    def eliminar_producto_seleccionado(self):
        fila = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(fila)
        self.actualizar_total_venta()

    def actualizar_total_venta(self):
        total = 0.0
        filas = self.ui.tableWidget.rowCount()

        for fila in range(filas):
            item = self.ui.tableWidget.item(fila, 4)  # columna "Total" (índice 4)
            if item:
                try:
                    total += float(item.text())
                except ValueError:
                    continue  # ignorar si el texto no es convertible

        self.ui.lebel_total_venta.setText(f"${total:.2f}")
        
    def limpiar_campos_producto(self):
        self.ui.codigo_venta.clear()
        self.ui.Product_ventas.clear()
        self.ui.precio_ventas.clear()
        self.ui.cantidad_ventas.clear()

    def guardar_venta(self):
        cliente = self.ui.Cliente_ventas.text().strip()
        forma_pago = self.ui.combox_forma_pago_venta.currentText()

        if not cliente or self.ui.tableWidget.rowCount() == 0:
            ventana = Ventanaerrorcampovacio(mensaje="Debe ingresar un cliente y al menos un producto.")
            ventana.exec()
            return

        productos = []

        for fila in range(self.ui.tableWidget.rowCount()):
            item_codigo  = self.ui.tableWidget.item(fila, 0)
            item_nombre  = self.ui.tableWidget.item(fila, 1)
            item_precio  = self.ui.tableWidget.item(fila, 2)
            item_cantidad = self.ui.tableWidget.item(fila, 3)

            if item_codigo and item_precio and item_cantidad:
                try:
                    codigo = item_codigo.text()
                    producto_id = db.buscar_id_producto(codigo)  # ← si el código no es el ID real
                    cantidad = int(item_cantidad.text())
                    precio = float(item_precio.text())

                    productos.append({
                        "producto_id": producto_id,
                        "cantidad": cantidad,
                        "precio": precio
                    })
                except ValueError:
                    continue  # ignorar si hay datos inválidos

        if not productos:
            ventana = Ventanaerrorcampovacio(mensaje="No se pudo procesar ningún producto válido.")
            ventana.exec()
            return

        db.guardar_venta(cliente, forma_pago, productos)

        # Limpiar interfaz
        self.ui.lebel_total_venta.setText("Total: $0")
        self.ui.tableWidget.setRowCount(0)
        self.ui.Cliente_ventas.clear()
        self.ui.combox_forma_pago_venta.setCurrentIndex(0)
        self.actualizar_tabla_ventas()

        ventana = Ventanaerrorcampovacio(mensaje="Venta registrada correctamente.")
        ventana.exec()

    def actualizar_tabla_ventas(self):
        ventas = db.obtener_ventas()  # lista de tu base de datos

        self.ui.tabla_registro_venta.setRowCount(0)
        self.ui.tabla_registro_venta.setColumnCount(5)
        self.ui.tabla_registro_venta.setHorizontalHeaderLabels(["ID", "Fecha", "Cliente", "Total", "Forma de pago"])

        for fila_index, venta in enumerate(ventas):
            self.ui.tabla_registro_venta.insertRow(fila_index)
            for col_index, dato in enumerate(venta):
                item = QTableWidgetItem(str(dato))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Segoe UI", 10))
                item.setForeground(QColor("#34495e"))  # Gris oscuro ServiFren
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.tabla_registro_venta.setItem(fila_index, col_index, item)

    def mostrar_ventas_en_tabla(self, ventas):
        self.ui.tabla_registro_ventas.setRowCount(0)
        for fila, venta in enumerate(ventas):
            self.ui.tabla_registro_ventas.insertRow(fila)
            for columna, dato in enumerate(venta):
                item = self.ui.tabla_registro_ventas(str(dato))
                self.ui.tabla_registro_ventas.setItem(fila, columna, item)

    def configurar_tabla_ventas(self):
        from PySide6.QtSql import QSqlDatabase, QSqlTableModel

        # Conexión a SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("servifren.db")
        if not self.db.open():
            print("Error al abrir la base de datos")
            return

        # Crear modelo
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("ventas")
        self.model.select()

        # Mostrar modelo en la tabla
        self.ui.tabla_registro_ventas.setModel(self.model)

    def mostrar_detalle_venta(self, index):
        # Validar que el index sea válido
        if not index.isValid():
            print("Index inválido: no hay celda seleccionada")
            return

        modelo = self.ui.tabla_registro_venta.model()
        if not modelo:
            print("No hay modelo asignado a la tabla")
            return

        fila = index.row()
        if fila < 0 or fila >= modelo.rowCount():
            print(f"Fila fuera de rango: {fila}")
            return

        # Obtener valor de la columna 0 (ID de la venta)
        index_id = modelo.index(fila, 0)
        id_venta = modelo.data(index_id)

        if not id_venta:
            print(f"No hay ID de venta en fila {fila}")
            return

        print("ID Venta:", id_venta)

        # Consultar detalles en la base de datos
        datos_venta = db.obtener_detalle_venta(id_venta)
        if not datos_venta:
            print(f"No se encontraron detalles para la venta {id_venta}")
            return

        dialogo = Ui_detalleventas(datos_venta, self)
        dialogo.exec()
        self.actualizar_tabla_ventas()

    def filtrar_ventas_por_rango(self):
        # Obtener fechas desde los QDateEdit
        fecha_inicio_qdate = self.ui.fecha_desde_venta.date()
        fecha_fin_qdate = self.ui.fecha_hasta_venta.date()

        # Convertir a datetime.date
        fecha_inicio = date(fecha_inicio_qdate.year(), fecha_inicio_qdate.month(), fecha_inicio_qdate.day())
        fecha_fin = date(fecha_fin_qdate.year(), fecha_fin_qdate.month(), fecha_fin_qdate.day())
        
        # Obtener ventas filtradas por rango
        ventas = db.obtener_ventas_por_rango(fecha_inicio, fecha_fin)
        
        # Actualizar la tabla en la UI
        self.actualizar_tabla_ventas1(ventas)

    def actualizar_tabla_ventas1(self, ventas):
        self.ui.tabla_registro_venta.setRowCount(0)
        self.ui.tabla_registro_venta.setColumnCount(5)
        self.ui.tabla_registro_venta.setHorizontalHeaderLabels(["ID", "Fecha", "Cliente", "Total", "Forma de pago"])

        for fila, turno in enumerate(ventas):
            self.ui.tabla_registro_venta.insertRow(fila)
            datos_visibles = [
                turno["id"],
                turno["fecha"],
                turno["cliente"],
                f"${turno['total']:.2f}",
                turno["forma_pago"]
            ]
            for columna, dato in enumerate(datos_visibles):
                item = QTableWidgetItem(str(dato))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Segoe UI", 10))
                item.setForeground(QColor("#34495e"))  # Gris oscuro ServiFren
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.tabla_registro_venta.setItem(fila, columna, item)

        self.ui.tabla_registro_venta.resizeColumnsToContents()




###############################################################################
		#funciones turnos
##################################################################################




    def guardar_turnos(self):
        cliente = self.ui.cliente_turno.text().strip()
        trabajo = self.ui.Trabajo_realizar_turno.toPlainText().strip()

        fecha_qdate = self.ui.fecha_turno.date()
        hora_qtime = self.ui.hora_turno.time()

        if not cliente or not trabajo:
            ventana = Ventanaerrorcampovacio(mensaje="Rellene campos obligatorios (cliente, fecha, trabajo)")
            ventana.exec()
            return

        # Convertir QDate y QTime a formatos compatibles
        fecha = date(fecha_qdate.year(), fecha_qdate.month(), fecha_qdate.day())
        hora = f"{hora_qtime.hour():02d}:{hora_qtime.minute():02d}"  # "HH:MM"

        patente = self.ui.patente_turno.text().strip()
        telefono = self.ui.telefono_turno.text().strip()

        db.agregar_turno(cliente, patente, fecha, hora, telefono, trabajo)

        # Limpiar campos
        self.ui.cliente_turno.clear()
        self.ui.fecha_turno.clear()
        self.ui.hora_turno.clear()
        self.ui.patente_turno.clear()
        self.ui.telefono_turno.clear()
        self.ui.Trabajo_realizar_turno.clear()
        
    # En actualizar_tabla_turnos
        self.actualizar_tabla_turnos()

    def actualizar_tabla_turnos(self):
        turnos = db.obtener_turnos()  # lista de tu base de datos

        self.ui.tabla_registro_turno.setRowCount(0)
        self.ui.tabla_registro_turno.setColumnCount(6)
        self.ui.tabla_registro_turno.setHorizontalHeaderLabels(["id","Nombre", "Patente", "Fecha", "Hora", "Telefono", "Trabajo"])

        for fila_index, turno in enumerate(turnos):
            self.ui.tabla_registro_turno.insertRow(fila_index)
            for col_index, dato in enumerate(turno):
                item = QTableWidgetItem(str(dato))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Segoe UI", 10))
                item.setForeground(QColor("#34495e"))  # Gris oscuro ServiFren
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.tabla_registro_turno.setItem(fila_index, col_index, item)

    def filtrar_turno_fecha(self):
        fecha = self.ui.calendario_turno.selectedDate().toString("yyyy-MM-dd")
        turno = db.obtener_turnos_por_fecha(fecha)

        self.actualizar_tabla_turnos1(turno)

    def actualizar_tabla_turnos1(self, turno):
        self.ui.tabla_registro_turno.setRowCount(0)
        self.ui.tabla_registro_turno.setColumnCount(6)
        self.ui.tabla_registro_turno.setHorizontalHeaderLabels(["ID","Nombre", "Patente", "Fecha", "Hora", "Telefono", "Trabajo"])

        for fila_index, turno in enumerate(turno):
            print(turno)
            self.ui.tabla_registro_turno.insertRow(fila_index)
            for col_index, dato in enumerate(turno):
                item = QTableWidgetItem(str(dato))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Segoe UI", 10))
                item.setForeground(QColor("#34495e"))  # Gris oscuro ServiFren
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.tabla_registro_turno.setItem(fila_index, col_index, item)

    def obtener_id_turno_seleccionado(self):
        fila = self.ui.tabla_registro_turno.currentRow()
        if fila == -1:
            return None  # Nada seleccionado

        item_id = self.ui.tabla_registro_turno.item(fila, 0)  # Columna 0 = ID
        if item_id:
            return item_id.text()
        return None

    def editar_turno_ventana(self):
        id_turno = self.obtener_id_turno_seleccionado()
        if not id_turno:
            ventana = Ventanaerrorcampovacio(mensaje="No se encontro ningun turno.")
            ventana.exec()
            return
        
        datos = db.obtener_datos_turno(id_turno)
        # Usar directamente los atributos de datetime.date
        fecha_obj = datos[3]  # datetime.date
        fecha_qdate = QDate(fecha_obj.year, fecha_obj.month, fecha_obj.day)

        # Suponiendo que datos[4] es string "HH:MM"
        Hora_str = datos[4]
        if isinstance(Hora_str, str):
            hora, minuto = map(int, Hora_str.split(":"))
        else:  # si es datetime.time
            hora = Hora_str.hour
            minuto = Hora_str.minute
        hora_qdate = QTime(hora, minuto)

        ventana = VentanaEditarTurno()
        ventana.ui.fecha_turno.setDate(fecha_qdate)
        ventana.ui.cliente_turno.setText(datos[1])
        ventana.ui.patente_turno.setText(datos[2])
        ventana.ui.hora_turno.setTime(hora_qdate)
        ventana.ui.telefono_turno.setText(datos[5])
        ventana.ui.Trabajo_realizar_turno.setText(datos[6])


        if ventana.exec():
            nuevos_datos = ventana.obtener_datos_actualizados()
            db.actualizar_turno_en_db(id_turno, nuevos_datos)
            self.filtrar_turno_fecha()  # Refrescar la tabla
            self.iniciar_actualizacion_automatica()

    def borrar_turno_seleccionado(self):
        id_turno = self.obtener_id_turno_seleccionado()
        if not id_turno:
            ventana = Ventanaerrorcampovacio(mensaje="Seleccioná un turno para borrar.")
            ventana.exec()
            return

        db.eliminar_turno_en_db(id_turno)
        self.filtrar_turno_fecha()
        ventana = Ventanaerrorcampovacio(mensaje="Turno Eliminado")
        ventana.exec()
        return

    def cargar_turnos_del_dia_en_inicio(self):
        fecha_actual = date.today()  # datetime.date
        
        # Obtener turnos de la base usando datetime.date
        turnos_hoy = db.obtener_turnos_por_fecha(fecha_actual)
        
        modelo = QStandardItemModel()
        modelo.setHorizontalHeaderLabels(["Cliente", "Fecha", "Hora", "Trabajo"])

        for fila, turno in enumerate(turnos_hoy):
            cliente = turno[1]
            fecha = turno[3]
            hora = turno[4]
            servicio = turno[6]
            datos_visibles = [cliente, fecha, hora, servicio]

            for columna, dato in enumerate(datos_visibles):
                item = QStandardItem(str(dato))
                modelo.setItem(fila, columna, item)

        self.ui.turnosinicio.setModel(modelo)
        self.ui.turnosinicio.resizeColumnsToContents()

    def iniciar_actualizacion_automatica(self):
        self.timer_actualizacion = QTimer(self)
        self.timer_actualizacion.timeout.connect(self.cargar_turnos_del_dia_en_inicio)
        self.timer_actualizacion.start(1000)  # 60,000 ms = 60 segundos

    def abrir_ventana_trabajo(self):
        id_turno = self.obtener_id_turno_seleccionado()
        if not id_turno:
            ventana = Ventanaerrorcampovacio(mensaje="Seleccioná un turno primero.")
            ventana.exec()

        datos = db.obtener_datos_turno(id_turno)

        ventana = VentanaTrabajoRealizado(datos, id_turno)
        ventana.exec()  # 👉 Esto abre la clase como ventana emergente
        self.filtrar_turno_fecha()


###############################################################################
		#funciones Trabajo
##################################################################################


    def abrir_busqueda_producto(self, ventana=None):
        ventana = VentanaBusquedaProductoVentas()

        if ventana.exec() == QDialog.Accepted:
            producto = ventana.producto_seleccionado
            print(producto)
            if producto:
                self.agregar_producto_a_tabla_trabajo(producto)

    def agregar_producto_a_tabla_trabajo(self, producto):
        if producto is None:
            ventana_error = ventanaconfirmareliminar(mensaje="No se seleccionó ningún producto.")
            ventana_error.exec()
            return

        print(producto)
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["ID", "Código", "Nombre", "Cantidad"])
        codigo = producto["codigo"]
        nombre = producto["nombre"]
        cantidad = str(producto["cantidad"])
        producto_id = db.buscar_id_producto_trabajo(codigo)

        tabla = self.ui.tableWidget_2
        fila = tabla.rowCount()
        tabla.insertRow(fila)

        # Crear y alinear cada celda
        item_id = QTableWidgetItem(str(producto_id))
        item_id.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 0, item_id)

        item_codigo = QTableWidgetItem(codigo)
        item_codigo.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 1, item_codigo)

        item_nombre = QTableWidgetItem(nombre)
        tabla.setItem(fila, 2, item_nombre)

        item_cantidad = QTableWidgetItem(cantidad)
        item_cantidad.setTextAlignment(Qt.AlignCenter)
        tabla.setItem(fila, 3, item_cantidad)

    def eliminar_producto_tabla(self):
        fila = self.ui.tableWidget_2.currentRow()
        self.ui.tableWidget_2.removeRow(fila)

    def guardar_trabajo(self):
        # Obtener datos del formulario
        fecha = date.today()
        fecha_str = f"{fecha.day}/{fecha.month}/{fecha.year}"
        cliente = self.ui.cliente_trabajo.text()
        patente = self.ui.patente_trabajo.text()
        telefono = self.ui.telefono_trabajo.text()
        kilometros = self.ui.kilometro_trabajo.text()
        trabajo_realizado = self.ui.realizado_trabajo.text()
        precio = self.ui.precio_trabajo.text()
        forma_pago= self.ui.forma_pago_trabajo.currentText()
        modelo = self.ui.tableWidget_2.model()
        


        # Validación básica
        if not cliente or not trabajo_realizado or not precio:
            ventana = Ventanaerrorcampovacio(mensaje="Complete al menos Cliente, trabajo realizado y precio para guardar.")
            ventana.exec()
            return
        productos_usados = []
        tabla = self.ui.tableWidget_2

        if tabla.rowCount() > 0:
            for fila in range(tabla.rowCount()):
                item_id = tabla.item(fila, 0)
                item_cantidad = tabla.item(fila, 3)

                if item_id and item_cantidad:
                    try:
                        producto_id = int(item_id.text())
                        cantidad = int(item_cantidad.text())
                        print(f"Producto ID: {producto_id}, Cantidad: {cantidad}")

                        productos_usados.append({
                            "producto_id": producto_id,
                            "cantidad": cantidad,
                        })
                    except ValueError:
                        print(f"⚠️ Error de conversión en fila {fila}")
            # Llamar a la función de base de datos
        exito = db.guardar_trabajo(fecha_str, cliente, patente, kilometros, telefono, trabajo_realizado, precio, productos_usados, forma_pago)


        if exito:
            ventana = Ventanaerrorcampovacio(mensaje="El trabajo fue registrado correctamente.")
            ventana.exec()
        
            self.limpiar_campos_trabajo()
            self.limpiar_tabla_trabajo(self.ui.tableWidget_2)
            self.actualizar_tabla_trabajo()
        else:
            ventana = Ventanaerrorcampovacio(mensaje="No se pudo guardar el trabajo ")
            ventana.exec()
        
    def limpiar_campos_trabajo(self):
        self.ui.cliente_trabajo.clear()
        self.ui.patente_trabajo.clear()
        self.ui.telefono_trabajo.clear()
        self.ui.precio_trabajo.clear()
        self.ui.kilometro_trabajo.clear()
        self.ui.realizado_trabajo.clear()
        self.ui.forma_pago_trabajo.setMaxCount(0)

    def limpiar_tabla_trabajo(self, tabla):
        modelo = tabla.model()
        if modelo:
            modelo.removeRows(0, modelo.rowCount())

    def actualizar_tabla_trabajo(self):
        ventas = db.obtener_trabajos()  # lista de tu base de datos

        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setColumnCount(9)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["ID", "Fecha", "Cliente", "Patente", "Kilometros", "Telefono", "Trabajo Realizado", "Precio", "Forma pago"])

        for fila_index, venta in enumerate(ventas):
            self.ui.tableWidget_3.insertRow(fila_index)
            for col_index, dato in enumerate(venta):
                item = QTableWidgetItem(str(dato))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("Segoe UI", 10))
                item.setForeground(QColor("#34495e"))  # Gris oscuro ServiFren
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.ui.tableWidget_3.setItem(fila_index, col_index, item)

    def mostrar_trabajo_en_tabla(self, trabajo):
        self.ui.tableWidget_3.setRowCount(0)
        for fila, venta in enumerate(trabajo):
            self.ui.tableWidget_3.insertRow(fila)
            for columna, dato in enumerate(venta):
                item = self.ui.tableWidget_3(str(dato))
                self.ui.tableWidget_3.setItem(fila, columna, item)

    def configurar_tabla_trabajo(self):
        from PySide6.QtSql import QSqlDatabase, QSqlTableModel

        # Conexión a SQLite
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("servifren.db")
        if not self.db.open():
            print("Error al abrir la base de datos")
            return

        # Crear modelo
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("trabajo")
        self.model.select()

        # Mostrar modelo en la tabla
        self.ui.tableWidget_3.setModel(self.model)

    def filtrar_trabajo(self):
        texto = self.ui.buscar_listatrabajo.text().strip()
        trabajo = db.buscar_trabajo(texto)

        tabla = self.ui.tableWidget_3
        tabla.setRowCount(0)
        tabla.setColumnCount(9)
        tabla.setHorizontalHeaderLabels([
            "ID", "Fecha", "Cliente", "Patente", "Kilometros",
            "Telefono", "Trabajo realizado", "Precio", "Forma de pago"
        ])

        for fila_index, fila_datos in enumerate(trabajo):
            tabla.insertRow(fila_index)
            for col_index, dato in enumerate(fila_datos):
                item = QTableWidgetItem(str(dato) if dato is not None else "")
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Opcional: hacer la celda no editable
                tabla.setItem(fila_index, col_index, item)

        tabla.resizeColumnsToContents()

    def mostrar_detalle_trabajo(self, index):
        valor1 = index.data()
        print("Contenido:", valor1)

        id_trabajo = valor1  # Asumiendo que el índice contiene el ID
        datos_trabajo = db.obtener_detalle_trabajo(id_trabajo)

        if datos_trabajo:
            dialogo = Ui_detalle_trabajo(datos_trabajo, self)
            dialogo.exec()



###############################################################################
		#funciones reportes
##################################################################################

    def mostrar_reporte(self, tipo):
        if tipo == "Productos Vendidos":
            datos = db.obtener_reporte_productos()
            headers = ["Producto", "Cantidad"]

        elif tipo == "Forma de pagos":
            datos = db.obtener_reporte_formas_pago()
            headers = ["Forma de pago", "Total"]

        elif tipo == "Trabajos realizados":
            datos = db.obtener_reporte_trabajos()
            headers = ["Resumen", "Valor"]

        elif tipo == "Ventas":
            datos = db.obtener_reporte_ventas()
            headers = ["Resumen", "Valor"]

        else:
            datos = []
            headers = []

        # Limpiar tabla
        self.ui.tabla_reporte.clear()
        self.ui.tabla_reporte.setRowCount(len(datos))
        self.ui.tabla_reporte.setColumnCount(len(headers))
        self.ui.tabla_reporte.setHorizontalHeaderLabels(headers)

        # Cargar filas
        for fila_idx, fila in enumerate(datos):
            for col_idx, dato in enumerate(fila):
                self.ui.tabla_reporte.setItem(fila_idx, col_idx, QTableWidgetItem(str(dato)))

    def mostrar_reporte_fecha(self, tipo):
        # Obtener rango de fechas desde los QDateEdit
        self.ui.combox_reporte.setCurrentIndex(0)
        fecha_inicio = self.ui.fecha_desde_reporte.date().toString("yyyy-MM-dd")
        fecha_fin = self.ui.fecha_hasta_reposrte.date().toString("yyyy-MM-dd")

        if tipo == "Productos Vendidos":
            datos = db.obtener_reporte_productos_fecha(fecha_inicio, fecha_fin)
            headers = ["Producto", "Cantidad"]

        elif tipo == "Forma de pagos":
            datos = db.obtener_reporte_formas_pago_fecha(fecha_inicio, fecha_fin)
            headers = ["Forma de pago", "Total"]

        elif tipo == "Trabajos realizados":
            datos = db.obtener_reporte_trabajos_fecha(fecha_inicio, fecha_fin)
            headers = ["Resumen", "Valor"]

        elif tipo == "Ventas":
            datos = db.obtener_reporte_ventas_fecha(fecha_inicio, fecha_fin)
            headers = ["Resumen", "Valor"]

        else:
            datos = []
            headers = []

        # Limpiar y preparar la tabla
        self.ui.tabla_reporte.clear()
        self.ui.tabla_reporte.setRowCount(len(datos))
        self.ui.tabla_reporte.setColumnCount(len(headers))
        self.ui.tabla_reporte.setHorizontalHeaderLabels(headers)

        # Llenar tabla con los datos
        for fila_idx, fila in enumerate(datos):
            for col_idx, dato in enumerate(fila):
                item = QTableWidgetItem(str(dato))
                self.ui.tabla_reporte.setItem(fila_idx, col_idx, item)

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec())	