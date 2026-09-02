# Notes-App
Proyecto (Individual)

## Descripción del Proyecto
Notes App es una aplicación que permite al usuario crear, consultar, editar, eliminar y buscar notas de manera sencilla.

## Justificación del proyecto
Se eligió desarrollar una aplicación de notas porque es un proyecto sencillo, pero permite aplicar conceptos fundamentales de Ingeniería de Software, 
como historias de usuario, Issues, control de versiones, modelado y desarrollo incremental.

El proyecto permite organizar información de manera sencilla mediante
la creación, edición, eliminación, búsqueda y almacenamiento de notas.

Además, su alcance es adecuado para un desarrollo individual, ya que las funcionalidades pueden implementarse de manera progresiva
y relacionarse directamente con las historias de usuario definidas.

## User Stories
* Como usuario, quiero crear una nota para guardar información importante.

* Como usuario, quiero editar una nota para actualizar o corregir su información.

* Como usuario, quiero eliminar una nota para quitar información que ya no necesito.

* Como usuario, quiero buscar una nota por su título o contenido para encontrar rápidamente la información que necesito.

* Como usuario, quiero visualizar todas mis notas para consultar la información que tengo guardada.

* Como usuario, quiero fijar las notas importantes para tenerlas siempre visibles y acceder a ellas rápidamente.

* Como usuario, quiero guardar mis notas para conservar la información aunque cierre la aplicación.

* Como usuario, quiero visualizar la fecha de creación y modificación de cada nota para saber cuándo fue creada o actualizada.

## Metodología

## Metodología
Para el desarrollo del proyecto se utilizará una metodología ágil, debido a que el proyecto se desarrolla de manera incremental.

Las funcionalidades se organizarán mediante historias de usuario e Issues de GitHub. Cada funcionalidad será desarrollada, probada y registrada mediante commits relacionados con su Issue correspondiente.

El tablero Kanban permitirá visualizar el progreso de cada tarea mediante las columnas:

- **To Do:** tareas pendientes de realizar.
- **In Progress:** tareas que se encuentran en desarrollo.
- **Done:** tareas terminadas y verificadas.

## Arquitectura del proyecto
El proyecto está organizado en dos archivos principales:

```text
 Notes-App/
├── docs/
│   └── diagrama-flujo.png
├── database.py
├── main.py
├── README.md
├── RETROSPECTIVA.md
└── .gitignore                 
```

main.py

Contiene la interfaz gráfica de la aplicación desarrollada con Tkinter.

En este archivo se encuentran las funciones que permiten al usuario:

Crear notas.
Editar notas.
Eliminar notas.
Buscar notas.
Mostrar todas las notas.
Fijar y desfijar notas.
Limpiar los campos.
Visualizar la fecha de creación y modificación.
database.py

Contiene las funciones encargadas de administrar la información mediante SQLite.

Se utiliza para:

Crear la tabla de notas.
Guardar nuevas notas.
Consultar las notas existentes.
Editar notas.
Eliminar notas.
Buscar notas.
Cambiar el estado de una nota fijada.

La separación entre main.py y database.py permite separar la interfaz gráfica de las operaciones de almacenamiento de información.

<br>

<div align="center">

```mermaid
flowchart TD
    Inicio([Inicio]) --> Abrir[Abrir Notes App]
    Abrir --> Cargar[Mostrar interfaz principal y cargar notas]
    Cargar --> Op[/Seleccionar una opción/]

    Op --> C_Crear[Crear nota]
    Op --> C_Editar[Editar nota]
    Op --> C_Eliminar[Eliminar nota]
    Op --> C_Buscar[Buscar nota]
    Op --> C_Fijar[Fijar / Desfijar nota]
    Op --> C_Consultar[Consultar notas]

    C_Crear --> N1[Ingresar título y contenido]
    N1 --> N2[Guardar nota en SQLite fecha de creación]
    N2 --> N3[Mostrar mensaje de confirmación]

    C_Editar --> E1[Seleccionar nota]
    E1 --> E2[Modificar título o contenido]
    E2 --> E3[Actualizar en SQLite fecha de modificación]
    E3 --> E4[Mostrar mensaje de confirmación]

    C_Eliminar --> D1[Seleccionar nota]
    D1 --> D2[Confirmar eliminación]
    D2 --> D3[Eliminar de SQLite]
    D3 --> D4[Mostrar mensaje de confirmación]

    C_Buscar --> B1[Ingresar texto de búsqueda]
    B1 --> B2[Buscar en SQLite título o contenido]
    B2 --> B3[Mostrar resultados]

    C_Fijar --> F1[Seleccionar nota]
    F1 --> F2["Cambiar estado (Fijada = 1 / 0)"]
    F2 --> F3[Actualizar en SQLite]
    F3 --> F4[Mostrar mensaje de confirmación]

    C_Consultar --> Q1[Cargar todas las notas]
    Q1 --> Q2[Mostrar lista de notas ordenadas Fijadas primero]
    Q2 --> Q3[Visualizar fecha de creación y modificación]

    N3 --> Pregunta{¿Desea realizar otra acción?}
    E4 --> Pregunta
    D4 --> Pregunta
    B3 --> Pregunta
    F4 --> Pregunta
    Q3 --> Pregunta

    Pregunta -- Sí --> Op
    Pregunta -- No --> Fin([Fin])
```

</div>

<br>

## Instrucciones de ejecución

Para ejecutar el proyecto se necesita:

Python 3.
Visual Studio Code o cualquier otro editor de código compatible.
Tkinter.
SQLite.

SQLite se utiliza como sistema de almacenamiento local, por lo que no es necesario instalar un servidor de base de datos externo.

Ejecución
Clonar el repositorio:
git clone https://github.com/7ernandit-collab/Notes-App.git
Entrar a la carpeta:
cd Notes-App
Ejecutar el programa:
python main.py
La aplicación abrirá la interfaz gráfica de Notes App.

La base de datos se crea automáticamente al ejecutar el programa.

## Integrante:
→ Ana Fernanda Loera Mendoza - 7ernandit-collab
