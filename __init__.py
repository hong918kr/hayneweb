from flask import Flask, render_template

def create_app():

	app = Flask(__name__)
	@app.route('/')
	@app.route('/index') 
	# both roots and index will be attribute to index functions
	def index():
		user = {'username': 'Hayne'}
		return render_template('index.html', title='Home', user=user)

	return app