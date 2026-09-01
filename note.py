class Nota:
    def __init__(
        self,
        id_nota,
        titulo,
        contenido,
        fijada,
        fecha_creacion,
        fecha_modificacion
    ):
        self.id = id_nota
        self.titulo = titulo
        self.contenido = contenido
        self.fijada = fijada
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
