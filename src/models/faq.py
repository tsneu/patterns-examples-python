from src.models.base import Model, SimpleResourceList, ItemList
from src.storage.faq import FaqStorageList, FaqStorage
from datetime import datetime


class FaqIterator(SimpleResourceList):
    @property
    def items(self):
        _itens = []
        for item in self._items:
            _itens.append(item.__repr__())
        return _itens
    
    def __init__(self, _id):
        super().__init__(_id, FaqStorageList, FaqItemModel)


class FaqItemModel(ItemList):
    _ID = 0
    _id_pergunta = 0
    _pergunta = ''
    _resposta = ''
    _nome_cliente = ''
    _nome_atendente = ''
    _email = ''
    _data_pergunta = ''
    _data_resposta = ''
    _cliente_aprova = False

    def _to_object(self, _dict):
        self._ID = self._default_attr(_dict, 'id_produto', 0)
        self._id_pergunta = self._default_attr(_dict, 'id_faq', 0)
        self._pergunta = self._default_attr(_dict, 'Pergunta', '')
        self._resposta = self._default_attr(_dict, 'Resposta', '')
        self._nome_cliente = self._default_attr(_dict, 'Usuario', '')
        self._nome_atendente = self._default_attr(_dict, 'Atendente', '')
        self._email = self._default_attr(_dict, 'Email', '')
        self._data_pergunta = self._default_attr(_dict, 'DtPergunta', '')
        if self._data_pergunta != '':
            self._data_pergunta = self._data_pergunta.strftime('%d/%m/%Y')
        self._data_resposta = self._default_attr(_dict, 'DtResposta', '')
        if self._data_resposta != '':
            self._data_resposta = self._data_resposta.strftime('%d/%m/%Y')
        self._ja_eh_cliente = self._default_attr(_dict, 'Cliente', False)
        if self._ja_eh_cliente:
            self._ja_eh_cliente = True 

    def serialize(self):
        return self

    def __repr__(self):
        if self._ID == 0:
            return None
        else:
            return {
                "type": 'faq',
                "id": self._ID,
                "attributes": {
                    "cliente": self._nome_cliente,
                    "atendente": self._nome_atendente,
                    "email": self._email,
                    "id_pergunta": self._id_pergunta,
                    "pergunta": self._pergunta,
                    "data_pergunta": self._data_pergunta,
                    "resposta": self._resposta,
                    "data_resposta": self._data_resposta,
                    "ja_eh_cliente": self._ja_eh_cliente
                }
            }


class FaqModel(Model):
    _ID = 0
    _produtoid = 0
    _nome = ""
    _email = ""
    _texto = ""

    def __init__(self, produtoid, nome, email, texto):
        super().__init__(0)
        self._ID = 0
        self._produtoid = produtoid
        self._nome = nome
        self._email = email
        self._texto = texto

    def _to_object(self, _dict):
        self._produtoid = self._default_attr(_dict, 'produtoid', None)
        self._nome = self._default_attr(_dict, 'nome', None)
        self._email = self._default_attr(_dict, 'email', None)
        self._texto = self._default_attr(_dict, 'texto', None)

    def __repr__(self):
        return  {
            "type": "disciplina",
            "id": str(self._ID),
            "attributes": {
                "produtoid": str(self._produtoid),
                "nome": self._nome,
                "email": self._email,
                "texto": self._texto
            }
        }
    
    def gravar(self):
        params = (self._produtoid, self._nome, self._email, self._texto)
        self._ID = FaqStorage().save(params)

