from flask import Flask
from controllers.FuncionarioController import funcionarioBp
from controllers.CiclistaController import ciclistaBp 
from controllers.CartaoController import cartaoBp

app = Flask(__name__)
app.register_blueprint(funcionarioBp)
app.register_blueprint(ciclistaBp)
app.register_blueprint(cartaoBp)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=5000)