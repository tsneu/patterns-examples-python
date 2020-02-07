class ParameterError(Exception):
    def __init__(self, name=None):
        if name == '':
            self.msg = 'Nenhum parâmetro foi informado'
        else:
            self.msg = 'O parâmetro *' + name + '* não foi informado.'

    def __str__(self):
        return self.msg


class DataBaseError(Exception):

    def __init__(self, tipo, detail=None):
        if tipo == 'connection':
            self.msg = 'Nao foi possivel conectar ao banco de dados'
        elif tipo == 'query':
            self.msg = 'Ocorreu algum erro: *' + detail + '*. Informe o desenvolvedor.'
        else:
            self.msg = 'Ocorreu algum erro no banco de dados. Informe o desenvolvedor.'

    def __str__(self):
        return self.msg