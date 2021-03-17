from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")
    
@app.route('/usr/<int:id>')
def user(id):
     return render_template("user.html",uid=id)

if __name__ == '__main__':
	app.run(debug=True)
