from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Listas de dados em memória
tecnicos = []
safras = []
pragas = []
fazendas = []
lancamentos=[]
talhoes = [{"nome":"th1"}, {"nome":"th2"}]
armadilhas = [{"nome":"arm1"}, {"nome":"arm2"}, {"nome":"arm3"}]
apontamentos = []
# Rota para a página de listagem de técnicos
@app.route('/tecnicos')
def tecnicos_list():
  return render_template('tecnicos/index.html', tecnicos=tecnicos)


# Rota para a página de cadastro de pessoas
@app.route('/tecnicos/cadastrar', methods=['GET', 'POST'])
def tecnicos_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    idade = request.form['idade']
    contato = request.form['contato']
    tecnicos.append( 
      {
        'nome': nome,        
        'idade': idade,
        'contato': contato
      }
    )
  return render_template('tecnicos/form.html')


# Rota para a página de lista de safras
@app.route('/safras')
def safras_list():
  return render_template('safras/index.html', safras=safras)


# Rota para a página de cadastro de safras
@app.route('/safras/cadastrar', methods=['GET', 'POST'])
def safras_cad():
  if request.method == 'POST':
    cultura = request.form['cultura']
    periodo = request.form['periodo']
    cultivar = request.form['cultivar']
    safras.append(
      {
        'cultura' : cultura,
        'periodo': periodo,
        'cultivar': cultivar
      })
  return render_template('safras/form.html')


# Rota para a página de lista de pragas
@app.route('/pragas')
def pragas_list():
  return render_template('pragas/index.html', pragas=pragas)


# Rota para a página de cadastro de pragas
@app.route('/pragas/cadastrar', methods=['GET', 'POST'])
def pragas_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    nome_cient = request.form['nome_cientifico']
    pragas.append({'nome': nome, 'nome_cientifico': nome_cient})
  return render_template('pragas/form.html')


# Rota para a página de lista de fazendas
@app.route('/fazendas')
def fazendas_list():
  return render_template('fazendas/index.html', fazendas=fazendas)

#Rota para o cadastro de fazendas
@app.route('/fazendas/cadastrar', methods=['GET', 'POST'])
def fazendas_cad():
  if request.method == 'POST':
    nome = request.form['nome']
    nome_area = request.form['area']
    nome_endereco = request.form['endereco']
    nome_contato = request.form['contato']
    nome_proprietario = request.form['proprietario']
    fazendas.append({'nome':nome,'area':nome_area,'endereco':nome_endereco,'contato':nome_contato,'proprietario':nome_proprietario})
  return render_template('fazendas/form.html', fazendas=fazendas)


# Rota para a página de lista de armadilhas
@app.route('/armadilhas')
def armadilhas_list():
  return render_template('armadilhas/index.html', armadilhas=armadilhas)

#Rota para o cadastro de armadilhas
@app.route('/armadilhas/cadastrar', methods=['GET', 'POST'])
def armadilhas_cad():
  if request.method == 'POST':
    nome_cultura = request.form['cultura']
    nome_talhao = request.form['talhao']
    nome_data = request.form['data']
    armadilhas.append(
      {
       "cultura":nome_cultura,
       "talhao":nome_talhao,
       "data":nome_data
      }
    )
  return render_template('armadilhas/form.html', armadilhas=armadilhas)


# Rota para a página de lista de Lançamentos
@app.route('/lancamentos')
def lancamentos_list():
  return render_template ('lancamentos/index.html', lancamentos=lancamentos)

#Rota para o cadastro de apontamentos
@app.route('/apontamentos')
def apontamentos_list():
  return render_template('apontamentos/index.html', apontamentos=apontamentos)


@app.route('/apontamentos/cadastrar', methods=['GET', 'POST'])
def apontamentos_cad():
  if request.method == 'POST':   
     cultura = request.form['cultura']
     cultivar = request.form['cultivar']
     periodo = request.form ['periodo']
     talhao = request.form['talhao']
     armadilha = request.form['armadilha']
     praga = request.form['praga']
     qtd = request.form['qtd']
     dt = request.form['dt']
     tecnico = request.form['tecnico']
    
    
     apontamentos.append({
      "cultura": cultura,
      "cultivar": cultivar,
      "periodo": periodo,
       "talhao": talhao,
       "armadilha": armadilha,
       "praga": praga,
       "qtd": qtd,
       "dt": dt,
       "tecnico": tecnico,
    })
  return render_template('apontamentos/form.html',safras=safras,talhoes=talhoes,pragas=pragas,armadilhas=armadilhas, tecnicos=tecnicos)


# Rota para a página inicial do app
@app.route('/')
def index():
  return render_template('app/index.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81) 
