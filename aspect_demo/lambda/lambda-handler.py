def main(event, context):
    print("request: {}".format(json.dumps(event)))

    return {
        'statusCode': 200,
        'header': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello {}! you have hit \n'.format(event['queryStringParameter']['name'])
    }