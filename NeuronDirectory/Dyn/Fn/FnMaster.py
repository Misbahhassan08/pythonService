# ---------------------- FnMaster For accessing all other scripts and Init

# ----------------------------------- Imports --------------------------------
from NeuronDirectory.Dyn.CPC import CpcMaster
from NeuronDirectory.Dyn.Fn import Fn1


# -------------------- Functions ----------------------------------------------
# message function receives the data from Cpcmaster and send it to the required script and the return value which is
# comming from respected scripts will send it to CPCmaster
def message(dict_NeuronId, dict_Data):
    print("FN Master : {} , {} ".format(dict_NeuronId, dict_Data))
    Fn1.Function(dict_NeuronId, dict_Data)  # sending Dicts to Fn1
