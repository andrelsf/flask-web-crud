from flask import Flask, request, render_template, redirect, url_for
from entidades.db_sqlite import DBSqlite

db = DBSqlite()
db.create_table_alunos()
app = Flask(__name__, template_folder="templates/html/")

#
# ROTA PARA O INDEX DA PAGINA
#
@app.route('/')
@app.route('/index')
def index():
    alunos = db.get_alunos()
    return render_template("index.html", alunos=alunos)


#
# CADASTRAR ALUNO
#
@app.route('/novoaluno')
def novoaluno():
    return render_template("novoaluno.html", action="cadastrar")


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome = (request.form.get("nome"))
        n1 = (request.form.get("n1"))
        n2 = (request.form.get("n2"))
        n3 = (request.form.get("n3"))
        n4 = (request.form.get("n4"))
        if nome and n1 and n2 and n3 and n4:
            if db.insert_aluno(nome, n1, n2, n3, n4):
                return redirect(url_for("index"))
            else:
                return redirect(url_for("err"))
        else:
            return redirect(url_for('err'))         
    return redirect(url_for("index"))
        

@app.route('/err/')
def err():
    return "[ ERROR ] : Falha ao salva. <a href='{}'>Voltar</a>".format(
        url_for('index')
    )


#
# EDITAR ALUNO
#
@app.route('/editar/<int:idaluno>')
def editar(idaluno):
    aluno = db.get_aluno_by_id(id_aluno=idaluno)
    return render_template("novoaluno.html", action="atualizar", aluno=aluno)


@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    if request.method == 'POST':
        id_aluno = (request.form.get("idaluno"))
        nome = (request.form.get("nome"))
        n1 = (request.form.get("n1"))
        n2 = (request.form.get("n2"))
        n3 = (request.form.get("n3"))
        n4 = (request.form.get("n4"))
        if nome and n1 and n2 and n3 and n4:
            if (db.update_aluno(id_aluno, nome, n1, n2, n3, n4)):
                return redirect(url_for('index'))
            else:
                return redirect(url_for('err'))
    return redirect(url_for('index'))


#
# EXCLUIR ALUNO
#
@app.route('/excluir/<int:idaluno>')
def excluir(idaluno):
    if db.excluir_aluno(idaluno):
        return redirect(url_for('index'))
    else:
        return redirect(url_for('err'))

#
# METODO PRINCIPAL
#
if __name__ == '__main__':
    app.run(debug=True)