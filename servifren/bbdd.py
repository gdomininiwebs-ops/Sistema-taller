import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, date

# Configuración de conexión a Supabase
DB_CONFIG = {

}
def get_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)

#------------------------------------------------
#productos--------------------------------------
#------------------------------------------------


def agregar_producto(codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id):
    # Convertir valores vacíos a None
    stock = int(stock) if stock not in (None, '') else None
    categoria_id = (categoria_id) if categoria_id not in (None, '') else None
    proveedor_id = (proveedor_id) if proveedor_id not in (None, '') else None

    descripcion = (descripcion) if descripcion not in (None, '') else None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id))
    conn.commit()
    conn.close()

def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in productos]

def actualizar_producto(codigo, nombre, descripcion, precio, stock, categoria_id, proveedor_id):
    stock = int(stock) if stock not in (None, '', 'None') else None
    categoria_id = (categoria_id) if categoria_id not in (None, '', 'None') else None
    proveedor_id = (proveedor_id) if proveedor_id not in (None, '', 'None') else None
    descripcion = descripcion if descripcion not in (None, '', 'None') else None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria_id=%s, proveedor_id=%s
        WHERE codigo=%s
    """, (nombre, descripcion, precio, stock, categoria_id, proveedor_id, codigo))
    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (id_producto,))
    conn.commit()
    conn.close()

def producto_tiene_relaciones(id_producto):
    print(id_producto)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as c FROM detalle_venta WHERE producto_id = %s", (id_producto,))
    ventas = cursor.fetchone()["c"]
    cursor.execute("SELECT COUNT(*) as c FROM detalle_trabajos WHERE producto_id = %s", (id_producto,))
    trabajos = cursor.fetchone()["c"]
    conn.close()
    print(f"Ventas: {ventas}, Trabajos: {trabajos}")

    return ventas > 0 or trabajos > 0

def codigo_existe(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as c FROM productos WHERE codigo = %s", (codigo,))
    existe = cursor.fetchone()["c"] > 0
    conn.close()
    return existe

def buscar_productos(texto):
    conn = get_connection()
    cursor = conn.cursor()
    texto = f"%{texto.lower()}%"
    cursor.execute("""
        SELECT * FROM productos
        WHERE LOWER(nombre) LIKE %s OR LOWER(codigo) LIKE %s
    """, (texto, texto))
    resultados = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in resultados]

def buscar_id_producto(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM productos WHERE codigo = %s", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado["id"] if resultado else None





#------------------------------------------------
#ventas--------------------------------------
#------------------------------------------------



def guardar_venta(cliente, forma_pago, productos):
    conn = get_connection()
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(p["cantidad"] * p["precio"] for p in productos)
    cursor.execute("""
        INSERT INTO ventas (fecha, cliente, total, forma_pago)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (fecha, cliente, total, forma_pago))
    venta_id = cursor.fetchone()["id"]
    for p in productos:
        cursor.execute("""
            INSERT INTO detalle_venta (venta_id, producto_id, cantidad, precio)
            VALUES (%s, %s, %s, %s)
        """, (venta_id, p["producto_id"], p["cantidad"], p["precio"]))
    conn.commit()
    conn.close()

def obtener_ventas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, total, forma_pago
        FROM ventas
        ORDER BY fecha DESC
    """)
    ventas = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in ventas]

def obtener_detalle_venta(id_venta):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, total, forma_pago
        FROM ventas WHERE id=%s
    """, (id_venta,))
    venta = cursor.fetchone()
    if not venta:
        conn.close()
        return None
    cursor.execute("""
        SELECT p.nombre, dv.cantidad, dv.precio, (dv.cantidad * dv.precio) as subtotal
        FROM detalle_venta dv
        JOIN productos p ON dv.producto_id = p.id
        WHERE dv.venta_id = %s
    """, (id_venta,))
    productos = cursor.fetchall()
    conn.close()
    return {
        "id": venta["id"],
        "fecha": venta["fecha"],
        "cliente": venta["cliente"],
        "total": venta["total"],
        "forma_pago": venta["forma_pago"],
        "productos": [tuple(r.values()) for r in productos]
    }

