from models import Pessoas
def insere():
    pessoa = Pessoas(nome='Hugo', idade=25)
    pessoa.save()
    print(pessoa)

def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)

def altera():
    pessoa = Pessoas.query.filter_by(nome='Victor').first()
    pessoa.nome = 'Victorr'
    pessoa.save()

def excluir():
    pessoa = Pessoas.query.filter_by(nome='Hugo').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere()
    #altera()
    excluir()
    consulta()