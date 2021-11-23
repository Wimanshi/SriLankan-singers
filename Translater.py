from googletrans import Translator, constants

import json

translator = Translator()

converted = []
with open('Corpus/Singers_in_Sinhala.json', encoding="utf8") as f:
    data = json.load(f)

#singer_id_list = list(data.keys())
#print(singer_id_list)
i=0
for Name in data:
    obj = data[i]
    i=i+1
    print(Name)
    obj['Biography'] = translator.translate(obj['Biography'], dest='si').text
    obj['Songs'] = translator.translate(obj['Songs'], dest='si').text
    
    converted.append(obj)

out_file = open("Singers_in_Sinhala.json", "w", encoding='utf-8')
json_data = json.dump(converted, out_file, indent = 4, ensure_ascii=False)
