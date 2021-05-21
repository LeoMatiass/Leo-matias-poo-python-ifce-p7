from produto import Produto
class ItemNotaFiscal:
    def __init__(self, id, sequencial, quantidade, produto):
        self._id = id
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = produto
        self._descricao = self._produto.getDescricao()
        self._valorUnitario = self._produto.getValorUnitario()
        self._valorItem = float(self._quantidade * self._valorUnitario)
    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self._valorItem,
            self._valorUnitario,
            self._descricao,
            self._quantidade,
            self._sequencial,
            self._id)
        return string
    def get_valor_item(self):
        return self._valorItem
    def get_sequencial(self):
        seq = str(self._sequencial)
        if len(seq) > 2:
            return seq
        elif len(seq) > 1:
            return f'0{seq}'
        return f'00{seq}'
    def get_descricao(self):
        return self._descricao
    def get_quantidade(self):
        return self._quantidade
    def get_valor_unitario(self):
        return self._valorUnitario
if __name__ == '__main__':
    produto1 = Produto(1, 100, 'Arroz', 5.5)
    item = ItemNotaFiscal(1, 1, 12, produto1)
    print(item.str())