# ------------------------ app.py Whole Neuron Starts from that Script ----------------------------------------------

# ------------------------Imports----------------------------
import os 
from flask import Flask 
# ----------------------- Importing Global Initializer GniDyn

# app name -------------------------------------------------
app = Flask(__name__)


# routing --------------------------------------------------
@app.route('/')
def startApp():
    #from GNI import GniDyn
    from GNI import GniDyn
    print('Returning now...')
    return True
    pass

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
