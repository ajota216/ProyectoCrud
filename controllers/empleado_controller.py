import pyodbc
from database.conexion import DatabaseConnection
from models.empleado import Empleado


class EmpleadoController:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()

    def create_empleado(self, empleado: Empleado):
        if not self.connection:
            print("No connection available to create empleado.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO empleado (nombre, direccion, telefono, ciudad, sucursal_id, apellido, correo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (empleado.get_nombre(), empleado.get_direccion(), empleado.get_telefono(), empleado.get_ciudad(),
                  empleado.get_sucursal_id(), empleado.get_apellido(), empleado.get_correo()))
            self.connection.commit()
            print("Empleado creado exitosamente.")
        except pyodbc.Error as e:
            print("Error al crear empleado: ", e)
        finally:
            cursor.close()

    def get_empleado(self, empleado_id: int):
        if not self.connection:
            print("No connection available to get empleado.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM empleado WHERE id = ?", empleado_id)
            row = cursor.fetchone()
            if row:
                empleado = Empleado(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    telefono=row.telefono,
                    ciudad=row.ciudad,
                    sucursal_id=row.sucursal_id,
                    apellido=row.apellido,
                    correo=row.correo
                )
                return empleado
            else:
                print("Empleado no encontrado.")
                return None
        except pyodbc.Error as e:
            print("Error al obtener empleado: ", e)
            return None
        finally:
            cursor.close()

    def get_all_empleados(self):
        if not self.connection:
            print("No connection available to get all empleados.")
            return []

        cursor = self.connection.cursor()
        empleados = []
        try:
            cursor.execute("SELECT * FROM empleado")
            rows = cursor.fetchall()
            for row in rows:
                empleado = Empleado(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    telefono=row.telefono,
                    ciudad=row.ciudad,
                    sucursal_id=row.sucursal_id,
                    apellido=row.apellido,
                    correo=row.correo
                )
                empleados.append(empleado)
            return empleados
        except pyodbc.Error as e:
            print("Error al obtener todos los empleados: ", e)
            return []
        finally:
            cursor.close()

    def update_empleado(self, empleado: Empleado):
        if not self.connection:
            print("No connection available to update empleado.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                UPDATE empleado
                SET nombre = ?, direccion = ?, telefono = ?, ciudad = ?, sucursal_id = ?, apellido = ?, correo = ?
                WHERE id = ?
            """, (empleado.get_nombre(), empleado.get_direccion(), empleado.get_telefono(), empleado.get_ciudad(),
                  empleado.get_sucursal_id(), empleado.get_apellido(), empleado.get_correo(), empleado.get_id()))
            self.connection.commit()
            print("Empleado actualizado exitosamente.")
        except pyodbc.Error as e:
            print("Error al actualizar empleado: ", e)
        finally:
            cursor.close()

    def delete_empleado(self, empleado_id: int):
        if not self.connection:
            print("No connection available to delete empleado.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM empleado WHERE id = ?", empleado_id)
            self.connection.commit()
            print("Empleado eliminado exitosamente.")
        except pyodbc.Error as e:
            print("Error al eliminar empleado: ", e)
        finally:
            cursor.close()
