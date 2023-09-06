from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('add repair')


class NewJewelleryRepairForm(FlaskForm):
    customer_name = StringField('Customer Name', validators=[DataRequired(), Length(min=2)])
    repair_description = TextAreaField('Item Description', validators=[DataRequired(), Length(min=2)])

    # todo change this to include updating
    submit = SubmitField('Create Repair')

#
# repair_data = [
#     {
#         'author': 'Seb Knight',
#         'job_number': "1",
#         'customer_name': "Jane Doe",
#         'repair_description': '18ct ring',
#         'date_created': "April 20th 2012"
#     },
#     {
#         'author': 'William Knight',
#         'job_number': "2",
#         'customer_name': "John Vil",
#         'repair_description': 'diamond watch',
#         'date_created': "January 30th 2013"
#     }
# ]
