# feinstaubsensor4MQTT
Verbindet den https://opensensemap.org Feinstaubsensor mit MQTT per custom Api

# Anwendung

Zu allererst musst du in die feinstaub.conf den port und die pi deines MQTT brokers eintragen.

Als nächstes musst du herausfinden welche daten du überhaupt haben willst, dafür hilft dir das read.py script. stelle auf deinem Feinstaub Sensor eine Custom Api ein (Konfiguration/APIs/an eigene API senden). Als ip gibst du die adresse deies Servers/computers an, auf dem das Script Läuft. Danach nicht vergessen zu speichern und neu zu starten.

Starte anschließend das Python script, und warte bis die ersten Daten ankommen. Aus dieser Liste an namen kann man sich jetzt die jenigen raus suchen, die einen interessieren. In meinem Fall waran dass SDS_P1, SDS_P2, BME280_temperature, BME280_pressure und BME280_humidity.

Wenn du deine Auswahl getroffen hast, kehrtst du zurück zur feinstaub.conf. Trage nun alle namen in die data_fields ein, nur mit einem Komma getrennt.

nun kannst du feinstaub.py starten. Jetzt sollten schon daten auf deinem MQTT-Broker ankommen.

# Sonstiges

Bei Problemen und wünschen stehe ich jederzeit zur Verfügung.
