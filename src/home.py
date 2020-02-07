import boto3
import json
from src.utils import error_message
from src.manager import Manager

def destaques(event, context):
    try:
        bucket = 'minhaloja.com'
        path = 'produto/destaques/'
        file_name = 'produtos_em_destaque.json'
        key = path + file_name
        config = Manager().config_db('s3files')

        s3 = boto3.client('s3',
                aws_access_key_id = config['key_id'],
                aws_secret_access_key = config['access_key']
            )
        content_object = s3.get_object(Bucket=bucket, Key=key)    
        file_content = content_object['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        return json_content
    except:
        return error_message('src/home', 'FileError', 'Destaques não encontrado')