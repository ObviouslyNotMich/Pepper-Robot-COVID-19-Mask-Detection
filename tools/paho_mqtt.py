import paho.mqtt.client as mqtt
import json
import string
import random


class PahoMqtt:
    pepper = session = clients = None

    def __init__(self, pepper):
        self.pepper = pepper
        self.session = pepper.session
        self.clients = []

        for i in json.loads(open('tools/clients.json', "r").read())['clients']:
            try:
                client = mqtt.Client(self.id_generator())
                client.username_pw_set(i["user"], i["pw"])

                client.on_connect = self.on_connect
                client.on_message = self.on_message

                client.connect(i["host"], i["port"])
                client.loop_start()
            except RuntimeError, e:
                print ("Couldn't create client: ", i["name"])

    def on_connect(self, client, userdata, flags, rc):
        if rc == 4:
            print("Connection attempt failed to mqtt broker with result code " + str(rc))
        if rc == 0:
            print("Connected to mqtt broker with result code " + str(rc))
            client.subscribe([("niewols/website", 0), ("robots/mirai/scan", 0)])

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        self.pepper.mqtt_msg = msg.payload

        return str(msg.payload)

    def id_generator(self, size=12, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
