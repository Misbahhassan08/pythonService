# ------------------------------- Fn1 Accept the 2 Dicts and send it to the CPC
# import -------------------------
from NeuronDirectory.Dyn.CPC import CpcMaster


# ----------------- Functions ---------------------------------

# --------------- Function rec values and send it to CPC
def Function(dict_NeuronId, dict_Data):
    print("FN1 : {} , {} ".format(dict_NeuronId, dict_Data))
    # creating Full Dict for CPC
    dict = {
        "Neuron": [
            {
                "NeuronId": " "
            },
            {
                "Data": [
                    {
                        "ID": 0,
                        "Address": 116,
                        "Byte": 4,
                        "Val": 1700
                    }
                ]
            }
        ]
    }
    print("FN1 : ",dict)
    # send to CPC Master
    CpcMaster.Function(dict)
    pass
