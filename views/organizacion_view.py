import tkinter as tk
from tkinter import ttk, messagebox
from models.organizacion import Organizacion
from controllers.organizacion_controller import OrganizacionController


class OrganizacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Organizaciones")
        self.root.geometry("800x600")
        self.root.configure(bg="#dceefb")  # Fondo azul claro

        self.controller = OrganizacionController()
        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        title = tk.Label(self.root, text="Organizaciones", font=("Arial", 24), bg="#dceefb")
        title.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#dceefb")
        form_frame.pack(pady=10, fill=tk.X)

        tk.Label(form_frame, text="Nombre:", bg="#dceefb").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Dirección:", bg="#dceefb").grid(row=0, column=2, padx=5, pady=5)
        self.direccion_entry = tk.Entry(form_frame)
        self.direccion_entry.grid(row=0, column=3, padx=5, pady=5)

        button_frame = tk.Frame(self.root, bg="#dceefb")
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Agregar", command=self.add_organizacion, bg="#1b6ec2", fg="white")
        add_button.grid(row=0, column=0, padx=5, pady=5)

        update_button = tk.Button(button_frame, text="Actualizar", command=self.update_organizacion, bg="#1b6ec2",
                                  fg="white")
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_organizacion, bg="#1b6ec2",
                                  fg="white")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

        deselect_button = tk.Button(button_frame, text="Deseleccionar", command=self.deselect_organizacion,
                                    bg="#1b6ec2", fg="white")
        deselect_button.grid(row=0, column=3, padx=5, pady=5)

        search_frame = tk.Frame(self.root, bg="#dceefb")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Buscar por nombre:", bg="#dceefb").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.filter_table)

        self.table = ttk.Treeview(self.root, columns=("id", "nombre", "direccion"), show="headings")
        self.table.heading("id", text="ID")
        self.table.heading("nombre", text="Nombre")
        self.table.heading("direccion", text="Dirección")
        self.table.pack(fill=tk.BOTH, expand=True)
        self.table.bind("<<TreeviewSelect>>", self.load_selected_organizacion)

    def validate_entries(self):
        if not self.nombre_entry.get() or not self.direccion_entry.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        return True

    def add_organizacion(self):
        if not self.validate_entries():
            return

        organizacion = Organizacion(
            id=None,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get()
        )
        self.controller.create_organizacion(organizacion)
        self.update_table()
        self.clear_entries()

    def update_organizacion(self):
        if not self.validate_entries():
            return

        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una organización en la tabla.")
            return

        item = self.table.item(selected_item)
        organizacion_id = item["values"][0]

        organizacion = Organizacion(
            id=organizacion_id,
            nombre=self.nombre_entry.get(),
            direccion=self.direccion_entry.get()
        )
        self.controller.update_organizacion(organizacion)
        self.update_table()
        self.clear_entries()

    def delete_organizacion(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Debe seleccionar una organización en la tabla.")
            return

        item = self.table.item(selected_item)
        organizacion_id = item["values"][0]

        self.controller.delete_organizacion(organizacion_id)
        self.update_table()
        self.clear_entries()

    def load_selected_organizacion(self, event):
        selected_item = self.table.selection()
        if not selected_item:
            return

        item = self.table.item(selected_item)
        values = item["values"]

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, values[1])

        self.direccion_entry.delete(0, tk.END)
        self.direccion_entry.insert(0, values[2])

    def deselect_organizacion(self):
        self.table.selection_remove(self.table.selection())
        self.clear_entries()

    def clear_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        organizaciones = self.controller.get_all_organizaciones()
        for organizacion in organizaciones:
            self.table.insert("", "end",
                              values=(organizacion.get_id(), organizacion.get_nombre(), organizacion.get_direccion()))

    def filter_table(self, event):
        search_term = self.search_entry.get().lower()
        for row in self.table.get_children():
            self.table.delete(row)

        organizaciones = self.controller.get_all_organizaciones()
        filtered_organizaciones = [organizacion for organizacion in organizaciones if
                                   search_term in organizacion.get_nombre().lower()]

        for organizacion in filtered_organizaciones:
            self.table.insert("", "end",
                              values=(organizacion.get_id(), organizacion.get_nombre(), organizacion.get_direccion()))


if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizacionApp(root)
    root.mainloop()
