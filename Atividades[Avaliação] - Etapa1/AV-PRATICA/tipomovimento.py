import enum
class TipoMovimento(enum.Enum):
    P = 1
    D = 2
if __name__ == '__main__':
    print(TipoMovimento.P.value)