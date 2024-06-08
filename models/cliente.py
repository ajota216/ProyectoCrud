class Cliente:
    def __init__(self, id, nombre, direccion, telefono, fecha_nacimiento, sexo, organizacion_id, apellido):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._organizacion_id = organizacion_id
        self._apellido = apellido

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_direccion(self):
        return self._direccion

    def get_telefono(self):
        return self._telefono

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def get_sexo(self):
        return self._sexo

    def get_organizacion_id(self):
        return self._organizacion_id

    def get_apellido(self):
        return self._apellido

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_direccion(self, direccion):
        self._direccion = direccion

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def set_sexo(self, sexo):
        self._sexo = sexo

    def set_organizacion_id(self, organizacion_id):
        self._organizacion_id = organizacion_id

    def set_apellido(self, apellido):
        self._apellido = apellido
