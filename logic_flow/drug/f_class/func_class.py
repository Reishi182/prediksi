from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SubmitField

class DrugForm(FlaskForm):
    name = StringField("Nama")
    age = StringField("Umur")
    gender = SelectField("Jenis-Kelamin", choices=[('M','Laki-laki'),('F','Perempuan')])
    bp = SelectField('Tekanan-Darah', choices=[('HIGH','TINGGI'),('NORMAL','NORMAL'),('LOW','RENDAH')])
    cholesterol = SelectField('Level-Kolesterol', choices=[('HIGH','TINGGI'),('NORMAL','RENDAH')])
    na_to_k = StringField("Rasio Na Terhadap Kalium")
    submit = SubmitField("Prediksi")

def drug_class():
    form = DrugForm()
    return form