class Item:
    def __init__(self, id_item, nome, codigo, preço, tipo):
        self._id = id_item
        self._nome = nome
        self._codigo = codigo
        self._preço = preço
        self._tipo = tipo

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} Preço={1} Tipo={0}".format(self._tipo, self._preço, self._codigo,
                                                                             self._nome, self._id)
        return string

    def get_id(self):
        return self._id

    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_preço(self):
        return self._preço

    def set_nome(self, nome):
        self._nome = nome

    def set_preço(self, preço):
        self._preço = preço
