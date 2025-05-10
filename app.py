from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html', titulo='Inicio')

@app.route('/sobre_mi')
def sobre_mi():
    return render_template('sobre_mi.html', titulo='Sobre Mí')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html', titulo='Habilidades')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html', titulo='Proyectos')

if __name__ == '__main__':
    app.run(debug=True)