#Se importa la libreria de flask y render_template 
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def principal():
    return render_template('/prime.html')


if __name__ == '__main__':
    app.run(debug=True)
