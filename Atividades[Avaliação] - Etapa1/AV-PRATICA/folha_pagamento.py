from movimento_folha import MovimentoFolha
class FolhaPagamento:
    def __init__(self, mes, ano, total_descontos, total_proventos):
        self._mes = mes
        self._ano = ano
        self._total_descontos = total_descontos
        self._total_proventos = total_proventos
        self._lista_movimentos = []
        self._colaboradores = []
    def total_salario(self):
        total_salario = 0
        for colaborador in self._colaboradores:
            total_salario += colaborador.get_salario()
        return total_salario
    def inserir_movimento_fp(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._lista_movimentos.append(movimento)
    def set_colaborador(self, colaborador):
        self._colaboradores.append(colaborador)
    def calcular_folha(self):
        for movimento in self._lista_movimentos:
            if movimento.get_tipo().value == 1:
                self._total_proventos += movimento.get_valor()
            else:
                self._total_descontos += movimento.get_valor()
        total_pagar = (self.total_salario() + self._total_proventos) - self._total_descontos
        print('Total de Salários = {}\nTotal de Proventos = {}\nTotal de Descontos = {}\n''Total a Pagar = {}'.format(self.total_salario(), self._total_proventos, self._total_descontos, total_pagar))