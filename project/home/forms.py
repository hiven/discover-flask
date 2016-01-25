from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    company = TextField('Company', validators=[DataRequired()])
    companyurl = TextField('Companyurl', validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    salary = TextField('Salary', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired(), Length(max=140)])
    jobtype = SelectField('Type', choices=[('full', 'Full-Time'), ('part', 'Part-Time'), ('temp', 'Temporary')], validators=[DataRequired()])
