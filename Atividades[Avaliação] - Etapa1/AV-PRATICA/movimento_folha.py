class MovimentoFolha:
    def __init__(self, colaborador, descricao, valor, tipo_movimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipo_movimento = tipo_movimento
    def get_tipo(self):
        return self._tipo_movimento
    def get_valor(self):
        return self._valor