from flask_wtf import FlaskForm, CSRFProtect, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired("Merci d'indiquer votre nom")])
    prenom = StringField('Prénom', validators=[DataRequired("Merci d'indiquer votre prénom")])
    email = StringField('E-mail', validators=[DataRequired("Merci d'indiquer votre adresse mail"),Email('Renseignez une adresse valide')])
    numero = StringField('Numéro de téléphone', validators=[DataRequired("Merci d'indiquer votre numéro")])
    subject = StringField('Sujet', validators=[DataRequired("Merci de préciser le sujet de votre demande")])
    message = TextAreaField('Message', validators=[DataRequired("Merci de préciser votre demande")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Envoyer le message")
