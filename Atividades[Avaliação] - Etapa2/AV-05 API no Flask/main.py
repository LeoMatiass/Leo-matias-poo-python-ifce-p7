from flask import Flask, request, url_for, redirect, render_template, flash
from modelo.item import Item

itens = [Item(1, "Arroz Agulha ", 100, '55.00', 'fisica'),
            Item(2, "Feijao Mulatinho", 200, '85.00', 'fisica'),
            Item(3, "Macarrao Fortaleza", 300, '45.00', 'fisica'),]
id_atual = 3
codigo_atual = 600


def atualizar_itens(item):
    global id_atual
    global codigo_atual
    id_atual += 1
    codigo_atual += 100
    itens.append(item)
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'senha'

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def set_item():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['preço']:
            flash('Por favor, entre com os valores')
        else:
            item = Item(id_atual, request.form['nome'], codigo_atual, request.form['preço'], 'fisica')
            atualizar_itens(item)
            flash('Seu item foi registrado com sucesso.')
            return redirect(url_for('show_itens'))
    return render_template('form.html')

@app.route('/item/<int:item_id>')
@app.route('/item', defaults={'item_id': None})
def get_item(item_id):
    if item_id:
        try:
            item = [c for c in itens if item_id == c.get_id()][0]
            return render_template('item.html', item=item)
        except IndexError as e:
            return render_template('item.html', erro=e)
    else:
        return render_template('item.html')

@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar_item():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['preço'] or not request.form['id']:
            flash('Favor entrar todos os valores dos campos')
        else:
            try:
                item_id = int(request.form['id'])
                item = [c for c in itens if item_id == c.get_id()][0]
                item.set_nome(request.form['nome'])
                item.set_preço(request.form['preço'])
                flash('Registro foi atualizado com sucesso')
                return redirect(url_for('show_itens'))
            except IndexError as e:
                flash(f'Favor entre com um id válido.')
    return render_template('atualizar.html')

@app.route('/itens')
def show_itens():
    return render_template('itens.html', itens=itens)

if __name__ == '__main__':
    app.run()
