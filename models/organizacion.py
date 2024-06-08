class Organizacion:
    def __init__(self, id, nombre, direccion):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_direccion(self, direccion):
        self._direccion = direccion
