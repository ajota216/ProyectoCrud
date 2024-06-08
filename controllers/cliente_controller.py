import pyodbc
from database.conexion import DatabaseConnection
from models.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()

    def create_cliente(self, cliente: Cliente):
        if not self.connection:
            print("No connection available to create cliente.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO cliente (nombre, direccion, telefono, fecha_nacimiento, sexo, organizacion_id, apellido)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (cliente.get_nombre(), cliente.get_direccion(), cliente.get_telefono(), cliente.get_fecha_nacimiento(),
                  cliente.get_sexo(), cliente.get_organizacion_id(), cliente.get_apellido()))

            self.connection.commit()
            print("Cliente creado exitosamente.")
        except pyodbc.Error as e:
            print("Error al crear cliente: ", e)
        finally:
            cursor.close()
            # connection.close()

    def get_cliente(self, cliente_id: int):
        if not self.connection:
            print("No connection available to get cliente.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM cliente WHERE id = ?", cliente_id)
            row = cursor.fetchone()
            if row:
                cliente = Cliente(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    telefono=row.telefono,
                    fecha_nacimiento=row.fecha_nacimiento,
                    sexo=row.sexo,
                    organizacion_id=row.organizacion_id,
                    apellido=row.apellido
                )
                return cliente
            else:
                print("Cliente no encontrado.")
                return None
        except pyodbc.Error as e:
            print("Error al obtener cliente: ", e)
            return None
        finally:
            cursor.close()
            # connection.close()

    def get_all_clientes(self):
        if not self.connection:
            print("No connection available to get all clientes.")
            return []

        cursor = self.connection.cursor()
        clientes = []
        try:
            cursor.execute("SELECT * FROM cliente")
            rows = cursor.fetchall()
            for row in rows:
                cliente = Cliente(
                    id=row.id,
                    nombre=row.nombre,
                    direccion=row.direccion,
                    telefono=row.telefono,
                    fecha_nacimiento=row.fecha_nacimiento,
                    sexo=row.sexo,
                    organizacion_id=row.organizacion_id,
                    apellido=row.apellido
                )
                clientes.append(cliente)
            return clientes
        except pyodbc.Error as e:
            print("Error al obtener todos los clientes: ", e)
            return []
        finally:
            cursor.close()
            # connection.close()

    def update_cliente(self, cliente: Cliente):
        if not self.connection:
            print("No connection available to update cliente.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                UPDATE cliente
                SET nombre = ?, direccion = ?, telefono = ?, fecha_nacimiento = ?, sexo = ?, organizacion_id = ?, apellido = ?
                WHERE id = ?
            """, cliente.get_nombre(), cliente.get_direccion(), cliente.get_telefono(), cliente.get_fecha_nacimiento(), cliente.get_sexo(), cliente.get_organizacion_id(), cliente.get_apellido(), cliente.get_id())
            self.connection.commit()
            print("Cliente actualizado exitosamente.")
        except pyodbc.Error as e:
            print("Error al actualizar cliente: ", e)
        finally:
            cursor.close()
            # connection.close()

    def delete_cliente(self, cliente_id: int):
        if not self.connection:
            print("No connection available to delete cliente.")
            return

        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM cliente WHERE id = ?", cliente_id)
            self.connection.commit()
            print("Cliente eliminado exitosamente.")
        except pyodbc.Error as e:
            print("Error al eliminar cliente: ", e)
        finally:
            cursor.close()
            # connection.close()

    def get_all_clientes_ids(self):
        if not self.connection:
            print("No connection available to get all clientes.")
            return []

        cursor = self.connection.cursor()
        clientes_ids = []
        try:
            cursor.execute("SELECT id FROM cliente")
            rows = cursor.fetchall()
            for row in rows:
                clientes_ids.append(row.id)
            return clientes_ids
        except pyodbc.Error as e:
            print("Error al obtener todos los IDs de los clientes: ", e)
            return []
        finally:
            cursor.close()
            # connection.close()
