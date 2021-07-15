from flask import Flask, request, flash, url_for, redirect, render_template
from cliente import Cliente

cliente1 = Cliente(1, "Yuri", 101, '533.316.867-22', 'Pessoa física')
cliente2 = Cliente(2, "Israel", 102, '876.432.154-43', 'Pessoa física')
cliente3 = Cliente(3, "Leonardo", 103, '517.351.343-11', 'Pessoa física')
cliente4 = Cliente(4, "Guilherme", 104, '564.359.478-06', 'Pessoa física')
clientesLista = [cliente1, cliente2, cliente3, cliente4]
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for cliente in clientesLista:
        result += "<li>%s</li>" % str(cliente._nome)
    result += "</ul>"
    return result
@app.route('/usuario', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['_nome'] or not request.form['_codigo']:
            flash('Favor entrar todos os valores dos campos', 'error')
        else:
            cliente = clientesLista(request.form['_nome'], request.form['_codigo'])
            clientesLista(cliente)
            return redirect(url_for('showUsuarios'))
    return render_template('home.html', title='Usuários')
@app.route('/usuario/del/<int:id>')
def delUsuario(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    cliente = clientesLista[id]
    clientesLista.remove(cliente)
    result += '<p>Usuário -> Id=' + str(cliente._id) + ' Excluido!</p>'
    return result
@app.route('/usuario/show/<int:id>')
def showUsario(id):
    cliente = clientesLista[id]
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id=" + str(cliente._id) + "</p>"
    result += "<p> Nome="  + cliente._nome + "</p>"
    result += "<p> Codigo=" + str(cliente._codigo) + "</p>"
    return result
@app.route('/usuarios')
def showUsuarios():
    result =  '<h1>Usuários</h1><br><ul>'
    for cliente in clientesLista:
        result += '<p>'
        result += 'Id=' + str(cliente._id)
        result += ' Nome=' + cliente._nome
        result += ' Codigo=' + str(cliente._codigo)
        result += '</p>'
    return result
if __name__ == '__main__':
    app.run()