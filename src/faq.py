from src.models.faq import FaqIterator, FaqModel
from src.validate.faq import FaqSchema
from src.utils import extract_params, error_message
from src.exceptions import ParameterError, DataBaseError
from marshmallow import ValidationError

def get(event, context):
    params = extract_params(event)    
    if 'id_produto' not in params:
        raise ParameterError('id_produto')

    id_produto = params['id_produto']
    dados = FaqIterator(id_produto)
    result = {
        "links":{
            "self": '/faq/' + str(id_produto)
        },
        "data": dados.items
    }
    
    return result


def add(event, context):
    try:
        params = extract_params(event)
        if not(params):
            raise ParameterError('')
        # validar parametros        
        schema = FaqSchema()
        validados = schema.load(params)
        dados = schema.dump(validados)        
        model = FaqModel(**dados)
        model.gravar()
        return {
            "links": { "links": "/faq/create" },
            "data": model.__repr__()
        }
    except ValidationError as err:
        return {
            "errors": {
                "title": "ParameterError",
                "detail": err.messages
            }
        }
    except ParameterError as err:
        return error_message('/faq/create', 'ParameterError', err)
    
    except DataBaseError as err:
        return error_message('/faq/create', 'DataBaseError', err)

    except Exception as err:
        return error_message('/faq/create', 'GeneralError', err)

