from abc import ABC, abstractmethod
from math import ceil

class AbstractComplexResourceList(ABC):    
    _items = []
    _pagina = 1
    _por_pagina = 25
    _total_regs = None
    _order_by = ""
    _storage = None
    
    @property
    def items(self):
        return self._items

    @property
    def total_paginas(self):
        if self._total_regs is None:
            dados = self._storage().get_total_registros()
            self._total_regs = int(dados['Count'])
        return ceil(self._total_regs / self._por_pagina)
       
    @property
    def prev(self):
        if self._pagina == 1:
            return 1
        else:
            return self._pagina -1

    @property
    def next(self):
        tp = self.total_paginas
        if self._pagina == tp:
            return self._pagina
        else:
            return self._pagina + 1
       

    @abstractmethod
    def __init__(self, storage, resource, order_by, pagina=1, por_pagina=25):
        super().__init__()        

    @abstractmethod
    def _prepare_order_by(self, order_by):
        pass


class AbstractSimpleResourceList(ABC):
    _items: []

    @property
    def items(self):
        return self._items
    
    @abstractmethod
    def __init__(self, id, storage, resource):
        self._items = []


class AbstractItemList(ABC):
    @abstractmethod
    def _default_attr(self, obj, field, value):
        pass    

    @abstractmethod
    def _to_object(self, _dict):
        pass

    @abstractmethod
    def serialize(self):
        pass


class AbstractModel(ABC):
    @abstractmethod
    def _default_attr(self, obj, field, value):
        pass    

    @abstractmethod
    def _to_object(self, _dict):
        pass

    @abstractmethod
    def __repr__(self):
        pass
