from flask import Flask
from controllers.FuncionarioController import funcionarioBp
#from controllers import 

app = Flask(__name__)
app.register_blueprint(funcionarioBp)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=5000)