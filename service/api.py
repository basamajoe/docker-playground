# Amazon Service

# Importa marc de feina(framework)
from flask import Flask
from flask_restful import Resource, Api

# Instancia la aplicacio
app = Flask(__name__)
api = Api(app)

class Servei(Resource):
    def get(self):
        return {
            'products': ['Telefon', 'Portatil', 'Pantalla']
        }

# Crear mapeig
api.add_resource(Servei, '/')

# Executa la aplicacio
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
