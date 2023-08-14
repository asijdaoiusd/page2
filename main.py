from flask import Flask

from endpoints.renaper.sifcop import sifcop_bp 

app = Flask(__name__)

app.register_blueprint(sifcop_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
