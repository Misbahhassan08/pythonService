# -------------------------Cpcmaster For accessing all other scripts and Init

# ---------------------------------imports---------------------------------------

from NeuronDirectory.Dyn.Msg.OutgoingMsg import OutgoingMsg

# -----------------------------------Initialize ---------------------------------

NeuronId = "Hello World"

# --------------------------------Functions ------------------------------------- message Function receives the


# ------------------ Receive the Dict from Fn1
def Function(Dict):

    Dict["Neuron"][0]["NeuronId"] = "Hello World"
    print("CPC Master: ", Dict)
    # ---- calling OutgoingMsg Function msg with Dict parameter
    OutgoingMsg.msg(Dict)
"""
{
    "Dyn": [
        {
            "NeuronId": "Dyn"
        },
        {
            "FnType": "Fn5"
        },
        {
            "Data": [
                {
                    "ID": 0,
                    "Address": 116,
                    "Byte": 4,
                    "Val": 1700
                },
                {
                    "ID": 1,
                    "Address": 116,
                    "Byte": 4,
                    "Val": 1600
                }
            ]
        }
    ]
}
"""
