from flask_restful import Resource

lista_habildades = ['Python', 'Flask', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habildades
