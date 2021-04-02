#!/usr/bin/python3

# import our Flask class
from flask import Flask
from flask import jsonify

app = Flask(__name__)

# return a simple string
@app.route("/", methods = ['GET'])
def citihome():
    return "Hello Citi Group Students!"

# perform some math
@app.route("/math", methods = ['GET'])
def math():
    x = 5
    y = 2
    answer = x + y
    return str(answer)

@app.route("/json", methods = ['GET'])
def jsonmaker():
    webster = {'a1': 'ant', 'b2': 'badger', 'c3': ['cat', 'cadipillar'], 'd4': None}
    return jsonify(webster)

if __name__ == '__main__':
    # run our flask application on all IPs:2224
    app.run(host="0.0.0.0", port=2224)
