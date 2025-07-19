from tinydb import TinyDB
import json 
db = TinyDB("stations.json")
# json 파일을 읽어서 tinydb에 1개씩 추가

file = open("station_code.json", encoding="UTF8")
data = json.load(file)
itemlist = data["DATA"]
db.insert_multiple(itemlist)