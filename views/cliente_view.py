import tkinter as tk
from tkinter import ttk, messagebox
from models.cliente import Cliente
from controllers.cliente_controller import ClienteController
from controllers.organizacion_controller import OrganizacionController

class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.geometry("800x600")
        self.root.configure(bg="#dceefb")  # Fondo azul claro

        self.controller = ClienteController()
        self.organizacion_controller = OrganizacionController()  # Controlador de organizaciones
        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        title = tk.Label(self.root, text="Clientes", font=("Arial", 24), bg="#dceefb")
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

        tk.Label(form_frame, text="Fecha de Nacimiento:", bg="#dceefb").grid(row=1, column=0, padx=5, pady=5)
        self.fecha_nacimiento_entry = tk.Entry(form_frame)
        self.fecha_nacimiento_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Sexo:", bg="#dceefb").grid(row=1, column=2, padx=5, pady=5)
        self.sexo_combo = ttk.Combobox(form_frame, values=["M", "F"])
        self.sexo_combo.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Apellido:", bg="#dceefb").grid(row=1, column=4, padx=5, pady=5)
        self.apellido_entry = tk.Entry(form_frame)
        self.apellido_entry.grid(row=1, column=5, padx=5, pady=5)

        # Agrega un ComboBox para las organizaciones
        tk.Label(form_frame, text="Organización:", bg="#dceefb").grid(row=2, column=0, padx=5, pady=5)
        self.organizacion_combo = ttk.Combobox(form_frame)
        self.organizacion_combo.grid(row=2, column=1, padx=5, pady=5)

        # Llena el ComboBox con las organizaciones disponibles
        organizaciones = self.organizacion_controller.get_all_organizaciones()
        self.organizacion_combo['values'] = [organizacion.get_nombre() for organizacion in organizaciones]

        button_frame = tk.Frame(self.root, bg="#dceefb")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_cliente, bg="#1b6ec2", fg="white")
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="Actualizar", command=self.update_cliente, bg="#1b6ec2",
                                  fg="white")
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_cliente, bg="#1b6ec2", fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        deselect_button = tk.Button(button_frame, text="Deseleccionar", command=self.deselect_cliente, bg="#1b6ec2",
                                    fg="white")
        deselect_button.grid(row=0, column=3, padx=5, pady=5)

        search_frame = tk.Frame(self.root, bg="#dceefb")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar por nombre:", bg="#dceefb").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.filter_table)

        self.table = ttk.Treeview(self.root, columns=("id", "nombre", "direccion", "telefono", "fecha_nacimiento", "sexo", "organizacion_id", "apellido"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("nombre", text="Nombre")
        self.table.heading("direccion", text="Dirección")
        self.table.heading("telefono", text="Teléfono")
        self.table.heading("fecha_nacimiento", text="Fecha Nacimiento")
        self.table.heading("sexo", text="Sexo")
        self.table.heading("organizacion_id", text="ID de Organización")
        self.table.heading("apellido", text="Apellido")
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<<TreeviewSelect>>", self.load_selected_cliente)

    def validate_entries(self):
        if not self.nombre_entry.get() or not self.direccion_entry.get() or not self.telefono_entry.get() \
                or not self.fecha_nacimiento_entry.get() or not self.sexo_combo.get() or not self.apellido_entry.get() \
                or not self.organizacion_combo.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def add_cliente(self):
        if not self.validate_entries():
            return

        # Obtiene el ID de la organización seleccionada del ComboBox
        selected_org_name = self.organizacion_combo.get()
        selected_org_id = None
        for organizacion in self.organizacion_controller.get_all_organizaciones():
            if organizacion.get_nombre() == selected_org_name:
                selected_org_id = organizacion.get_id()
                break

        cliente = Cliente(
            id=None,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            fecha_nacimiento=self.fecha_nacimiento_entry.get(),
            sexo=self.sexo_combo.get(),
            organizacion_id=selected_org_id,
            apellido=self.apellido_entry.get()
        )
        self.controller.create_cliente(cliente)
        self.update_table()
        self.clear_entries()

    def update_cliente(self):
        if not self.validate_entries():
            return

        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar un cliente en la tabla.")
            return

        item = self.table.item(selected_item)
        cliente_id = item["values"][0]

        # Obtiene el ID de la organización seleccionada del ComboBox
        selected_org_name = self.organizacion_combo.get()
        selected_org_id = None
        for organizacion in self.organizacion_controller.get_all_organizaciones():
            if organizacion.get_nombre() == selected_org_name:
                selected_org_id = organizacion.get_id()
                break

        cliente = Cliente(
            id=cliente_id,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get(),
            fecha_nacimiento=self.fecha_nacimiento_entry.get(),
            sexo=self.sexo_combo.get(),
            organizacion_id=selected_org_id,
            apellido=self.apellido_entry.get()
        )
        self.controller.update_cliente(cliente)
        self.update_table()
        self.clear_entries()

    def delete_cliente(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar un cliente en la tabla.")
            return

        item = self.table.item(selected_item)
        cliente_id = item["values"][0]

        self.controller.delete_cliente(cliente_id)
        self.update_table()
        self.clear_entries()

    def load_selected_cliente(self, event):
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

        self.fecha_nacimiento_entry.delete(0, tk.END)
        self.fecha_nacimiento_entry.insert(0, values[4])

        self.sexo_combo.set(values[5])

        # Selecciona el nombre de la organización en el ComboBox
        self.organizacion_combo.set(values[6])

        self.apellido_entry.delete(0, tk.END)
        self.apellido_entry.insert(0, values[7])

    def deselect_cliente(self):
        self.table.selection_remove(self.table.selection())
        self.clear_entries()

    def clear_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.fecha_nacimiento_entry.delete(0, tk.END)
        self.sexo_combo.set("")
        self.organizacion_combo.set("")
        self.apellido_entry.delete(0, tk.END)

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        clientes = self.controller.get_all_clientes()
        for cliente in clientes:
            self.table.insert("", "end", values=(
                cliente.get_id(), cliente.get_nombre(), cliente.get_direccion(), cliente.get_telefono(),
                cliente.get_fecha_nacimiento(), cliente.get_sexo(), cliente.get_organizacion_id(),
                cliente.get_apellido()))

    def filter_table(self, event):
        search_term = self.search_entry.get().lower()
        for row in self.table.get_children():
            self.table.delete(row)

        clientes = self.controller.get_all_clientes()
        filtered_clientes = [cliente for cliente in clientes if search_term in cliente.get_nombre().lower()]

        for cliente in filtered_clientes:
            self.table.insert("", "end", values=(
                cliente.get_id(), cliente.get_nombre(), cliente.get_direccion(), cliente.get_telefono(),
                cliente.get_fecha_nacimiento(), cliente.get_sexo(), cliente.get_organizacion_id(),
                cliente.get_apellido()))


if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()
