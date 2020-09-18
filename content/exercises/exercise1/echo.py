# load Flask 
import flask
from googletrans import Translator

app = flask.Flask(__name__)


# define a predict function as an endpoint 
@app.route("/predict", methods=["GET", "POST"])
def predict():
    data = {"success": False}

    # get the request parameters
    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, echo the msg parameter 
    if (params != None):
        translator = Translator()
        data["language"] = "Spanish"
        data["response"] = params.get("msg")
        translated_text = translator.translate(data["response"], src='en', dest="es")
        data["translated_text"] = translated_text.text
        data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)


# This allows for unicode characters in the response
app.config['JSON_AS_ASCII'] = False

# start the flask app, allow remote connections
app.run(host='0.0.0.0')
