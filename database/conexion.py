import pyodbc

class DatabaseConnection:
    def __init__(self):
        self.server = 'localhost'
        self.database = 'dbproceso'
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'Trusted_Connection=yes;'
            )
            print("Connection successful")
        except pyodbc.Error as e:
            print("Error connecting to database: ", e)
            self.connection = None

    def create_database_if_not_exists(self):
        try:
            # Connect to the server itself (not a specific database)
            temp_connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                f'SERVER={self.server};'
                f'Trusted_Connection=yes;'
            )
            cursor = temp_connection.cursor()
            cursor.execute(f"IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'{self.database}') EXEC('CREATE DATABASE [{self.database}]')")
            cursor.close()
            temp_connection.close()
            print(f"Database '{self.database}' checked/created")
        except pyodbc.Error as e:
            print("Error creating database: ", e)

    def create_tables_if_not_exists(self):
        connection = self.get_connection()
        if not connection:
            print("No connection available to create tables.")
            return
        cursor = connection.cursor()

        tablas_sql = [
            """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='organizacion' AND xtype='U')
            CREATE TABLE organizacion (
                id INT PRIMARY KEY IDENTITY(1,1),
                nombre VARCHAR(100),
                direccion VARCHAR(255)
            )
            """,
            """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='sucursal' AND xtype='U')
            CREATE TABLE sucursal (
                id INT PRIMARY KEY IDENTITY(1,1),
                nombre VARCHAR(100),
                direccion VARCHAR(255),
                ciudad VARCHAR(100),
                organizacion_id INT,
                FOREIGN KEY (organizacion_id) REFERENCES organizacion(id)
            )
            """,
            """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='cliente' AND xtype='U')
            CREATE TABLE cliente (
                id INT PRIMARY KEY IDENTITY(1,1),
                nombre VARCHAR(100),
                direccion VARCHAR(255),
                telefono VARCHAR(15),
                fecha_nacimiento DATE,
                sexo CHAR(1),
                organizacion_id INT,
                apellido VARCHAR(255),
                FOREIGN KEY (organizacion_id) REFERENCES organizacion(id)
            )
            """,
            """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='cuenta' AND xtype='U')
            CREATE TABLE cuenta (
                id INT PRIMARY KEY IDENTITY(1,1),
                tipo VARCHAR(50),
                saldo_actual DECIMAL(10,2),
                saldo_medio DECIMAL(10,2),
                fecha_apertura DATE,
                sucursal_id INT,
                cliente_id INT,
                FOREIGN KEY (sucursal_id) REFERENCES sucursal(id),
                FOREIGN KEY (cliente_id) REFERENCES cliente(id)
            )
            """,
            """
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='empleado' AND xtype='U')
            CREATE TABLE empleado (
                id INT PRIMARY KEY IDENTITY(1,1),
                nombre VARCHAR(100),
                direccion VARCHAR(255),
                telefono VARCHAR(15),
                ciudad VARCHAR(100),
                sucursal_id INT,
                apellido VARCHAR(255),
                correo VARCHAR(255),
                FOREIGN KEY (sucursal_id) REFERENCES sucursal(id)
            )
            """
        ]

        for tabla_sql in tablas_sql:
            try:
                cursor.execute(tabla_sql)
                connection.commit()
                print("Tabla creada o ya existente.")
            except pyodbc.Error as e:
                print("Error al crear la tabla: ", e)

        cursor.close()
        connection.close()

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection

# Example usage
if __name__ == "__main__":
    db = DatabaseConnection()
    db.create_database_if_not_exists()
    db.connect()
    db.create_tables_if_not_exists()
