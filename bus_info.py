import requests
from flask import Flask, render_template, send_file, request
import pprint
from tinydb import TinyDB
import config
service_key = config.SERVICE_KEY
url = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid"
url2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByName"
app = Flask("버스 도착정보 서비스")

db = TinyDB('stations.json')
st = db.all()
b_blue = "businformation_static/static/bus_blue@400.png"
b_red = "businformation_static/static/bus_red@400.png"
b_gray = "businformation_static/static/bus_gray@400.png"
b_green = "businformation_static/static/bus_green@400.png"
b_yellow = "businformation_static/bus_yellow@400.png"
url2 = "http://ws.bus.go.kr/api/rest/stationinfo/getStationByName"
stations = []
for s in st:
    stations.append([s["stop_nm"], s["stop_no"]])

def get_info(code):
    bus = []
    params = {
        "serviceKey": service_key,
        "arsId": code,
        "resultType": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        r_obj = response.json()
        # pprint.pprint(r_obj)
        items = r_obj['msgBody']['itemList']
        for i in items:
            if i['routeType'] == '6':
                bus.append(["bus_red", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
            if i['routeType'] == '3':
                bus.append(["bus_blue", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
            if i['routeType'] == '4':
                bus.append(["bus_green", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
            if i['routeType'] == '5':
                bus.append(["bus_yellow", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
            if i['routeType'] == '1':
                bus.append(["bus_yellow", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
            if i['routeType'] == '2':
                bus.append(["bus_green", i['busRouteAbrv'],i['arrmsg1'], i['arrmsg2']])
        return bus

# bus = get_info(25140)
# print(bus)
@app.route("/")
def main():
    return render_template("index.html", bus=[], st = stations)

@app.route("/search", methods=["POST"])
def search():
    station = request.form["station"]
    bus = get_info(station)
    return render_template("index.html", bus=bus, st = stations)

app.run(port=5000)