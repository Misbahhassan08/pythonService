# ---------------------- Outgoingmsg Receives the Json payload from CPCmaster and send it to Next neuron Id address

# ----------------------- imports ---------------------------------
import json
import paho.mqtt.client as mqtt

# ------------------------ Paho Initialize -------------------------

mqttc = mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)
Topic = "Robotid/Neuronid/Outgoing"


# ----------------- paho functions -------------------------------
# ---------------- When paho Connect to Mqtt----------------------
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


# ---------------- When paho is publish---------------------------
def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# Sending payload to required Neuron By Publishing it to Subscriber one
def msg(Payload):
    # Global
    global mqttc
    global topicPub

    data = json.dumps(Payload)
    print("OutgoingmsgDyn : ",data)
    (rc, mid) = mqttc.publish(Topic, data)  # publishing
    print('{}, {}'.format(rc, mid))
    pass
