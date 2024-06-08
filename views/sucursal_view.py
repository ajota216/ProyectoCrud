import tkinter as tk
from tkinter import ttk, messagebox
from models.sucursal import Sucursal
from controllers.sucursal_controller import SucursalController


class SucursalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Sucursales")
        self.root.geometry("800x600")
        self.root.configure(bg="#dceefb")  # Fondo azul claro

        self.controller = SucursalController()
        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        title = tk.Label(self.root, text="Sucursales", font=("Arial", 24), bg="#dceefb")
        title.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#dceefb")
        form_frame.pack(pady=10, fill=tk.X)

        tk.Label(form_frame, text="Nombre:", bg="#dceefb").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Dirección:", bg="#dceefb").grid(row=0, column=2, padx=5, pady=5)
        self.direccion_entry = tk.Entry(form_frame)
        self.direccion_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Ciudad:", bg="#dceefb").grid(row=0, column=4, padx=5, pady=5)
        self.ciudad_entry = tk.Entry(form_frame)
        self.ciudad_entry.grid(row=0, column=5, padx=5, pady=5)

        button_frame = tk.Frame(self.root, bg="#dceefb")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_sucursal, bg="#1b6ec2", fg="white")
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="Actualizar", command=self.update_sucursal, bg="#1b6ec2",
                                  fg="white")
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_sucursal, bg="#1b6ec2", fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        deselect_button = tk.Button(button_frame, text="Deseleccionar", command=self.deselect_sucursal, bg="#1b6ec2",
                                    fg="white")
        deselect_button.grid(row=0, column=3, padx=5, pady=5)

        search_frame = tk.Frame(self.root, bg="#dceefb")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar por nombre:", bg="#dceefb").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.filter_table)

        self.table = ttk.Treeview(self.root, columns=("id", "nombre", "direccion", "ciudad"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("nombre", text="Nombre")
        self.table.heading("direccion", text="Dirección")
        self.table.heading("ciudad", text="Ciudad")
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<<TreeviewSelect>>", self.load_selected_sucursal)

    def validate_entries(self):
        if not self.nombre_entry.get() or not self.direccion_entry.get() or not self.ciudad_entry.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def add_sucursal(self):
        if not self.validate_entries():
            return

        sucursal = Sucursal(
            id=None,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            ciudad=self.ciudad_entry.get()
        )
        self.controller.create_sucursal(sucursal)
        self.update_table()
        self.clear_entries()

    def update_sucursal(self):
        if not self.validate_entries():
            return

        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una sucursal en la tabla.")
            return

        item = self.table.item(selected_item)
        sucursal_id = item["values"][0]

        sucursal = Sucursal(
            id=sucursal_id,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get(),
            ciudad=self.ciudad_entry.get()
        )
        self.controller.update_sucursal(sucursal)
        self.update_table()
        self.clear_entries()

    def delete_sucursal(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una sucursal en la tabla.")
            return

        item = self.table.item(selected_item)
        sucursal_id = item["values"][0]

        self.controller.delete_sucursal(sucursal_id)
        self.update_table()
        self.clear_entries()

    def load_selected_sucursal(self, event):
        selected_item = self.table.selection()
        if not selected_item:
            return

        item = self.table.item(selected_item)
        values = item["values"]

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, values[1])

        self.direccion_entry.delete(0, tk.END)
        self.direccion_entry.insert(0, values[2])

        self.ciudad_entry.delete(0, tk.END)
        self.ciudad_entry.insert(0, values[3])

    def deselect_sucursal(self):
        self.table.selection_remove(self.table.selection())
        self.clear_entries()

    def clear_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.ciudad_entry.delete(0, tk.END)

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        sucursales = self.controller.get_all_sucursales()
        for sucursal in sucursales:
            self.table.insert("", "end", values=(
            sucursal.get_id(), sucursal.get_nombre(), sucursal.get_direccion(), sucursal.get_ciudad()))

    def filter_table(self, event):
        search_term = self.search_entry.get().lower()
        for row in self.table.get_children():
            self.table.delete(row)

        sucursales = self.controller.get_all_sucursales()
        filtered_sucursales = [sucursal for sucursal in sucursales if search_term in sucursal.get_nombre().lower()]

        for sucursal in filtered_sucursales:
            self.table.insert("", "end", values=(
            sucursal.get_id(), sucursal.get_nombre(), sucursal.get_direccion(), sucursal.get_ciudad()))


if __name__ == "__main__":
    root = tk.Tk()
    app = SucursalApp(root)
    root.mainloop()
