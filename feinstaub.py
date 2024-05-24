from http.server import BaseHTTPRequestHandler, HTTPServer
import json, threading, configparser, paho.mqtt.client as mqtt

config = configparser.ConfigParser()

config.read('feinstaub.conf')


def run_mqtt_client():      #Verbinden mit dem MQTT Server
    global client
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

    if config['MQTT']['auth'] == "true":
        client.username_pw_set(config['MQTT']['user'], config['MQTT']['password'])
        print("ping")

    client.on_connect = on_connect
    client.connect(config['MQTT']['ip'], int(config['MQTT']['port']), 60)
    client.loop_forever()

class PayloadHandler(BaseHTTPRequestHandler):       #Ankommende Payload verarbeiten
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data)
            formated_data = use_data(payload)
            formated_json = json.dumps(formated_data)
            client.publish("Feinstaub", formated_json)

            self.send_response(200)     #positiven http response senden
            self.end_headers()

        except Exception as e:
            self.send_response(400)     #negativen http response senden
            self.end_headers()

def on_connect(client, userdata, flags, rc):        #Wenn Broker verbunden
    print("connected")

def use_data(data):
    fields_str = config['data']['data_fields']
    fields = [item.strip() for item in fields_str.split(',')]

    values = []

    for sensor in data["sensordatavalues"]:         #extrahieren der daten aus der Json und einsetzung in array
        if sensor["value_type"] in fields:
            values.append(float(sensor["value"]))       

    json_data = {}      #erstellen des Json objekts
    
    for name, value in zip(fields, values):         #einsetzen der daten und der Namen in die neue Json
        json_data[name] = value

    json_string = json.dumps(json_data)

    return json_data

def run_http(server_class=HTTPServer, handler_class=PayloadHandler):  #Lässt den http server Laufen
    server_address = ('', int(config['http']['port']))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

http_thread = threading.Thread(target=run_http)      #Startet den http Server
http_thread.start()

mqtt_thread = threading.Thread(target=run_mqtt_client)      #Startet den MQTT teil
mqtt_thread.start()