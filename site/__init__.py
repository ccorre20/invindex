from flask import Flask, render_template, url_for, request, session, redirect
from pymongo import MongoClient

#app.config['MONGO_DBNAME'] = 'dbtest'
#app.config['MONGO_URI'] = '127.0.0.1:27017'
#mongo = PyMongo(app)
#Info de mongo.
#IP 10.131.137.188
#PORT 27017
#DB grupo_03
#USER user1
#PWD eafit.2017
#PORT other dc 8001

app = Flask(__name__)

client = MongoClient('10.131.137.188', 27017)
db = client['grupo_03']
db.authenticate('user1','eafit.2017') 
mycol = db.indexes


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/resultados", methods = ['GET'])
def resultados():
	result = request.args.get('magicWord')
	resultado = mycol.find_one({'_id': result})['data']
	return render_template('resultados.html', resultado=resultado)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8001)
