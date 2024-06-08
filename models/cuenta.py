class Cuenta:
    def __init__(self, id, tipo, saldo_actual, saldo_medio, fecha_apertura, sucursal_id, cliente_id):
        self._id = id
        self._tipo = tipo
        self._saldo_actual = saldo_actual
        self._saldo_medio = saldo_medio
        self._fecha_apertura = fecha_apertura
        self._sucursal_id = sucursal_id
        self._cliente_id = cliente_id

    # Getters
    def get_id(self):
        return self._id

    def get_tipo(self):
        return self._tipo

    def get_saldo_actual(self):
        return self._saldo_actual

    def get_saldo_medio(self):
        return self._saldo_medio

    def get_fecha_apertura(self):
        return self._fecha_apertura

    def get_sucursal_id(self):
        return self._sucursal_id

    def get_cliente_id(self):
        return self._cliente_id

    # Setters
    def set_id(self, id):
        self._id = id

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_saldo_actual(self, saldo_actual):
        self._saldo_actual = saldo_actual

    def set_saldo_medio(self, saldo_medio):
        self._saldo_medio = saldo_medio

    def set_fecha_apertura(self, fecha_apertura):
        self._fecha_apertura = fecha_apertura

    def set_sucursal_id(self, sucursal_id):
        self._sucursal_id = sucursal_id

    def set_cliente_id(self, cliente_id):
        self._cliente_id = cliente_id
