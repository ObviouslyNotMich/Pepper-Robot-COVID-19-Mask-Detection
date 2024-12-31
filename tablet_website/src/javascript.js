mqttClient = new MQTTClient(
          {
            clientId: 'niewols',
            host: 'mqtt.hva-robots.nl',
            port: 443,
            username: 'niewols',
            password: 'hzD7KrOhih5gO0lVdjCZ'
        }, this.scope);

        mqttClient.connect();
        mqttClient.subscribe("niewols/website")

        mqttClient.on('connected', function () {
            console.log('connected');
        });

        mqttClient.on('connectionLost', function () {
            console.log('ConnectionLost');
        });

        mqttClient.on('message', function (topic, message) {
            console.log(message.toString())
        })

function start() {
    mqttClient.publish("niewols/website","start")
}
function stop() {
    mqttClient.publish("niewols/website","stop")
}
function Surveillance_mode() {
    mqttClient.publish("niewols/website","surveillance_mode")
}
function Entrance_mode() {
    mqttClient.publish("niewols/website","entrance_mode")
}