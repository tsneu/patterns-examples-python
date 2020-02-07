from abc import ABC, abstractmethod

class AbstractStorageBase(ABC):

    @abstractmethod
    def query(self, sql, params):
        pass

    @abstractmethod
    def query_simple(self, sql):
        pass


class AbstractComplexStorageList(AbstractStorageBase):

    @abstractmethod
    def get_by_params(self, order_by, pagina, por_pagina):
        pass

    @abstractmethod
    def get_total_registros(self):
        pass


class AbstractStorageSimpleList(AbstractStorageBase):

    @abstractmethod
    def get_by_parentid(self, id):
        pass


class AbstractStorage(AbstractStorageBase):

    @abstractmethod
    def get_by_id(self, id):
        pass

