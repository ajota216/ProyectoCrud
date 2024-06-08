class Empleado:
    def __init__(self, id, nombre, direccion, telefono, ciudad, sucursal_id, apellido, correo):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._ciudad = ciudad
        self._sucursal_id = sucursal_id
        self._apellido = apellido
        self._correo = correo

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    def get_telefono(self):
        return self._telefono

    def get_ciudad(self):
        return self._ciudad

    def get_sucursal_id(self):
        return self._sucursal_id

    def get_apellido(self):
        return self._apellido

    def get_correo(self):
        return self._correo

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_direccion(self, direccion):
        self._direccion = direccion

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def set_sucursal_id(self, sucursal_id):
        self._sucursal_id = sucursal_id

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_correo(self, correo):
        self._correo = correo
