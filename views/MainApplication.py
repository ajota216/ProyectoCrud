import tkinter as tk
from tkinter import ttk
from views.cliente_view import ClienteApp
from views.cuenta_view import CuentaApp
from views.empleado_view import EmpleadoApp
from views.organizacion_view import OrganizacionApp
from views.sucursal_view import SucursalApp

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("600x400")  # Tamaño de la ventana principal

        # Crear un frame para organizar los elementos
        frame_principal = ttk.Frame(self)
        frame_principal.pack(expand=True, fill=tk.BOTH)

        # Título grande
        lbl_titulo = ttk.Label(frame_principal, text="Menú Principal", font=("Arial", 20))
        lbl_titulo.pack(pady=20)

        # Botones para abrir las diferentes interfaces
        btn_gestion_sucursales = ttk.Button(frame_principal, text="Gestionar Sucursales", command=self.abrir_gestion_sucursales)
        btn_gestion_sucursales.pack(pady=10)

        btn_gestion_organizaciones = ttk.Button(frame_principal, text="Gestionar Organizaciones",
                                                 command=self.abrir_gestion_organizaciones)
        btn_gestion_organizaciones.pack(pady=10)

        btn_gestion_empleados = ttk.Button(frame_principal, text="Gestionar Empleados", command=self.abrir_gestion_empleados)
        btn_gestion_empleados.pack(pady=10)

        btn_gestion_clientes = ttk.Button(frame_principal, text="Gestionar Clientes", command=self.abrir_gestion_clientes)
        btn_gestion_clientes.pack(pady=10)

        btn_gestion_cuentas = ttk.Button(frame_principal, text="Gestionar Cuentas", command=self.abrir_gestion_cuentas)
        btn_gestion_cuentas.pack(pady=10)

    def abrir_gestion_sucursales(self):
        # Aquí abrir la interfaz de gestión de sucursales
        print("Abriendo interfaz de gestión de sucursales")
        root = tk.Tk()
        app = SucursalApp(root)
        root.mainloop()

    def abrir_gestion_organizaciones(self):
        # Aquí abrir la interfaz de gestión de organizaciones
        print("Abriendo interfaz de gestión de organizaciones")
        root = tk.Tk()
        app = OrganizacionApp(root)
        root.mainloop()

    def abrir_gestion_empleados(self):
        # Aquí abrir la interfaz de gestión de empleados
        print("Abriendo interfaz de gestión de empleados")
        root = tk.Tk()
        app = EmpleadoApp(root)
        root.mainloop()

    def abrir_gestion_clientes(self):
        # Aquí abrir la interfaz de gestión de clientes
        print("Abriendo interfaz de gestión de clientes")
        root = tk.Tk()
        app = ClienteApp(root)
        root.mainloop()

    def abrir_gestion_cuentas(self):
        # Aquí abrir la interfaz de gestión de cuentas
        print("Abriendo interfaz de gestión de cuentas")
        root = tk.Tk()
        app = CuentaApp(root)
        root.mainloop()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
