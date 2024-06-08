import pyodbc
from database.conexion import DatabaseConnection
from models.organizacion import Organizacion

class OrganizacionController:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_organizacion(self, organizacion: Organizacion):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to create organizacion.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO organizacion (nombre, direccion)
                VALUES (?, ?)
            """, (organizacion.get_nombre(), organizacion.get_direccion()))
            connection.commit()
            print("Organizacion creada exitosamente.")
        except pyodbc.Error as e:
            print("Error al crear organizacion: ", e)
        finally:
            cursor.close()
            connection.close()

    def get_organizacion(self, organizacion_id: int):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get organizacion.")
            return None

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM organizacion WHERE id = ?", organizacion_id)
            row = cursor.fetchone()
            if row:
                organizacion = Organizacion(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion
                )
                return organizacion
            else:
                print("Organizacion no encontrada.")
                return None
        except pyodbc.Error as e:
            print("Error al obtener organizacion: ", e)
            return None
        finally:
            cursor.close()
            connection.close()

    def get_all_organizaciones(self):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get all organizaciones.")
            return []

        cursor = connection.cursor()
        organizaciones = []
        try:
            cursor.execute("SELECT * FROM organizacion")
            rows = cursor.fetchall()
            for row in rows:
                organizacion = Organizacion(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion
                )
                organizaciones.append(organizacion)
            return organizaciones
        except pyodbc.Error as e:
            print("Error al obtener todas las organizaciones: ", e)
            return []
        finally:
            cursor.close()
            connection.close()

    def update_organizacion(self, organizacion: Organizacion):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to update organizacion.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE organizacion
                SET nombre = ?, direccion = ?
                WHERE id = ?
            """, (organizacion.get_nombre(), organizacion.get_direccion(), organizacion.get_id()))
            connection.commit()
            print("Organizacion actualizada exitosamente.")
        except pyodbc.Error as e:
            print("Error al actualizar organizacion: ", e)
        finally:
            cursor.close()
            connection.close()

    def delete_organizacion(self, organizacion_id: int):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to delete organizacion.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM organizacion WHERE id = ?", organizacion_id)
            connection.commit()
            print("Organizacion eliminada exitosamente.")
        except pyodbc.Error as e:
            print("Error al eliminar organizacion: ", e)
        finally:
            cursor.close()
            connection.close()

    def get_all_organizaciones(self):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get all organizaciones.")
            return []

        cursor = connection.cursor()
        organizaciones = []
        try:
            cursor.execute("SELECT * FROM organizacion")
            rows = cursor.fetchall()
            for row in rows:
                organizacion = Organizacion(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion
                )
                organizaciones.append(organizacion)
            return organizaciones
        except pyodbc.Error as e:
            print("Error al obtener todas las organizaciones: ", e)
            return []
        finally:
            cursor.close()
            connection.close()
