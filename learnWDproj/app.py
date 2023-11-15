from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/Department')
def Department():
	return render_template('Department.html')

if __name__ == '__main__':
	app.run(debug=True)
