from src.storagperg.base import StorageSimpleList, Storage, getdate

class FaqStorageList(StorageSimpleList):

    def get_by_parentid(self, parent_id):
        sql = """
                select
                    perg.id_produto, 
                    perg.id_faq, 
                    perg.nome [Usuario], 
                    resp.nome [Atendente], 
                    perg.email, 
                    perg.texto [Pergunta], 
                    resp.texto [Resposta], 
                    perg.dt_cadastro [DtPergunta], 
                    resp.dt_cadastro [DtResposta], 
                    perg.cliente 
                from Faq perg 
                    left join Faq resp on resp.id_faq_pai = perg.id_pergunta 
                where perg.situacao = 'A' and 
                    perg.status = 'A' and 
                    perg.id_produto = %s and 
                    perg.id_faq_pai is null 
                order by perg.id_faq, perg.dt_cadastro desc"""
        
        self.query(sql, (parent_id,))
        return self.db_cursor.fetchall()


class FaqStorage(Storage):

    def get_by_id(self, _id):
        pass

    def save(self, params):
        hoje = getdate().strftime('%Y-%m-%d %H:%M:%S')
        # Situação: A = Ativo, I = Inativo
        # Status: 'M' = Moderacao (aguardando resposta)
        params += ('A', 'M', hoje, hoje)
        sql = """insert into Faq 
                (id_produto, nome, email, texto, situacao, status, dt_cadastro, dt_alteracao)
                values (%d, %s, %s, %s, %s, %s, %s, %s)"""
                
        self.query(sql, params)
        self.db_connection.commit()
        return self.db_cursor.lastrowid