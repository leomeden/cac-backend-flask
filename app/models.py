from app.database import get_db

class Trago:

    def __init__(self, id, codigo, nombre, instrucciones, vaso, imagen, alcohol, categoria):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.vaso = vaso
        self.imagen = imagen
        self.alcohol = alcohol
        self.categoria = categoria
        # self.activo = True

    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        # cursor.execute( "INSERT INTO tragos (codigo, nombre, instrucciones, vaso, imagen, alcohol, categoria) VALUES (%s, %s, %s, %s, %s, %s, %s)", ("prueba", "prueba", "prueba", "prueba", "prueba", "prueba", "prueba"))
        # self.id = cursor.lastrowid
        cursor.execute("""
                        INSERT INTO tragos (codigo, nombre, instrucciones, vaso, imagen, alcohol, categoria) VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (self.codigo, self.nombre, self.instrucciones, self.vaso, self.imagen, self.alcohol, self.categoria))
        self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def traerTragos():
        db = get_db()
        cursor = db.cursor()
        tragos = cursor.execute( "SELECT * FROM tragos")

        rows = cursor.fetchall()
        tragos = []
        for row in rows:
            tragos.append(Trago(id=row[0], codigo=row[1], nombre=row[2], instrucciones=row[3], vaso=row[4], imagen=row[5], alcohol=row[6], categoria=row[7]).serialize())

        # db.commit()
        cursor.close()    
        return tragos
    
    @staticmethod
    def traerTragoPorCodigo(codigo):
        # print(str(codigo))
        db = get_db()
        cursor = db.cursor()
        tragos = cursor.execute( "SELECT * FROM tragos WHERE codigo='" + str(codigo) + "'")

        row = cursor.fetchone()
        cursor.close()
        if row:
            # print(Trago(id=row[0], codigo=row[1], nombre=row[2], instrucciones=row[3], vaso=row[4], imagen=row[5], alcohol=row[6], categoria=row[7]).serialize())
            return Trago(id=row[0], codigo=row[1], nombre=row[2], instrucciones=row[3], vaso=row[4], imagen=row[5], alcohol=row[6], categoria=row[7]).serialize()
        return None    
    
    
    @staticmethod
    def eliminarTragoPorCodigo(codigo):
        # print(str(codigo))
        db = get_db()
        cursor = db.cursor()
        cursor.execute( "DELETE FROM tragos WHERE codigo='" + str(codigo) + "'")
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nombre': self.nombre,
            'instrucciones': self.instrucciones,
            'vaso': self.vaso,
            'imagen': self.imagen,
            'alcohol': self.alcohol,
            'categoria': self.categoria#,
            # 'activo': self.activo
        }