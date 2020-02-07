def extract_params(event):
    params = []
    if 'path' in event and event['path']:
        params = event['path']
    elif 'query' in event and event['query']:
        params = event['query']    
    elif 'body' in event:
        params = event['body']

    return params

def error_message(pointer, title, detail):
    return {
            "errors": [
                {
                    "source": {"pointer": pointer},
                    "title": title,
                    "detail": str(detail)
                }
            ]
        }