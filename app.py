import os

from flask import Flask, flash, redirect, render_template, request, send_from_directory
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from datetime import datetime

from helpers import apology
from flask_mail import Mail, Message

from form_contact import ContactForm, csrf
from flask_talisman import Talisman
from flask_sitemap import Sitemap

mail = Mail()

# Configure application
app = Flask(__name__)

csp  = { 
     'default-src' : [ 
         "'unsafe-inline'" , 
         '*.gstatic.com/' ,
         '*.googleapis.com/' ,
         '*.googleapis.com/' ,
         '*.jquery.com/' ,
         '*.cloudflare.com/' ,
         "*.google.com/" ,
         "*.google.com/",
         '*.jsdelivr.net/',
         '*.bld-devs.com/',
         '*.herokuapp.com/',
         '*.memegen.link/*.imgur.com/',
         '*.dynamicsjs.com/'
     ] 
 } 
Talisman(app, content_security_policy = csp)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bld.devs@gmail.com'
app.config['MAIL_PASSWORD'] = 'Auto78310'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True

app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LeIwmgcAAAAAIqzcLYo9AjypZn8nCJ2sUKzqaDz'
app.config['RECAPTCHA_PRIVATE_KEY']='6LeIwmgcAAAAAL06WFUEMcabDEvGQkxzIN0eUgcg'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}

mail.init_app(app)

@app.route("/")
def index():
    """Show index page"""
    return render_template("index.html")

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['prenom'])
        print(request.form['email'])
        print(request.form['numero'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        send_messageClient(request.form)
        return redirect('/success')    

    return render_template('contact.html', form=form)  

@app.route('/success')
def success():
    return render_template('index.html', success=success)

def send_message(message):
    print(message.get('name'))

    msg = Message(subject = message.get('subject'),
            recipients = ['bld.devs@gmail.com'],
            html = render_template('email.html')
    )  
    mail.send(msg)
    
def send_messageClient(message):
    
    msgClient = Message(subject = 'BLD Devs - Accusé de réception de votre message.',
            recipients = [message.get('email')],
            html = render_template('emailClient.html')
    )
    mail.send(msgClient)

@app.route("/portfolio")
def portfolio():
        return render_template("portfolio.html")


@app.route("/diplomes")
def diplomes():
        return render_template("diplomes.html") 

@app.route("/mentionslegales")
def mentionslegales():
        return render_template("mentionslegales.html")

@app.route("/experiences")
def experiences():
        return render_template("experiences.html")

@app.route("/aboutme")
def aboutme():
        return render_template("aboutme.html")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


if __name__ == "__main__":
    app.run(debug = True)
