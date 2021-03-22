from flask import Flask, request, jsonify
from _datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello() :
    
    print(datetime)
    return "hello world"

@app.route('/jsontest', methods = ['POST'])
def getJson() :
    requestData = request.get_json()
    return jsonify(requestData)


if __name__ == "__main__" :
    app.run(host='localhost',port='0000')


