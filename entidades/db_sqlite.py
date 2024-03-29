import sqlite3

class DBSqlite():

    def __init__(self):
        try:
            self.conn = sqlite3.connect("database/alunos.db")
            self.cursor = self.conn.cursor()
        except Exception as err:
            print("[ __init__ DBSqlite ] :", err)


    def create_table_alunos(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS alunos (
                    id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome_aluno TEXT(250) NOT NULL,
                    n1 REAL NOT NULL,
                    n2 REAL NOT NULL,
                    n3 REAL NOT NULL,
                    n4 REAL NOT NULL,
                    media REAL NOT NULL,
                    situacao INTEGER not null
                );
            """)
        except Exception as err:
            print("[ __init__ ERROR ] :", err)
            return False
        else:
            self.conn.close()
            return True
                

    def get_alunos(self):
        try:
            self.cursor.execute("SELECT * FROM alunos;")
            alunos = self.cursor.fetchall()
        except Exception as err:
            print("[ get_conncet ERROR ] :", err)
        else:
            self.conn.close()
            return alunos

    
    def get_aluno_by_id(self, id_aluno):
        try:
            self.cursor.execute(
                "SELECT * FROM alunos WHERE id_aluno = {};".format(id_aluno)
            )
            aluno = self.cursor.fetchone()
        except Exception as err:
            print("[ get_conncet ERROR ] :", err)
        else:
            self.conn.close()
            return aluno


    def calcula_media(self, *notas):
        return (sum(notas))/4


    def insert_aluno(self, nome, n1, n2, n3, n4):
        try:
            media = self.calcula_media(
                    float(n1), float(n2), float(n3), float(n4)
                )
            situacao = self._verifica_situacao_aluno(media)
            self.cursor.execute(
                """
                INSERT INTO alunos (nome_aluno, n1, n2, n3, n4, media, situacao) 
                VALUES ('{nome}', {n1}, {n2}, {n3}, {n4}, {media}, {situacao});
                """.format(
                        nome=nome,
                        n1=n1,
                        n2=n2,
                        n3=n3,
                        n4=n4,
                        media=media,
                        situacao=situacao
                    )
            )
        except Exception as err:
            print("[ insert_aluno ERROR ] :", err)
            self.conn.close()
            return False
        else:
            self.conn.commit()
            self.conn.close()
            return True

    def _verifica_situacao_aluno(self, media):
        if media >= 8:
            return 1 #Aprovado
        elif media < 5:
            return 2 #Reprovado
        elif media >= 5 and media < 8:
            return 3 #Em recuperação


    def excluir_aluno(self, id_aluno):
        try:
            self.cursor.execute("""DELETE FROM alunos WHERE id_aluno = {};""".format(id_aluno))
        except Exception as err:
            print("[ excluir_aluno ERROR ] :", err)
            self.conn.close()
            return False
        else:
            self.conn.commit()
            self.conn.close()
            return True

    def update_aluno(self, id_aluno, nome, n1, n2, n3, n4):
        try:
            media = self.calcula_media(
                    float(n1), float(n2), float(n3), float(n4)
                )
            situacao = self._verifica_situacao_aluno(media)
            self.cursor.execute(
                """
                UPDATE 
                    alunos 
                SET
                    nome_aluno = '{nome}', 
                    n1 = {n1}, 
                    n2 = {n2}, 
                    n3 = {n3}, 
                    n4 = {n4}, 
                    media = {media}, 
                    situacao = {situacao}
                WHERE 
                    id_aluno = {id_aluno};
                """.format(
                        nome=nome,
                        n1=n1,
                        n2=n2,
                        n3=n3,
                        n4=n4,
                        media=media,
                        situacao=situacao,
                        id_aluno=id_aluno
                    )
            )
        except Exception as err:
            print("[ insert_aluno ERROR ] :", err)
            self.conn.close()
            return False
        else:
            self.conn.commit()
            self.conn.close()
            return True