import sys
import boto3
import pprint

t = sys.argv[1]
c = int(sys.argv[2])

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('app2.db')


resp = table.delete_item( Key={ 'type': t, 'count': c } )
pprint.pprint(resp)

