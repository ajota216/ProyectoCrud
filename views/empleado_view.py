import tkinter as tk
from tkinter import ttk, messagebox
from models.empleado import Empleado
from controllers.empleado_controller import EmpleadoController
from controllers.sucursal_controller import SucursalController  # Importa el controlador de sucursales


class EmpleadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados")
        self.root.geometry("800x600")
        self.root.configure(bg="#dceefb")  # Fondo azul claro

        self.controller = EmpleadoController()
        self.sucursal_controller = SucursalController()  # Crea una instancia del controlador de sucursales
        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        title = tk.Label(self.root, text="Empleados", font=("Arial", 24), bg="#dceefb")
        title.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#dceefb")
        form_frame.pack(pady=10, fill=tk.X)

        tk.Label(form_frame, text="Nombre:", bg="#dceefb").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Dirección:", bg="#dceefb").grid(row=0, column=2, padx=5, pady=5)
        self.direccion_entry = tk.Entry(form_frame)
        self.direccion_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Teléfono:", bg="#dceefb").grid(row=0, column=4, padx=5, pady=5)
        self.telefono_entry = tk.Entry(form_frame)
        self.telefono_entry.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(form_frame, text="Ciudad:", bg="#dceefb").grid(row=1, column=0, padx=5, pady=5)
        self.ciudad_entry = tk.Entry(form_frame)
        self.ciudad_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="ID de Sucursal:", bg="#dceefb").grid(row=1, column=2, padx=5, pady=5)
        self.sucursal_combo = ttk.Combobox(form_frame)  # Crea el ComboBox
        self.sucursal_combo.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Apellido:", bg="#dceefb").grid(row=1, column=4, padx=5, pady=5)
        self.apellido_entry = tk.Entry(form_frame)
        self.apellido_entry.grid(row=1, column=5, padx=5, pady=5)

        tk.Label(form_frame, text="Correo:", bg="#dceefb").grid(row=2, column=0, padx=5, pady=5)
        self.correo_entry = tk.Entry(form_frame)
        self.correo_entry.grid(row=2, column=1, padx=5, pady=5)

        # Llena el ComboBox con las sucursales disponibles
        sucursales = self.sucursal_controller.get_all_sucursales_ids()
        self.sucursal_combo['values'] = sucursales  # Establece los valores del ComboBox

        button_frame = tk.Frame(self.root, bg="#dceefb")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_empleado, bg="#1b6ec2", fg="white")
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="Actualizar", command=self.update_empleado, bg="#1b6ec2",
                                  fg="white")
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_empleado, bg="#1b6ec2", fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        deselect_button = tk.Button(button_frame, text="Deseleccionar", command=self.deselect_empleado, bg="#1b6ec2",
                                    fg="white")
        deselect_button.grid(row=0, column=3, padx=5, pady=5)

        search_frame = tk.Frame(self.root, bg="#dceefb")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar por nombre:", bg="#dceefb").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.filter_table)

        self.table = ttk.Treeview(self.root, columns=("id", "nombre", "direccion", "telefono", "ciudad", "sucursal_id", "apellido", "correo"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("nombre", text="Nombre")
        self.table.heading("direccion", text="Dirección")
        self.table.heading("telefono", text="Teléfono")
        self.table.heading("ciudad", text="Ciudad")
        self.table.heading("sucursal_id", text="ID de Sucursal")
        self.table.heading("apellido", text="Apellido")
        self.table.heading("correo", text="Correo")
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<<TreeviewSelect>>", self.load_selected_empleado)

    def validate_entries(self):
        if not self.nombre_entry.get() or not self.direccion_entry.get() or not self.telefono_entry.get() \
                or not self.ciudad_entry.get() or not self.sucursal_combo.get() or not self.apellido_entry.get() \
                or not self.correo_entry.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def add_empleado(self):
        if not self.validate_entries():
            return

        empleado = Empleado(
            id=None,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            ciudad=self.ciudad_entry.get(),
            sucursal_id=int(self.sucursal_combo.get()),
            apellido=self.apellido_entry.get(),
            correo=self.correo_entry.get()
        )
        self.controller.create_empleado(empleado)
        self.update_table()
        self.clear_entries()

    def update_empleado(self):
        if not self.validate_entries():
            return

        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar un empleado en la tabla.")
            return

        item = self.table.item(selected_item)
        empleado_id = item["values"][0]

        empleado = Empleado(
            id=empleado_id,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            ciudad=self.ciudad_entry.get(),
            sucursal_id=int(self.sucursal_combo.get()),
            apellido=self.apellido_entry.get(),
            correo=self.correo_entry.get()
        )
        self.controller.update_empleado(empleado)
        self.update_table()
        self.clear_entries()

    def delete_empleado(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar un empleado en la tabla.")
            return

        item = self.table.item(selected_item)
        empleado_id = item["values"][0]

        self.controller.delete_empleado(empleado_id)
        self.update_table()
        self.clear_entries()

    def load_selected_empleado(self, event):
        selected_item = self.table.selection()
        if not selected_item:
            return

        item = self.table.item(selected_item)
        values = item["values"]

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, values[1])

        self.direccion_entry.delete(0, tk.END)
        self.direccion_entry.insert(0, values[2])

        self.telefono_entry.delete(0, tk.END)
        self.telefono_entry.insert(0, values[3])

        self.ciudad_entry.delete(0, tk.END)
        self.ciudad_entry.insert(0, values[4])

        self.sucursal_combo.delete(0, tk.END)
        self.sucursal_combo.insert(0, values[5])

        self.apellido_entry.delete(0, tk.END)
        self.apellido_entry.insert(0, values[6])

        self.correo_entry.delete(0, tk.END)
        self.correo_entry.insert(0, values[7])

    def deselect_empleado(self):
        self.table.selection_remove(self.table.selection())
        self.clear_entries()

    def clear_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.ciudad_entry.delete(0, tk.END)
        self.sucursal_combo.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        empleados = self.controller.get_all_empleados()
        for empleado in empleados:
            self.table.insert("", "end", values=(
                empleado.get_id(), empleado.get_nombre(), empleado.get_direccion(), empleado.get_telefono(),
                empleado.get_ciudad(), empleado.get_sucursal_id(), empleado.get_apellido(), empleado.get_correo()))

    def filter_table(self, event):
        search_term = self.search_entry.get().lower()
        for row in self.table.get_children():
            self.table.delete(row)

        empleados = self.controller.get_all_empleados()
        filtered_empleados = [empleado for empleado in empleados if search_term in empleado.get_nombre().lower()]

        for empleado in filtered_empleados:
            self.table.insert("", "end", values=(
                empleado.get_id(), empleado.get_nombre(), empleado.get_direccion(), empleado.get_telefono(),
                empleado.get_ciudad(), empleado.get_sucursal_id(), empleado.get_apellido(), empleado.get_correo()))


if __name__ == "__main__":
    root = tk.Tk()
    app = EmpleadoApp(root)
    root.mainloop()
