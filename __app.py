from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de pessoas
pessoas = []

# Rota para a página de cadastro de pessoas
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        pessoas.append({'nome': nome, 'idade': idade})
    return render_template('pessoas/cadastro.html')

# Rota para a página de listagem de pessoas
@app.route('/lista')
def lista():
    return render_template('pessoas/lista.html', pessoas=pessoas)


# Rota para a página inicial (index)
@app.route('/')
def index():
    return render_template('app/index.html')

if __name__ == '__main__':
    app.run(debug=True)