def obtener_ventas_por_rango(fecha_inicio, fecha_fin):
    conn = get_connection()  # <-- llamar a la función para obtener la conexión
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, total, forma_pago
        FROM ventas
        WHERE fecha::date BETWEEN %s AND %s
        ORDER BY fecha ASC
    """, (fecha_inicio, fecha_fin))
    ventas = cursor.fetchall()
    conn.close()
    return ventas






#------------------------------------------------
#turno--------------------------------------
#------------------------------------------------



def agregar_turno(nombre, patente, fecha, hora, telefono, trabajo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO turnos (nombre, patente, fecha, hora, telefono, trabajo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, patente, fecha, hora, telefono, trabajo))
    conn.commit()
    conn.close()

def obtener_datos_turno(id_turno):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turnos WHERE id = %s", (id_turno,))
    turno = cursor.fetchone()
    conn.close()
    return tuple(turno.values()) if turno else None

def actualizar_turno_en_db(id_turno, datos):
    try:
        nombre, patente, fecha_str, hora, telefono, trabajo = datos

        # Convertir la fecha al formato ISO
        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y").date()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE turnos
            SET nombre=%s, patente=%s, fecha=%s, hora=%s, telefono=%s, trabajo=%s
            WHERE id=%s
        """, (nombre, patente, fecha_obj, hora, telefono, trabajo, id_turno))
        conn.commit()
        conn.close()

        print(f"[OK] Turno actualizado correctamente para ID {id_turno}")

    except ValueError:
        print(f"[Error] Fecha inválida: '{fecha_str}'. Formato esperado: DD/MM/YYYY")
    except Exception as e:
        print(f"[Error] Falló la actualización del turno: {e}")

def eliminar_turno_en_db(id_turno):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM turnos WHERE id=%s", (id_turno,))
    conn.commit()
    conn.close()

def obtener_turnos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id,nombre, patente, fecha, hora, telefono, trabajo
        FROM turnos
        ORDER BY fecha DESC
    """)
    turnos = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in turnos]

def obtener_turnos_por_fecha(fecha):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id,nombre, patente, fecha, hora, telefono, trabajo
            FROM turnos
            WHERE fecha = %s
            ORDER BY hora ASC
        """, (fecha,))
        turno = cursor.fetchall()
        return [tuple(r.values()) for r in turno]
    finally:
        conn.close()






#------------------------------------------------
#trabajo--------------------------------------
#------------------------------------------------

def guardar_trabajo(fecha, cliente, patente, kilometros, telefono, trabajo_realizado, precio, productos_usados, forma_pago):
    try:
        # Convertir la fecha al formato ISO
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha.strip(), "%d/%m/%Y").date()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO trabajo (fecha, cliente, patente, kilometros, telefono, trabajo_realizar, precio, forma_pago)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (fecha, cliente, patente, kilometros, telefono, trabajo_realizado, precio, forma_pago))

        trabajo_id = cursor.fetchone()["id"]  # ✅ # Usar índice si no estás usando RealDictCursor

        for p in productos_usados:
            cursor.execute("""
                INSERT INTO detalle_trabajos (trabajo_id, producto_id, cantidad)
                VALUES (%s, %s, %s)
            """, (trabajo_id, p["producto_id"], p["cantidad"]))

        conn.commit()
        conn.close()
        print(f"[OK] Trabajo guardado correctamente con ID {trabajo_id}")
        return True

    except ValueError:
        print(f"[Error] Fecha inválida: '{fecha}'. Formato esperado: DD/MM/YYYY")
        
        return False

def actualizar_trabajo(id_trabajo,
				cliente,
				patente,
				kilometros,
				telefono,
				trabajo_realizado,
				precio,
				forma_pago
			):
    conn = None
    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE trabajo
            SET
                cliente = %s,
                patente = %s,
                kilometros = %s,
                telefono = %s,
                trabajo_realizar = %s,
                precio = %s,
                forma_pago = %s
            WHERE id = %s
        """, ( cliente, patente, kilometros, telefono, trabajo_realizado, precio, forma_pago, id_trabajo))

        conn.commit()
        print(f"[OK] Trabajo ID {id_trabajo} actualizado correctamente.")
        return True

    except ValueError:
        print(f"[Error] Fecha inválida: '{fecha_str}'. Formato esperado: DD/MM/YYYY")
        return False

    except Exception as e:
        print(f"[Error] Falló la actualización del trabajo: {e}")
        return False

    finally:
        if conn:
            conn.close()

def buscar_id_producto_trabajo(codigo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM productos WHERE codigo = %s", (codigo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado["id"] if resultado else None

def buscar_trabajo(texto):
    conn = get_connection()
    cursor = conn.cursor()
    texto = f"%{texto.lower()}%"
    cursor.execute("""
        SELECT * FROM trabajo
        WHERE LOWER(cliente) LIKE %s OR LOWER(patente) LIKE %s
    """, (texto, texto))
    resultados = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in resultados]

def obtener_trabajos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, patente, kilometros, telefono, trabajo_realizar, precio, forma_pago
        FROM trabajo ORDER BY fecha DESC
    """)
    trabajo = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in trabajo]

