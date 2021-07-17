# -------------------------- IncomingMsg Receive the message from Mqtt-paho -----------------------------------------

# ---------------------------imports----------------------
import json
import paho.mqtt.client as mqtt
from NeuronDirectory.Dyn.CPP import CppMaster

# ------------------------------Initializer---------------

Sub = mqtt.Client()  # Sub_c1 is for Payload
Sub.connect("test.mosquitto.org", 1883, 60)  # Connecting Sub to mosquitto

Payload = None  # Payload Variable

Topic = "Robotid/Neuronid/Incoming"  # Topic Address Variable


# MsgIncomming Function Sends Payload to
# CppMster----------------------------------------------------

def msgtocpp():
    # ----- Globals
    global Payload

    # if Payload is not None:
    # Send this payload to CPP
    if Payload is not None:
        # Test print for Checking Payload
        print("IncomingMsg :  ", Payload)
        # send payload to cpp
        CppMaster.message(Payload)
        # Clear the Payload Variable
        Payload = None
    else:
        # If there is no Payload then it prints
        print("Msgtocpp : Payload is None")
        pass


# ------------ ------Paho Client Functions-------------------------------
# The Threaded Function which is always scanning/Ready to receive new messages from Mqtt-Paho for Client
def on_message(mqttc, obj, msg):
    # ----------- Globals---------
    global Payload

    # -Receive the payload from mqtt and save it to the global Payload variable
    _Payload = msg.payload.decode('utf-8')
    Payload = json.loads(_Payload)
    # calling msgtocpp function, to send the Payload from Incomming Msg to CPP master Script
    msgtocpp()


# --------- When Sun_c2 is connected
def on_connect(mqttc, obj, flags, rc):
    print(" Client is connected and rc: " + str(rc))


# ---------- When Sub_c2 is Subscribed
def on_subscribe(mqttc, obj, mid, granted_qos):
    print(" Client is Subscribed: " + str(mid) + " " + str(granted_qos) + " " + str(obj) + " " + str(mqttc))


# --------- Initialize the Sub functions with proper function explain
Sub.on_message = on_message
Sub.on_connect = on_connect
Sub.on_subscribe = on_subscribe
Sub.subscribe(Topic, 1)
Sub.loop_start()
# -- Test Print to check whole Neuron works perfectly fine
print("All Done")


# To start the neuron we need infinite loop at the end
def startLoop():
    # pass
    while True:
        pass
