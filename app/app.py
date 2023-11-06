from flask import Flask, jsonify, request

app = Flask(__name__)

#exemplo aqui embaixo (mudar depois da pergunta)
@app.route('/')

def index():
    return '<h1>Hello, World!</h1>', 200
if __name__ == '_main_':
 app.run(port=8080,host='localhost',debug=false)