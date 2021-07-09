from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html",titulo="Constructora Leon")

@app.route('/about')
def about():
    return render_template("about.html",titulo="Nosotros")

@app.route('/service')
def service():
    return render_template("service.html",titulo="Servicios")

@app.route('/experence')
def experence():
    return render_template("experence.html",titulo="Experiencia")

@app.route('/contact')
def contact():
    return render_template("contact.html",titulo="Contactanos")

@app.route('/client')
def client():
    return render_template("client.html",titulo="Clientes")

@app.route('/projects')
def projects():
    return render_template("projects.html",titulo="Proyectos")

if __name__ == '__main__':
    app.run(debug=True)