def obtener_detalle_trabajo(id_trabajo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, fecha, cliente, patente, kilometros, telefono, trabajo_realizar, precio, forma_pago
        FROM trabajo WHERE id = %s
    """, (id_trabajo,))
    trabajo = cursor.fetchone()
    if not trabajo:
        conn.close()
        return None
    cursor.execute("""
        SELECT p.id, p.nombre, dv.cantidad
        FROM detalle_trabajos dv
        JOIN productos p ON dv.producto_id = p.id
        WHERE dv.trabajo_id = %s
    """, (id_trabajo,))
    productos = cursor.fetchall()
    conn.close()
    return {
        "id": trabajo["id"],
        "fecha": trabajo["fecha"],
        "cliente": trabajo["cliente"],
        "patente": trabajo["patente"],
        "kilometros": trabajo["kilometros"],
        "telefono": trabajo["telefono"],
        "trabajo_realizar": trabajo["trabajo_realizar"],
        "precio": trabajo["precio"],
        "forma_pago": trabajo["forma_pago"],
        "productos": [tuple(r.values()) for r in productos]
    }



#------------------------------------------------
#reportes--------------------------------------
#------------------------------------------------

def obtener_reporte_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            p.nombre AS producto,
            SUM(COALESCE(dt.cantidad, 0) + COALESCE(dv.cantidad, 0)) AS total_usado_o_vendido
        FROM productos p
        LEFT JOIN detalle_trabajos dt ON p.id = dt.producto_id
        LEFT JOIN detalle_venta dv ON p.id = dv.producto_id
        GROUP BY p.nombre
        ORDER BY total_usado_o_vendido DESC
    """)
    datos = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in datos]

def obtener_reporte_formas_pago():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT forma_pago, SUM(total) AS total_pagado FROM ventas GROUP BY forma_pago")
    ventas = cursor.fetchall()
    cursor.execute("SELECT forma_pago, SUM(precio) AS total_pagado FROM trabajo GROUP BY forma_pago")
    trabajos = cursor.fetchall()
    conn.close()
    pagos = {}
    for forma, total in [(r["forma_pago"], r["total_pagado"]) for r in ventas + trabajos]:
        pagos[forma] = pagos.get(forma, 0) + total
    return [(forma, round(total, 2)) for forma, total in pagos.items()]

def obtener_reporte_trabajos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS cantidad_trabajos, SUM(precio) AS total_facturado FROM trabajo")
    resultado = cursor.fetchone()
    conn.close()
    return [("Cantidad de trabajos", resultado["cantidad_trabajos"]), ("Total facturado", round(resultado["total_facturado"], 2))]

def obtener_reporte_ventas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS cantidad_ventas, SUM(total) AS total_ventas FROM ventas")
    resultado = cursor.fetchone()
    conn.close()
    return [("Cantidad de ventas", resultado["cantidad_ventas"]), ("Total vendido", round(resultado["total_ventas"], 2))]


def obtener_reporte_productos_fecha(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            p.nombre AS producto,
            SUM(COALESCE(dt.cantidad, 0) + COALESCE(dv.cantidad, 0)) AS total_usado_o_vendido
        FROM productos p
        LEFT JOIN detalle_trabajos dt ON p.id = dt.producto_id
        LEFT JOIN detalle_venta dv ON p.id = dv.producto_id
        WHERE fecha::date BETWEEN %s AND %s
        GROUP BY p.nombre
        ORDER BY total_usado_o_vendido DESC
    """, (fecha_inicio, fecha_fin))
    datos = cursor.fetchall()
    conn.close()
    return [tuple(r.values()) for r in datos]

def obtener_reporte_formas_pago_fecha( fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT forma_pago, SUM(total) AS total_pagado FROM ventas WHERE fecha::date BETWEEN %s AND %s GROUP BY forma_pago",  (fecha_inicio, fecha_fin))
    ventas = cursor.fetchall()
    cursor.execute("SELECT forma_pago, SUM(precio) AS total_pagado FROM trabajo WHERE fecha::date BETWEEN %s AND %s GROUP BY forma_pago",  (fecha_inicio, fecha_fin))
    trabajos = cursor.fetchall()
    conn.close()
    pagos = {}
    for forma, total in [(r["forma_pago"], r["total_pagado"]) for r in ventas + trabajos]:
        pagos[forma] = pagos.get(forma, 0) + total
    return [(forma, round(total, 2)) for forma, total in pagos.items()]

def obtener_reporte_trabajos_fecha(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS cantidad_trabajos, SUM(precio) AS total_facturado FROM trabajo WHERE fecha::date BETWEEN %s AND %s",  (fecha_inicio, fecha_fin))
    resultado = cursor.fetchone()
    conn.close()
    return [("Cantidad de trabajos", resultado["cantidad_trabajos"]), ("Total facturado", round(resultado["total_facturado"], 2))]

def obtener_reporte_ventas_fecha(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) AS cantidad_ventas, SUM(total) AS total_ventas FROM ventas WHERE fecha::date BETWEEN %s AND %s",  (fecha_inicio, fecha_fin))
    resultado = cursor.fetchone()
    conn.close()
    return [("Cantidad de ventas", resultado["cantidad_ventas"]), ("Total vendido", round(resultado["total_ventas"], 2))]


