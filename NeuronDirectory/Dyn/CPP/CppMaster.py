# importing FnMaster

from NeuronDirectory.Dyn.Fn import FnMaster

# -------------- Initializer------------------


# ---------------Functions ------------------

# ----------------Receive the payload deom IncomingMsg and send it to the CPP master
def message(Payload):
    # ------------ Test Print---------------
    print("CPP MASTER: ", Payload)
    # CPP -----------------------------------------------
    # multiple Dicts in Dyn list
    _data = Payload["Neuron"]  # parse the Dyn list
    # getting Data Dict --------------------------------
    Data = _data[1]  # fetching Data Dict from Dyn List
    # getting FnType ----------------------------------
    NeuronId = _data[0]  # fetching FnType Dict from Dyn List

    # ----- Print the results ----------------------------
    print("CPP Master : ")
    print(Data)
    print("--------------")
    print(NeuronId)
    FnMaster.message(NeuronId, Data )

