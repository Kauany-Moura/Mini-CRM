# ==============================================
# app.py — Interface Flask do Mini-CRM
# ==============================================
from flask import Flask, render_template, request, redirect, url_for
from models import CRM, Cliente, Funcionario

app = Flask(__name__)
crm = CRM()  # Instância única do sistema


@app.route('/')
def index():
    cadastros = crm.listar_cadastros()
    return render_template('index.html', cadastros=cadastros)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        tipo = request.form['tipo']
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        if tipo == 'cliente':
            empresa = request.form['empresa']
            status = request.form['status']
            pessoa = Cliente(nome, email, telefone, empresa, status)
        else:
            cargo = request.form['cargo']
            pessoa = Funcionario(nome, email, telefone, cargo)

        crm.adicionar_pessoa(pessoa)
        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
