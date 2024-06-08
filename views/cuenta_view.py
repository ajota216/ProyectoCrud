import tkinter as tk
from tkinter import ttk, messagebox
from controllers.cuenta_controller import CuentaController
from controllers.sucursal_controller import SucursalController
from controllers.cliente_controller import ClienteController
from models.cuenta import Cuenta


class CuentaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Cuentas")
        self.root.geometry("800x600")
        self.root.configure(bg="#dceefb")  # Fondo azul claro

        self.controller = CuentaController()
        self.sucursal_controller = SucursalController()
        self.cliente_controller = ClienteController()

        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        title = tk.Label(self.root, text="Cuentas", font=("Arial", 24), bg="#dceefb")
        title.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#dceefb")
        form_frame.pack(pady=10, fill=tk.X)

        tk.Label(form_frame, text="Tipo:", bg="#dceefb").grid(row=0, column=0, padx=5, pady=5)
        self.tipo_entry = tk.Entry(form_frame)
        self.tipo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Saldo Actual:", bg="#dceefb").grid(row=0, column=2, padx=5, pady=5)
        self.saldo_actual_entry = tk.Entry(form_frame)
        self.saldo_actual_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Saldo Medio:", bg="#dceefb").grid(row=0, column=4, padx=5, pady=5)
        self.saldo_medio_entry = tk.Entry(form_frame)
        self.saldo_medio_entry.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(form_frame, text="Fecha de Apertura:", bg="#dceefb").grid(row=1, column=0, padx=5, pady=5)
        self.fecha_apertura_entry = tk.Entry(form_frame)
        self.fecha_apertura_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="ID de Sucursal:", bg="#dceefb").grid(row=1, column=2, padx=5, pady=5)
        self.sucursal_combo = ttk.Combobox(form_frame)  # ComboBox para la sucursal
        self.sucursal_combo.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="ID de Cliente:", bg="#dceefb").grid(row=1, column=4, padx=5, pady=5)
        self.cliente_combo = ttk.Combobox(form_frame)  # ComboBox para el cliente
        self.cliente_combo.grid(row=1, column=5, padx=5, pady=5)

        # Llena el ComboBox con las sucursales disponibles
        sucursales = self.sucursal_controller.get_all_sucursales_ids()
        self.sucursal_combo['values'] = sucursales

        # Llena el ComboBox con los clientes disponibles
        clientes = self.cliente_controller.get_all_clientes_ids()
        self.cliente_combo['values'] = clientes

        button_frame = tk.Frame(self.root, bg="#dceefb")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_cuenta, bg="#1b6ec2", fg="white")
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="Actualizar", command=self.update_cuenta, bg="#1b6ec2", fg="white")
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_cuenta, bg="#1b6ec2", fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.table = ttk.Treeview(self.root, columns=(
        "id", "tipo", "saldo_actual", "saldo_medio", "fecha_apertura", "sucursal_id", "cliente_id"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("tipo", text="Tipo")
        self.table.heading("saldo_actual", text="Saldo Actual")
        self.table.heading("saldo_medio", text="Saldo Medio")
        self.table.heading("fecha_apertura", text="Fecha de Apertura")
        self.table.heading("sucursal_id", text="ID de Sucursal")
        self.table.heading("cliente_id", text="ID de Cliente")
        self.table.pack(fill=tk.BOTH, expand=True)

    def add_cuenta(self):
        tipo = self.tipo_entry.get()
        saldo_actual = float(self.saldo_actual_entry.get())
        saldo_medio = float(self.saldo_medio_entry.get())
        fecha_apertura = self.fecha_apertura_entry.get()
        sucursal_id = int(self.sucursal_combo.get())
        cliente_id = int(self.cliente_combo.get())

        cuenta = Cuenta('', tipo, saldo_actual, saldo_medio, fecha_apertura, sucursal_id, cliente_id)
        self.controller.create_cuenta(cuenta)
        self.update_table()

    def update_table(self):
        # Clear the table
        for record in self.table.get_children():
            self.table.delete(record)

        # Retrieve all accounts from the database and insert them into the table
        cuentas = self.controller.get_all_cuentas()
        for cuenta in cuentas:
            self.table.insert("", "end", values=(
                cuenta.get_id(),
                cuenta.get_tipo(),
                cuenta.get_saldo_actual(),
                cuenta.get_saldo_medio(),
                cuenta.get_fecha_apertura(),
                cuenta.get_sucursal_id(),
                cuenta.get_cliente_id()
            ))

    def update_cuenta(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, seleccione una cuenta.")
            return

        tipo = self.tipo_entry.get()
        saldo_actual = float(self.saldo_actual_entry.get())
        saldo_medio = float(self.saldo_medio_entry.get())
        fecha_apertura = self.fecha_apertura_entry.get()
        sucursal_id = int(self.sucursal_combo.get())
        cliente_id = int(self.cliente_combo.get())

        cuenta_id = int(self.table.item(selected_item, "values")[0])
        cuenta = Cuenta(cuenta_id, tipo, saldo_actual, saldo_medio, fecha_apertura, sucursal_id, cliente_id)
        self.controller.update_cuenta(cuenta)
        self.update_table()

    def delete_cuenta(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, seleccione una cuenta.")
            return

        cuenta_id = int(self.table.item(selected_item, "values")[0])
        self.controller.delete_cuenta(cuenta_id)
        self.update_table()


if __name__ == "__main__":
    root = tk.Tk()
    app = CuentaApp(root)
    root.mainloop()
