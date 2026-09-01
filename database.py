import sqlite3
from datetime import datetime


NOMBRE_BD = "notes.db"


def conectar():
    return sqlite3.connect(NOMBRE_BD)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fijada INTEGER DEFAULT 0,
            fecha_creacion TEXT NOT NULL,
            fecha_modificacion TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


# ==========================================================
# ISSUE #1 - CREAR UNA NOTA
# ==========================================================

def crear_nota(titulo, contenido):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO notas (
            titulo,
            contenido,
            fijada,
            fecha_creacion,
            fecha_modificacion
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        titulo,
        contenido,
        0,
        fecha,
        fecha
    ))

    conexion.commit()
    conexion.close()


# ==========================================================
# ISSUE #5 - MOSTRAR TODAS LAS NOTAS
# ==========================================================

def obtener_notas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            titulo,
            contenido,
            fijada,
            fecha_creacion,
            fecha_modificacion
        FROM notas
        ORDER BY fijada DESC, id DESC
    """)

    notas = cursor.fetchall()

    conexion.close()

    return notas


# ==========================================================
# ISSUE #2 - EDITAR UNA NOTA
# ==========================================================

def editar_nota(id_nota, titulo, contenido):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE notas
        SET
            titulo = ?,
            contenido = ?,
            fecha_modificacion = ?
        WHERE id = ?
    """, (
        titulo,
        contenido,
        fecha,
        id_nota
    ))

    conexion.commit()
    conexion.close()


# ==========================================================
# ISSUE #3 - ELIMINAR UNA NOTA
# ==========================================================

def eliminar_nota(id_nota):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM notas
        WHERE id = ?
    """, (id_nota,))

    conexion.commit()
    conexion.close()


# ==========================================================
# ISSUE #4 - BUSCAR UNA NOTA
# ==========================================================

def buscar_notas(texto):
    conexion = conectar()
    cursor = conexion.cursor()

    texto_busqueda = f"%{texto}%"

    cursor.execute("""
        SELECT
            id,
            titulo,
            contenido,
            fijada,
            fecha_creacion,
            fecha_modificacion
        FROM notas
        WHERE titulo LIKE ?
           OR contenido LIKE ?
        ORDER BY fijada DESC, id DESC
    """, (
        texto_busqueda,
        texto_busqueda
    ))

    notas = cursor.fetchall()

    conexion.close()

    return notas


# ==========================================================
# ISSUE #6 - FIJAR / DESFIJAR UNA NOTA
# ==========================================================

def cambiar_fijada(id_nota, estado):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE notas
        SET fijada = ?
        WHERE id = ?
    """, (
        estado,
        id_nota
    ))

    conexion.commit()
    conexion.close()


# ==========================================================
# ISSUE #7 - GUARDAR LAS NOTAS
# ==========================================================
# Las notas se guardan automáticamente en SQLite mediante
# crear_nota() y editar_nota().
#
# No es necesario un botón adicional para guardar cada nota.
# ==========================================================


# ==========================================================
# ISSUE #8 - FECHAS
# ==========================================================
# fecha_creacion se establece al crear la nota.
# fecha_modificacion se actualiza al editarla.
# ==========================================================
