from src.storage.base import Storage, ComplexStorageList, StorageSimpleList

class ProdutoStorageList(ComplexStorageList):

    def get_by_params(self, order_by, pagina, por_pagina):
        sql = """
            SELECT p.id_produto, c.descricao as categoria, p.descricao, p.valor,p.nome_imagem
            from produto p
                left join categoria as c on c.id_categoria = p.id_categoria
            where p.situacao = 'A'
            order by """ + order_by + """
            OFFSET %s ROWS
            FETCH NEXT %s ROWS ONLY            
            """
        offset = por_pagina * (pagina - 1)
        self.query(sql, (offset, por_pagina,))
        return self.db_cursor.fetchall()

    def get_total_registros(self):
        sql = "select count(*) as Count from produto where situacao = 'A'"
        self.query_simple(sql)
        return self.db_cursor.fetchone()

class ProdutoStorage(Storage):

    def get_by_id(self, id_produto):
        sql = """
            select p.id_produto, c.descricao as categoria, p.descricao, p.valor, 
                p.nome_imagem, p.informacoes
            from produto p
                left join categoria c on c.id_categoria = p.id_categoria
            where 
                p.id_produto = %s
                and p.situacao = 'A'"""

        self.query(sql, (id_produto,))
        return self.db_cursor.fetchone()


class VideoStorageList(StorageSimpleList):
    
    def get_by_parentid(self, id_produto):
        sql = "SELECT id_video, titulo, link_web from produto_video_youtube where id_produto = %s"
        self.query(sql, (id_produto,))
        return self.db_cursor.fetchall()

 