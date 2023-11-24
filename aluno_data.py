'''construção do objeto de acesso a dados
instalar o pymysql
instalar o objeto de conexão'''

import pymysql.cursors
from aluno import Aluno

class AlunoData: # estebelece a conexão com o bando de dados.
    def __init__(self):
        self.conexao = pymysql.connect(host ='localhost',
                                       user ='root',
                                       password ='',
                                       database ='escola',
                                       cursorclass = pymysql.cursors.DictCursor) #para as pesquisa virem em formato de dicionarios.
        self.cursor =self.conexao.cursor() # para executar os comandos das querys.

    def insert (self, aluno:Aluno): #instancia aluno da classe Aluno, para iserir na tabela tem que criar o objeto a ser inserido.
        try:
            sql="INSERT INTO alunos VALUES (%s, %s,%s, %s,%s)"
            self.cursor.execute(sql, (aluno.matricula,aluno.nome,aluno.idade,aluno.curso,aluno.nota))
            self.conexao.commit() #salva as alterações.
        except Exception as error:
            print(f'Erro ao inserir ! Erro:{error}')


    def select (self): #lista todos os alunos.
        try:
            sql="SELECT *FROM alunos"
            self.cursor.execute(sql)
            alunos= self.cursor.fetchall()#fatia os alunos e coloca-os dentro de um dicionário (como linha)
            return alunos
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')


    def update (self, aluno:Aluno):#atualiza tabela.
        try:
            sql="UPDATE alunos SET nome= %s, idade =%s, curso=%s, nota=%s WHERE matricula =%s"
            self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota, aluno.matricula))
            self.conexao.commit() #salva as alterações
        except Exception as error:
            print(f'Erro ao atualizar! Erro {error}')





if __name__ == '__main__':
    ad=AlunoData() #criação do objeto de acesso a dados.
    #aluno=Aluno ('Jonas', 21, 'Python', 9.2) #criar o objeto aluno dentro da tabela
    #ad.insert(aluno)
    aluno=Aluno('Jonas Lopes',25, 'Java', 8.6)
    aluno.matricula='dd8730db-8a55-11ee-bff4-0ae0afa10843'
    ad.update(aluno)
    print(ad.select())
    #ad.update('Maria', 21,'Python',9.2,'dd8730db-8a55-11ee-bff4-0ae0afa10843')

