import tkinter as tk
from tkinter import messagebox

import database


# ==========================================================
# CONFIGURACIÓN INICIAL
# ==========================================================

database.crear_tabla()


nota_seleccionada = None


# ==========================================================
# FUNCIONES
# ==========================================================

def limpiar_editor():
    global nota_seleccionada

    nota_seleccionada = None

    entrada_titulo.delete(0, tk.END)
    texto_contenido.delete("1.0", tk.END)

    etiqueta_fecha.config(
        text="Fecha de creación: --\nFecha de modificación: --"
    )


def crear_nota():
    titulo = entrada_titulo.get().strip()
    contenido = texto_contenido.get("1.0", tk.END).strip()

    if titulo == "":
        messagebox.showwarning(
            "Campo vacío",
            "Debes ingresar un título."
        )
        return

    if contenido == "":
        messagebox.showwarning(
            "Campo vacío",
            "Debes ingresar contenido para la nota."
        )
        return

    database.crear_nota(titulo, contenido)

    messagebox.showinfo(
        "Nota creada",
        "La nota se creó y se guardó correctamente."
    )

    limpiar_editor()
    mostrar_notas()


def seleccionar_nota(event=None):
    global nota_seleccionada

    seleccion = lista_notas.curselection()

    if not seleccion:
        return

    indice = seleccion[0]

    nota = notas_actuales[indice]

    nota_seleccionada = nota

    entrada_titulo.delete(0, tk.END)
    entrada_titulo.insert(0, nota[1])

    texto_contenido.delete("1.0", tk.END)
    texto_contenido.insert("1.0", nota[2])

    etiqueta_fecha.config(
        text=(
            f"Fecha de creación: {nota[4]}\n"
            f"Fecha de modificación: {nota[5]}"
        )
    )


def editar_nota():
    global nota_seleccionada

    if nota_seleccionada is None:
        messagebox.showwarning(
            "Sin selección",
            "Selecciona una nota para editar."
        )
        return

    titulo = entrada_titulo.get().strip()
    contenido = texto_contenido.get("1.0", tk.END).strip()

    if titulo == "" or contenido == "":
        messagebox.showwarning(
            "Campos vacíos",
            "El título y contenido son obligatorios."
        )
        return

    database.editar_nota(
        nota_seleccionada[0],
        titulo,
        contenido
    )

    messagebox.showinfo(
        "Nota actualizada",
        "La nota se actualizó correctamente."
    )

    limpiar_editor()
    mostrar_notas()


def eliminar_nota():
    global nota_seleccionada

    if nota_seleccionada is None:
        messagebox.showwarning(
            "Sin selección",
            "Selecciona una nota para eliminar."
        )
        return

    confirmar = messagebox.askyesno(
        "Eliminar nota",
        "¿Estás segura de que deseas eliminar esta nota?"
    )

    if not confirmar:
        return

    database.eliminar_nota(
        nota_seleccionada[0]
    )

    messagebox.showinfo(
        "Nota eliminada",
        "La nota se eliminó correctamente."
    )

    limpiar_editor()
    mostrar_notas()


def buscar_nota(event=None):
    texto = entrada_busqueda.get().strip()

    if texto == "":
        mostrar_notas()
        return

    cargar_lista(
        database.buscar_notas(texto)
    )


def mostrar_notas():
    cargar_lista(
        database.obtener_notas()
    )


def cargar_lista(notas):
    global notas_actuales

    notas_actuales = notas

    lista_notas.delete(0, tk.END)

    for nota in notas:
        id_nota = nota[0]
        titulo = nota[1]
        fijada = nota[3]

        if fijada == 1:
            texto = f"{titulo}"
        else:
            texto = f"{titulo}"

        lista_notas.insert(
            tk.END,
            texto
        )


def fijar_nota():
    global nota_seleccionada

    if nota_seleccionada is None:
        messagebox.showwarning(
            "Sin selección",
            "Selecciona una nota."
        )
        return

    estado_actual = nota_seleccionada[3]

    if estado_actual == 0:
        nuevo_estado = 1
        mensaje = "La nota se fijó correctamente."
    else:
        nuevo_estado = 0
        mensaje = "La nota dejó de estar fijada."

    database.cambiar_fijada(
        nota_seleccionada[0],
        nuevo_estado
    )

    messagebox.showinfo(
        "Nota",
        mensaje
    )

    limpiar_editor()
    mostrar_notas()


# ==========================================================
# VENTANA PRINCIPAL
# ==========================================================

ventana = tk.Tk()

ventana.title("Notes App")

ventana.geometry("1050x650")

ventana.minsize(
    900,
    550
)


