import sqlite3


class Database:
    @staticmethod
    def conn():
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists pasajeros (
                            ced integer primary key,
                            nombre text
                        )""")
        c.execute("""CREATE TABLE if not exists clases (
                                    ref integer primary key,
                                    clase text
                                )""")
        c.execute("""CREATE TABLE if not exists asignaciones (
                                    ubi integer primary key,
                                    ced integer,
                                    ref integer
                                )""")
        conn.commit()
        conn.close()
        print("BASE DE DATOS CONECTADA.")

    @staticmethod
    def agregar_pasajero(ced, nombre):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "INSERT INTO pasajeros VALUES (?, ?)"
        c.execute(query, (ced, nombre))
        conn.commit()
        conn.close()
        print("PASAJERO " + nombre + " AGREGADO.")

    @staticmethod
    def eliminar_pasajero(ced):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "DELETE FROM pasajeros WHERE ced=?"
        c.execute(query, (ced, ))
        conn.commit()
        conn.close()
        print(str(ced) + " ELIMINADO")


    @staticmethod
    def mostrar_pasajeros():
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "SELECT * FROM pasajeros"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def buscar_pasajero(ced):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "SELECT * FROM asignaciones WHERE ced=?"
        c.execute(query, (ced, ))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def agregar_clase(ref, clase):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "INSERT INTO clases VALUES (?, ?)"
        c.execute(query, (ref, clase))
        conn.commit()
        conn.close()
        print("CLASE " + clase + " AGREGADA.")

    @staticmethod
    def eliminar_clase(ref):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "DELETE FROM clases WHERE ref=?"
        c.execute(query, (ref, ))
        conn.commit()
        conn.close()
        print(str(ref) + " ELIMINADA")

    @staticmethod
    def mostrar_clases():
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "SELECT * FROM clases"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows

    @staticmethod
    def agregar_asignacion(ubi, ced, ref):
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = "INSERT INTO asignaciones VALUES (?, ?, ?)"
        c.execute(query, (ubi, ced, ref))
        conn.commit()
        conn.close()
        print("SILLA NÚMERO " + str(ubi) + " ASIGNADA.")

    @staticmethod
    def mostrar_asignaciones():
        conn = sqlite3.connect("taller.db")
        c = conn.cursor()
        query = """
                    SELECT
                        nombre, clase, ubi
                    FROM
                        pasajeros pj, clases cl, asignaciones ah
                    WHERE
                        ah.ced = pj.ced
                    AND 
                        ah.ref = cl.ref
                """
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return rows
        
    """
        self.db.agregar_clase(1, "Ejecutiva")
        self.db.agregar_clase(2, "Económica")
        self.db.agregar_asignacion(1, 1233897696, 1)
        self.db.agregar_asignacion(10, 100342564, 1)

    """