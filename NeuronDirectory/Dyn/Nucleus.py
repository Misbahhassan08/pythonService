# ---------------------------------- Bridge.py The Nucleus of whole Neuron Connects with IncomingMsg, CppMaster,
# FnMaster, CpcMaster and OutgoingMsg
# -------------------Imports------------------------------------------------------------
from NeuronDirectory.Dyn.Msg.IncomingMsg import IncomingMsg

# ------------------------------ Initializer -----------------------------------------


# ----------Print test-----------------------------------------------------------------
print("Bridge: Code is Running ")

# run the incommingMsg from calling function
IncomingMsg.startLoop()
