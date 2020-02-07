from src.storage.produto import ProdutoStorageList, ProdutoStorage
from src.models.base import ComplexResourceList, ItemList, Model

class ProdutoModel(Model):
    _param_id = 0
    _ID = 0
    _categoria = ""
    _descricao = ""
    _valor = 0.00
    _qtd_estoque = 0
    _imagem = ""
    _informacoes = ""

    def __init__(self, _id):
        self._param_id = _id
        item = ProdutoStorage().get_by_id(_id)        
        self._to_object(item)    
    
    def _to_object(self, _dict):
        self._ID = self._default_attr(_dict, 'id_produto', 0)
        self._categoria = self._default_attr(_dict, 'categoria', "")
        self._descricao = self._default_attr(_dict, 'descricao', "")
        self._valor = self._default_attr(_dict, 'valor', 0.00)
        self._qtd_estoque = self._default_attr(_dict, 'qtd_estoque', "")
        self._imagem = self._default_attr(_dict, 'nome_imagem', "")
        self._informacoes = self._default_attr(_dict, 'informacoes', "")


    def __repr__(self):
        if self._ID == 0:
            return None
        else:
            return {
                "type": "produto",
                "id": self._ID,
                "attributes": {
                    "categoria": self._categoria,
                    "descricao": self._descricao,
                    "valor": self._valor,
                    "qtd_estoque": self._qtd_estoque,
                    "imagem": self._imagem,
                    "informacoes": self._informacoes
                }
            }
   

class ProdutoItemModel(ItemList):
    _ID = 0
    _categoria = ""
    _descricao = ""
    _valor = 0.00
    _imagem = ""

    def __init__(self, _dict=None):
        self._to_object(_dict)
    
    def _to_object(self, _dict):
        self._ID = self._default_attr(_dict, 'id_produto', 0)
        self._categoria = self._default_attr(_dict, 'categoria', "")
        self._descricao = self._default_attr(_dict, 'descricao', "")
        self._valor = self._default_attr(_dict, 'valor', 0.00)
        self._imagem = self._default_attr(_dict, 'nome_imagem', "")


    def serialize(self):
        return  {
            "type": "produto",
            "id": self._ID,
            "attributes": {
                "categoria": self._categoria,
                "descricao": self._descricao,
                "valor": valor,
                "imagem": self._imagem
            }            
        }


class EstoqueIterator(ComplexResourceList):
    def __init__(self, order_by, pagina=1, por_pagina=25):
        if order_by is None:
            order_by = 'id_Produto'
        if pagina is None:
            pagina = 1
        if por_pagina is None:
            por_pagina = 25
        super().__init__(ProdutoStorageList, ProdutoItemModel, order_by, pagina, por_pagina)

    def _prepare_order_by(self, order_by):        
        fields = order_by.split(',')
        s = ""
        for name in fields:
            reverse = False
            if name[0] == '-':
                reverse = True
                name = name[1:]

            if name == 'descricao':
                s += 'p.descricao'
            elif name == 'categoria':
                s += 'c.categoria'
            elif name == 'valor':
                s += 'p.valor'
            else:
                s += 'p.id_produto'
                
            if reverse:
                s += " desc"
            s += ","
        return s[:-1] # retirando a ultima virgula
