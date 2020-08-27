
import json
def load():
    ex = []
    with open('../static/city.list.json',encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            if i.get("id") == 833:
                print(i)
            ex.append({"model":"weather.city",
                       "pk":i.get("id"),
                       "fields": {
                            "name":i.get("name"),
                            "coord_lon":i.get("coord").get("lon"),
                            "coord_lat":i.get("coord").get("lat")
                       }})
    with open('../static/my_data.json', 'w', encoding='utf-8') as file:
        json.dump(ex, file,ensure_ascii=False)

load()