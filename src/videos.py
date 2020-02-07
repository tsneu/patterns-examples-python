from src.utils import extract_params, error_message
from src.models.videos import VideosIterator
from src.exceptions import ParameterError

def lista(event, context):
    try:
        params = extract_params(event)   
        if 'id_produto' not in params:
            raise ParameterError('id_produto')

        id_produto = params['id_produto']
        dados = VideosIterator(id_produto)   
        result = dict()
        result = {
                "links":{
                    "self": '/produto/' + str(id_produto) + '/videos'
                },
                "data": dados.items
            }
        return result

    except Exception as e:
        print('Error: ', e)
        return error_message('/videos/lista', 'VideosError', e)