# ==========================================================
# TÍTULO
# ==========================================================

titulo_principal = tk.Label(
    ventana,
    text="Notes App",
    font=("Arial", 26, "bold")
)

titulo_principal.pack(
    pady=15
)


# ==========================================================
# BUSCADOR
# ==========================================================

frame_busqueda = tk.Frame(
    ventana
)

frame_busqueda.pack(
    fill="x",
    padx=25,
    pady=5
)


etiqueta_busqueda = tk.Label(
    frame_busqueda,
    text="Buscar:",
    font=("Arial", 12)
)

etiqueta_busqueda.pack(
    side="left"
)


entrada_busqueda = tk.Entry(
    frame_busqueda,
    font=("Arial", 12)
)

entrada_busqueda.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10
)

entrada_busqueda.bind(
    "<KeyRelease>",
    buscar_nota
)


boton_mostrar = tk.Button(
    frame_busqueda,
    text="Mostrar todas",
    command=mostrar_notas
)

boton_mostrar.pack(
    side="right"
)


# ==========================================================
# CONTENEDOR PRINCIPAL
# ==========================================================

frame_principal = tk.Frame(
    ventana
)

frame_principal.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)


# ==========================================================
# PANEL IZQUIERDO - LISTA DE NOTAS
# ==========================================================

frame_lista = tk.LabelFrame(
    frame_principal,
    text="Mis notas",
    font=("Arial", 12, "bold")
)

frame_lista.pack(
    side="left",
    fill="both",
    expand=False,
    padx=(0, 10)
)


lista_notas = tk.Listbox(
    frame_lista,
    width=32,
    font=("Arial", 12)
)

lista_notas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

lista_notas.bind(
    "<<ListboxSelect>>",
    seleccionar_nota
)


# ==========================================================
# PANEL DERECHO - EDITOR
# ==========================================================

frame_editor = tk.LabelFrame(
    frame_principal,
    text="Editor de nota",
    font=("Arial", 12, "bold")
)

frame_editor.pack(
    side="right",
    fill="both",
    expand=True
)


# ==========================================================
# TÍTULO DE NOTA
# ==========================================================

etiqueta_titulo = tk.Label(
    frame_editor,
    text="Título:",
    font=("Arial", 12)
)

etiqueta_titulo.pack(
    anchor="w",
    padx=15,
    pady=(15, 5)
)


entrada_titulo = tk.Entry(
    frame_editor,
    font=("Arial", 13)
)

entrada_titulo.pack(
    fill="x",
    padx=15,
    pady=5
)


# ==========================================================
# CONTENIDO
# ==========================================================

etiqueta_contenido = tk.Label(
    frame_editor,
    text="Contenido:",
    font=("Arial", 12)
)

etiqueta_contenido.pack(
    anchor="w",
    padx=15,
    pady=(10, 5)
)


texto_contenido = tk.Text(
    frame_editor,
    font=("Arial", 12),
    height=12,
    wrap="word"
)

texto_contenido.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5
)


# ==========================================================
# FECHAS
# ==========================================================

etiqueta_fecha = tk.Label(
    frame_editor,
    text="Fecha de creación: --\nFecha de modificación: --",
    font=("Arial", 10),
    justify="left"
)

etiqueta_fecha.pack(
    anchor="w",
    padx=15,
    pady=10
)


# ==========================================================
# BOTONES
# ==========================================================

frame_botones = tk.Frame(
    frame_editor
)

frame_botones.pack(
    pady=15
)


boton_crear = tk.Button(
    frame_botones,
    text="Crear",
    width=12,
    command=crear_nota
)

boton_crear.grid(
    row=0,
    column=0,
    padx=5
)


boton_editar = tk.Button(
    frame_botones,
    text="Editar",
    width=12,
    command=editar_nota
)

boton_editar.grid(
    row=0,
    column=1,
    padx=5
)


boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    width=12,
    command=eliminar_nota
)

boton_eliminar.grid(
    row=0,
    column=2,
    padx=5
)


boton_fijar = tk.Button(
    frame_botones,
    text="Fijar",
    width=12,
    command=fijar_nota
)

boton_fijar.grid(
    row=0,
    column=3,
    padx=5
)


boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    width=12,
    command=limpiar_editor
)

boton_limpiar.grid(
    row=0,
    column=4,
    padx=5
)


# ==========================================================
# VARIABLES
# ==========================================================

notas_actuales = []


# ==========================================================
# CARGAR NOTAS AL INICIAR
# ==========================================================

mostrar_notas()


# ==========================================================
# EJECUTAR APLICACIÓN
# ==========================================================

ventana.mainloop()
