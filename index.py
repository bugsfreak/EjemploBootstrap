#Se importa la libreria de flask y render_template 
from flask import Flask, render_template

#Se asigna la libreria flask a la variable app
app = Flask(__name__, template_folder='templates')

#Se define una ruta
@app.route('/')
def principal():
    return render_template('/prime.html')


if __name__ == '__main__':
    app.run(debug=True)
