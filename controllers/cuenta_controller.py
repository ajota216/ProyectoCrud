import pyodbc
from database.conexion import DatabaseConnection
from models.cuenta import Cuenta

class CuentaController:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_cuenta(self, cuenta: Cuenta):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to create cuenta.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO cuenta (tipo, saldo_actual, saldo_medio, fecha_apertura, sucursal_id, cliente_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (cuenta.get_tipo(), cuenta.get_saldo_actual(), cuenta.get_saldo_medio(), cuenta.get_fecha_apertura(), cuenta.get_sucursal_id(), cuenta.get_cliente_id()))
            connection.commit()
            print("Cuenta creada exitosamente.")
        except pyodbc.Error as e:
            print("Error al crear cuenta: ", e)
        finally:
            cursor.close()
            connection.close()

    def get_cuenta(self, cuenta_id: int):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get cuenta.")
            return None

        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM cuenta WHERE id = ?", cuenta_id)
            row = cursor.fetchone()
            if row:
                cuenta = Cuenta(
                    id=row.id,
                    tipo=row.tipo,
                    saldo_actual=row.saldo_actual,
                    saldo_medio=row.saldo_medio,
                    fecha_apertura=row.fecha_apertura,
                    sucursal_id=row.sucursal_id,
                    cliente_id=row.cliente_id
                )
                return cuenta
            else:
                print("Cuenta no encontrada.")
                return None
        except pyodbc.Error as e:
            print("Error al obtener cuenta: ", e)
            return None
        finally:
            cursor.close()
            connection.close()

    def get_all_cuentas(self):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get all cuentas.")
            return []

        cursor = connection.cursor()
        cuentas = []
        try:
            cursor.execute("SELECT * FROM cuenta")
            rows = cursor.fetchall()
            for row in rows:
                cuenta = Cuenta(
                    id=row.id,
                    tipo=row.tipo,
                    saldo_actual=row.saldo_actual,
                    saldo_medio=row.saldo_medio,
                    fecha_apertura=row.fecha_apertura,
                    sucursal_id=row.sucursal_id,
                    cliente_id=row.cliente_id
                )
                cuentas.append(cuenta)
            return cuentas
        except pyodbc.Error as e:
            print("Error al obtener todas las cuentas: ", e)
            return []
        finally:
            cursor.close()
            connection.close()

    def update_cuenta(self, cuenta: Cuenta):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to update cuenta.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("""
                UPDATE cuenta
                SET tipo = ?, saldo_actual = ?, saldo_medio = ?, fecha_apertura = ?, sucursal_id = ?, cliente_id = ?
                WHERE id = ?
            """, (cuenta.get_tipo(), cuenta.get_saldo_actual(), cuenta.get_saldo_medio(), cuenta.get_fecha_apertura(), cuenta.get_sucursal_id(), cuenta.get_cliente_id(), cuenta.get_id()))
            connection.commit()
            print("Cuenta actualizada exitosamente.")
        except pyodbc.Error as e:
            print("Error al actualizar cuenta: ", e)
        finally:
            cursor.close()
            connection.close()

    def delete_cuenta(self, cuenta_id: int):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to delete cuenta.")
            return

        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM cuenta WHERE id = ?", cuenta_id)
            connection.commit()
            print("Cuenta eliminada exitosamente.")
        except pyodbc.Error as e:
            print("Error al eliminar cuenta: ", e)
        finally:
            cursor.close()
            connection.close()

    def get_all_cuentas(self):
        connection = self.db.get_connection()
        if not connection:
            print("No connection available to get all cuentas.")
            return []

        cursor = connection.cursor()
        cuentas = []
        try:
            cursor.execute("SELECT * FROM cuenta")
            rows = cursor.fetchall()
            for row in rows:
                cuenta = Cuenta(
                    id=row.id,
                    tipo=row.tipo,
                    saldo_actual=row.saldo_actual,
                    saldo_medio=row.saldo_medio,
                    fecha_apertura=row.fecha_apertura,
                    sucursal_id=row.sucursal_id,
                    cliente_id=row.cliente_id
                )
                cuentas.append(cuenta)
            return cuentas
        except pyodbc.Error as e:
            print("Error al obtener todas las cuentas: ", e)
            return []
        finally:
            cursor.close()
            connection.close()
