import sqlite3
conn = sqlite3.connect('database/alunos.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO alunos (nome_aluno, n1, n2, n3, n4, media, situacao) values ('Andre Ferreira', 10, 9, 8, 9.5, 9.125, 1);")
conn.commit()
conn.close()