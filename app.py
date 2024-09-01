from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy


# instanciando flask
app = Flask(__name__)

# criando banco de dados 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
db = SQLAlchemy(app)





#tabela db
class  Cards(db.Model):
    __name__ = 'Cards'
    id =  db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome= db.Column(db.String(30))
    atk = db.Column(db.Integer)
    df = db.Column(db.Integer)
    descricao = db.Column(db.String(200))

    def __init__(self,nome,atk,df,descricao):
        self.nome= nome
        self.atk = atk
        self.df = df
        self.descricao = descricao




@app.route('/')
def index():
    c = Cards.query.all()
    indice = 0
    return render_template('index.html',cards=c,indice=indice)


@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        print('POST')
        nome = request.form['nome']
        nome = nome.capitalize()
        nome = "".join(nome.split())
        atk = request.form['atk']
        df = request.form['df']
        descricao = request.form['desc']
        add_new = Cards(nome,atk,df,descricao)

        try:
            db.session.add(add_new)
            db.session.commit()
            return redirect('/add')
        except:
            print('erro')
            return render_template('add.html')
    else:
        print('GET')
        return render_template('add.html')


@app.route('/delete/<int:id>')
def delete(id):
    c = Cards.query.get(id)
    db.session.delete(c)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    c = Cards.query.get(id)
    if request.method == 'POST':
        print('post')
        c.nome = request.form['nome']
        c.atk = request.form['atk']
        c.df = request.form['df']
        c.descricao = request.form['desc']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        print('get')
    return render_template('edit.html',cards=c)

@app.route('/onclick', methods=['POST'])
def onclick():
    # lógica do evento
    return 'alert("hello")'


if __name__=='__main__':
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    