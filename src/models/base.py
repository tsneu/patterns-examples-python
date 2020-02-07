from src.abstract.resources import *

class ComplexResourceList(AbstractComplexResourceList):

    def __init__(self, storage, resource, order_by, pagina=1, por_pagina=25):
        self._items = []
        self._pagina = pagina
        self._por_pagina = por_pagina
        self._order_by = self._prepare_order_by(order_by)
        self._storage = storage
        dados = storage().get_by_params(self._order_by, self._pagina, self._por_pagina)
        for row in dados:
            item = resource(row)
            self._items.append(item.serialize())  


    def _prepare_order_by(self, order_by):
        pass



class SimpleResourceList(AbstractSimpleResourceList):
    _items = []
    
    def __init__(self, _id, requester, resource):
        self._items = []
        q = requester()
        dados = q.get_by_parentid(_id)        
        for row in dados:
            store = resource()
            store._to_object(row)
            self._items.append(store.serialize())


class ItemList(AbstractItemList):
    
    def _default_attr(self, obj, field, value):
        if not(obj):
            return value
        elif field not in obj:
            return value
        elif obj[field] == None:
            return value
        else:            
            return obj[field]


    def _to_object(self, _dict):
        pass


    def serialize(self):
        pass



class Model(AbstractModel):

    def __init__(self, id):
        pass 

    def _to_object(self, _dict):
        pass

    def __repr__(self):
        pass

    def _default_attr(self, obj, field, value):
        if not(obj):
            return value
        elif field not in obj:
            return value
        elif obj[field] == None:
            return value
        else:
            return obj[field]
