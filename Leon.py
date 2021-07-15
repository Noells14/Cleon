from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from forms import envioCorreos

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'pablo.lemo89@gmail.com'
app.config['MAIL_PASSWORD'] = 'M45h1m4th..'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail= Mail(app)

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
    envio_correo = envioCorreos()
    return render_template("contact.html", titulo="Contactanos", form = envio_correo)

@app.route('/client')
def client():
    return render_template("client.html",titulo="Clientes")

@app.route('/projects')
def projects():
    return render_template("projects.html",titulo="Proyectos")

@app.route('/envio', methods=['POST'])
def envio():
    envio_correo = envioCorreos()
    nombre = request.form.get("nombre")
    correo = request.form['correo']
    comentario = request.form['comentario']
    msg = Message('Gracias por contactarnos',
        sender = 'pablo.lemo89@gmail.com',
        recipients = [correo, 'nemobad26@gmail.com'])
    msg.html = render_template("contacto.html", name = nombre, comment = comentario)
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)

    msg = Message('Nuevo cliente',
        sender = 'pablo.lemo89@gmail.com',
        recipients = ['pablo.lemo89@gmail.com'])
    msg.html = render_template("correo.html", name = nombre, email = correo, comment = comentario)
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)

    success_message = 'Te hemos enviado un correo electronico'
    flash(success_message) 
    envio_correo.nombre.data = ''
    envio_correo.correo.data = ''
    envio_correo.comentario.data = ''
    return render_template("contact.html",titulo="Contactanos", form = envio_correo)

if __name__ == '__main__':
    app.run(debug=True)
