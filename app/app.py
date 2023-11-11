from flask import Flask, jsonify, request

app = Flask(__name__)

#mudar o código
@app.route('/')

def index():
    return '<h1>Hello, World!</h1>', 200
if __name__ == '_main_':
 app.run(port=8080,host='localhost',debug=false)