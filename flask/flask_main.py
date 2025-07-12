from flask import Flask, request
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)  #Flask app
CORS(app)  #add CORS
#app.config['DEBUG'] = True  #debug mode

#ProjectName = ""
ProjectName = "/MyWebAPI"

@app.route(ProjectName + "/", methods=['GET'])
def Hello():
  return '<h1>Hello, My Flask</h1>'  #hello response

@app.route(ProjectName + "/ResponseData", methods=['POST'])
def ResponseData():
  try:
    requestData = request.get_json()  #get request data from client
    receivedData = requestData["SendData"]  #get JSON data
    responseMsg = {"ReturnMsg": receivedData}  #compose response message
    return responseMsg  #return response message
  except Exception as err:
    responseMsg = {"ReturnMsg": str(err)}  #exception message
    return responseMsg  #return response message

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  #serve(app, host="0.0.0.0", port=5000, threads=5)  #run waitress server  