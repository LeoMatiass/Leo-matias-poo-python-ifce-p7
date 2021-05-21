from movimento_folha import MovimentoFolha
class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salario_atual = salario_atual
        self._lista_movimentos = []
    def get_salario(self):
        return self._salario_atual
    def calcular_salario(self):
        total_proventos = 0
        total_descontos = 0
        for movimento in self._lista_movimentos:
            if movimento.get_tipo().value == 1:
                total_proventos += movimento.get_valor()
            else:
                total_descontos += movimento.get_valor()
        salario_liquido = self._salario_atual + total_proventos - total_descontos
        print('Código: {}\nNome: {}\nSalário: {}\nTotal proventos: {}\n'
              'Total descontos: {}\nValor líquido a receber: {}\n'.format(self._codigo, self._nome, self._salario_atual, total_proventos, total_descontos, salario_liquido))
    def inserir_movimentos_colab(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self._lista_movimentos.append(movimento)