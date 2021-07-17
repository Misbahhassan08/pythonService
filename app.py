# ------------------------ app.py Whole Neuron Starts from that Script ----------------------------------------------

# ------------------------Imports----------------------------
import os 
from flask import Flask, request
# ----------------------- Importing Global Initializer GniDyn

# app name -------------------------------------------------
app = Flask(__name__)


# routing --------------------------------------------------
@app.route('/')
def startApp():
    """ Return a friendly HTTP greeting. """
    who = request.args.get("who", "World")
    return f"Hello {who}!\n"
    pass

if __name__ == "__main__":
    from GNI import GniDyn
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
