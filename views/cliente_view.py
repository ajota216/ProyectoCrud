import tkinter as tk
from tkinter import ttk, messagebox
from controllers.cliente_controller import ClienteController
from models.cliente import Cliente


class ClienteView:
    def __init__(self, root):
        self.controller = ClienteController()
        self.root = root
        self.root.title("Gestión de Clientes")

        # Configurar el menú principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.cliente_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Cliente", menu=self.cliente_menu)
        self.cliente_menu.add_command(label="Crear Cliente", command=self.create_cliente)
        self.cliente_menu.add_command(label="Obtener Cliente", command=self.get_cliente)
        self.cliente_menu.add_command(label="Obtener Todos los Clientes", command=self.get_all_clientes)
        self.cliente_menu.add_command(label="Actualizar Cliente", command=self.update_cliente)
        self.cliente_menu.add_command(label="Eliminar Cliente", command=self.delete_cliente)

    def create_cliente(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Crear Cliente")

        tk.Label(create_window, text="Nombre").grid(row=0, column=0)
        nombre_entry = tk.Entry(create_window)
        nombre_entry.grid(row=0, column=1)

        tk.Label(create_window, text="Dirección").grid(row=1, column=0)
        direccion_entry = tk.Entry(create_window)
        direccion_entry.grid(row=1, column=1)

        tk.Label(create_window, text="Teléfono").grid(row=2, column=0)
        telefono_entry = tk.Entry(create_window)
        telefono_entry.grid(row=2, column=1)

        tk.Label(create_window, text="Fecha de Nacimiento (YYYY-MM-DD)").grid(row=3, column=0)
        fecha_nacimiento_entry = tk.Entry(create_window)
        fecha_nacimiento_entry.grid(row=3, column=1)

        tk.Label(create_window, text="Sexo (M/F)").grid(row=4, column=0)
        sexo_entry = tk.Entry(create_window)
        sexo_entry.grid(row=4, column=1)

        tk.Label(create_window, text="ID de Organización").grid(row=5, column=0)
        organizacion_id_entry = tk.Entry(create_window)
        organizacion_id_entry.grid(row=5, column=1)

        tk.Label(create_window, text="Apellido").grid(row=6, column=0)
        apellido_entry = tk.Entry(create_window)
        apellido_entry.grid(row=6, column=1)

        def submit():
            nombre = nombre_entry.get()
            direccion = direccion_entry.get()
            telefono = telefono_entry.get()
            fecha_nacimiento = fecha_nacimiento_entry.get()
            sexo = sexo_entry.get()
            organizacion_id = int(organizacion_id_entry.get())
            apellido = apellido_entry.get()
            cliente = Cliente(None, nombre, direccion, telefono, fecha_nacimiento, sexo, organizacion_id, apellido)
            self.controller.create_cliente(cliente)
            create_window.destroy()
            messagebox.showinfo("Info", "Cliente creado exitosamente")

        tk.Button(create_window, text="Crear", command=submit).grid(row=7, columnspan=2)

    def get_cliente(self):
        get_window = tk.Toplevel(self.root)
        get_window.title("Obtener Cliente")

        tk.Label(get_window, text="ID del Cliente").grid(row=0, column=0)
        cliente_id_entry = tk.Entry(get_window)
        cliente_id_entry.grid(row=0, column=1)

        def submit():
            cliente_id = int(cliente_id_entry.get())
            cliente = self.controller.get_cliente(cliente_id)
            if cliente:
                result = f"ID: {cliente.get_id()}\nNombre: {cliente.get_nombre()}\nDirección: {cliente.get_direccion()}\nTeléfono: {cliente.get_telefono()}\nFecha de Nacimiento: {cliente.get_fecha_nacimiento()}\nSexo: {cliente.get_sexo()}\nID de Organización: {cliente.get_organizacion_id()}\nApellido: {cliente.get_apellido()}"
                messagebox.showinfo("Cliente", result)
            else:
                messagebox.showerror("Error", "Cliente no encontrado")
            get_window.destroy()

        tk.Button(get_window, text="Obtener", command=submit).grid(row=1, columnspan=2)

    def get_all_clientes(self):
        clientes = self.controller.get_all_clientes()
        result = ""
        for cliente in clientes:
            result += f"ID: {cliente.get_id()} - Nombre: {cliente.get_nombre()} - Dirección: {cliente.get_direccion()} - Teléfono: {cliente.get_telefono()} - Fecha de Nacimiento: {cliente.get_fecha_nacimiento()} - Sexo: {cliente.get_sexo()} - ID de Organización: {cliente.get_organizacion_id()} - Apellido: {cliente.get_apellido()}\n"
        messagebox.showinfo("Todos los Clientes", result)

    def update_cliente(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Actualizar Cliente")

        tk.Label(update_window, text="ID del Cliente").grid(row=0, column=0)
        cliente_id_entry = tk.Entry(update_window)
        cliente_id_entry.grid(row=0, column=1)

        tk.Label(update_window, text="Nuevo Nombre").grid(row=1, column=0)
        nombre_entry = tk.Entry(update_window)
        nombre_entry.grid(row=1, column=1)

        tk.Label(update_window, text="Nueva Dirección").grid(row=2, column=0)
        direccion_entry = tk.Entry(update_window)
        direccion_entry.grid(row=2, column=1)

        tk.Label(update_window, text="Nuevo Teléfono").grid(row=3, column=0)
        telefono_entry = tk.Entry(update_window)
        telefono_entry.grid(row=3, column=1)

        tk.Label(update_window, text="Nueva Fecha de Nacimiento (YYYY-MM-DD)").grid(row=4, column=0)
        fecha_nacimiento_entry = tk.Entry(update_window)
        fecha_nacimiento_entry.grid(row=4, column=1)

        tk.Label(update_window, text="Nuevo Sexo (M/F)").grid(row=5, column=0)
        sexo_entry = tk.Entry(update_window)
        sexo_entry.grid(row=5, column=1)

        tk.Label(update_window, text="Nuevo ID de Organización").grid(row=6, column=0)
        organizacion_id_entry = tk.Entry(update_window)
        organizacion_id_entry.grid(row=6, column=1)

        tk.Label(update_window, text="Nuevo Apellido").grid(row=7, column=0)
        apellido_entry = tk.Entry(update_window)
        apellido_entry.grid(row=7, column=1)

        def submit():
            cliente_id = int(cliente_id_entry.get())
            cliente = self.controller.get_cliente(cliente_id)
            if cliente:
                cliente.set_nombre(nombre_entry.get())
                cliente.set_direccion(direccion_entry.get())
                cliente.set_telefono(telefono_entry.get())
                cliente.set_fecha_nacimiento(fecha_nacimiento_entry.get())
                cliente.set_sexo(sexo_entry.get())
                cliente.set_organizacion_id(int(organizacion_id_entry.get()))
                cliente.set_apellido(apellido_entry.get())
                self.controller.update_cliente(cliente)
                update_window.destroy()
                messagebox.showinfo("Info", "Cliente actualizado exitosamente")
            else:
                messagebox.showerror("Error", "Cliente no encontrado")

        tk.Button(update_window, text="Actualizar", command=submit).grid(row=8, columnspan=2)

    def delete_cliente(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Eliminar Cliente")

        tk.Label(delete_window, text="ID del Cliente").grid(row=0, column=0)
        cliente_id_entry = tk.Entry(delete_window)
        cliente_id_entry.grid(row=0, column=1)

        def submit():
            cliente_id = int(cliente_id_entry.get())
            self.controller.delete_cliente(cliente_id)
            delete_window.destroy()
            messagebox.showinfo("Info", "Cliente eliminado exitosamente")

        tk.Button(delete_window, text="Eliminar", command=submit).grid(row=1, columnspan=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteView(root)
    root.mainloop()
