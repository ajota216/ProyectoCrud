import pyodbc
from database.conexion import DatabaseConnection
from models.sucursal import Sucursal


class SucursalController:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()

    def create_sucursal(self, sucursal: Sucursal):

        if not self.connection:
            print("No connection available to create sucursal.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO sucursal (nombre, direccion, ciudad)
                VALUES (?, ?, ?)
            """, (sucursal.get_nombre(), sucursal.get_direccion(), sucursal.get_ciudad()))
            self.connection.commit()
            print("Sucursal creada exitosamente.")
        except pyodbc.Error as e:
            print("Error al crear sucursal: ", e)
        finally:
            cursor.close()
            # connection.close()

    def get_sucursal(self, sucursal_id: int):
        if not self.connection:
            print("No connection available to get sucursal.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM sucursal WHERE id = ?", sucursal_id)
            row = cursor.fetchone()
            if row:
                sucursal = Sucursal(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    ciudad=row.ciudad
                )
                return sucursal
            else:
                print("Sucursal no encontrada.")
                return None
        except pyodbc.Error as e:
            print("Error al obtener sucursal: ", e)
            return None
        finally:
            cursor.close()
            # self.connection.close()

    def get_all_sucursales(self):
        if not self.connection:
            print("No connection available to get all sucursales.")
            return []

        cursor = self.connection.cursor()
        sucursales = []
        try:
            cursor.execute("SELECT * FROM sucursal")
            rows = cursor.fetchall()
            for row in rows:
                sucursal = Sucursal(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    ciudad=row.ciudad
                )
                sucursales.append(sucursal)
            return sucursales
        except pyodbc.Error as e:
            print("Error al obtener todas las sucursales: ", e)
            return []
        finally:
            cursor.close()
            # self.connection.close()

    def update_sucursal(self, sucursal: Sucursal):
        if not self.connection:
            print("No connection available to update sucursal.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                UPDATE sucursal
                SET nombre = ?, direccion = ?, ciudad = ?
                WHERE id = ?
            """, (sucursal.get_nombre(), sucursal.get_direccion(), sucursal.get_ciudad(), sucursal.get_id()))
            self.connection.commit()
            print("Sucursal actualizada exitosamente.")
        except pyodbc.Error as e:
            print("Error al actualizar sucursal: ", e)
        finally:
            cursor.close()
            # self.connection.close()

    def delete_sucursal(self, sucursal_id: int):
        if not self.connection:
            print("No connection available to delete sucursal.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM sucursal WHERE id = ?", sucursal_id)
            self.connection.commit()
            print("Sucursal eliminada exitosamente.")
        except pyodbc.Error as e:
            print("Error al eliminar sucursal: ", e)
        finally:
            cursor.close()
            # self.connection.close()

    def get_all_sucursales_names(self):
        if not self.connection:
            print("No connection available to get all sucursales.")
            return []

        cursor = self.connection.cursor()
        sucursales = []
        try:
            cursor.execute("SELECT nombre FROM sucursal")
            rows = cursor.fetchall()
            for row in rows:
                sucursales.append(row.nombre)
            return sucursales
        except pyodbc.Error as e:
            print("Error al obtener todas las sucursales: ", e)
            return []
        finally:
            cursor.close()

    def get_all_sucursales_ids(self):
        if not self.connection:
            print("No connection available to get all sucursales.")
            return []

        cursor = self.connection.cursor()
        sucursales = []
        try:
            cursor.execute("SELECT id FROM sucursal")
            rows = cursor.fetchall()
            for row in rows:
                sucursales.append(row.id)
            return sucursales
        except pyodbc.Error as e:
            print("Error al obtener todas las sucursales: ", e)
            return []
        finally:
            cursor.close()
