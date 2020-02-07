from src.utils import extract_params, error_message
from src.models.produto import EstoqueIterator, ProdutoModel
from src.exceptions import ParameterError

def lista(event, context):
    try:
        params = extract_params(event)
        order_by = params['sort'] if 'sort' in params else "id"
        pagina = int(params['page[number]']) if 'page[number]' in params else 1
        por_pagina = int(params['page[size]']) if 'page[size]' in params else 25
        model = EstoqueIterator(order_by, pagina, por_pagina)
        data = {
            "meta": {
                "totalPages": model.total_paginas
            },
            "data": [],
            "links": {
                "self": '/estoque?page[number]=' + str(pagina) + '&page[size]=25&sort=' + order_by
            }
        }

        if model.total_paginas > 0:
            data.update({"data": model.items})
            data["links"].update({                            
                "first": '/estoque?page[number]=1&page[size]=' + str(por_pagina) + '&sort=' + order_by,
                "prev": '/estoque?page[number]=' + str(model.prev) + '&page[size]=' + str(por_pagina) + '&sort=' + order_by,
                "next": '/estoque?page[number]=' + str(model.next) + '&page[size]='+ str(por_pagina) +'&sort=' + order_by,
                "last": '/estoque?page[number]=' + str(model.total_paginas) + '&page[size]=' + str(por_pagina) + '&sort=' + order_by,
            })
        return data
    except Exception as e:
        print('Error: ', e)
        return error_message('Estoque/lista', 'EstoqueError', e)


def get(event, context):
    try:
        params = extract_params(event)
        if 'id_produto' not in params:
            raise ParameterError('id_produto')

        id_produto = params['id_produto']
        dados = ProdutoModel(id_produto)
        return {
            "links": {
                "self": 'produto/' + str(id_produto),
                "videos": 'produto/' + str(id_produto) + '/videos'
            },
            "data": dados.__repr__()
        }

    except Exception as e:
        print('Error: ', e)        
        return error_message('produto/get', 'EstoqueError', e)