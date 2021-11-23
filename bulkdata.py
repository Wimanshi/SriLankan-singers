from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json


es = Elasticsearch()

INDEX = 'srilankansingersdatabase'
TYPE = 'singers'

converted = []
with open('Corpus/Singers_in_Sinhala.json', encoding='utf-8') as f:
    data = json.load(f)

singer_objs = []

for singer in data:
    obj = {}
    
    print(singer['Name'])
    
    obj['name'] = singer['Name']
    obj['dob'] = singer['Birth Date']
    obj['city'] = singer['City']
    obj['bio'] = singer['Biography']
    obj['lyrics'] = singer['Lyrics of a song']
    obj['songs'] = singer['Songs']
    obj['email'] = singer['email']
    singer_objs.append(obj)

actions = []
i = 1

for obj in singer_objs:
    actions.append({
        "_index": INDEX,
        "_type": TYPE,
        "_id": i,
        "_source": obj
    })
    i += 1

helpers.bulk(es, actions)
