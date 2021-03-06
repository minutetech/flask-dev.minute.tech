from wtforms import (Form, TextField,
                     PasswordField,
                     TextAreaField,
                     validators)
from wtforms.widgets import TextArea
# from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed  # FileRequired
# from werkzeug.utils import secure_filename  # For secure file uploads
from flask_uploads import (
    UploadSet, IMAGES)  # patch_request_class, configure_uploads

photos = UploadSet('photos', IMAGES)


class TechRegistrationForm(Form):
    first_name = TextField(
        'First Name', [validators.Length(min=1, max=50)])
    last_name = TextField('Last Name', [validators.Length(min=1, max=50)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    phone = TextField('Phone Number', [validators.Length(min=10, max=20)])
    address = TextField(
        'Street Address', [validators.Length(min=6, max=100)])
    city = TextField('City', [validators.Length(min=2, max=50)])
    state = TextField('State', [validators.Length(min=2, max=50)])
    tzip = TextField('ZIP', [validators.Length(min=2, max=16)])
    password = PasswordField('Password', [validators.Required(
    ), validators.EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField('Repeat Password')
    # recaptcha = RecaptchaField()


class TechEditAccountForm(Form):
    prof_pic = FileField(validators=[FileAllowed(photos, u'Image only!')])
    first_name = TextField(
        'First Name', [validators.Length(min=1, max=50)])
    last_name = TextField('Last Name', [validators.Length(min=1, max=50)])
    address = TextField(
        'Street Address', [validators.Length(min=6, max=100)])
    city = TextField('City', [validators.Length(min=2, max=50)])
    state = TextField('State', [validators.Length(min=2, max=50)])
    tzip = TextField('ZIP', [validators.Length(min=2, max=16)])
    birth_month = TextField('Birthday', [validators.Length(min=2, max=16)])
    birth_day = TextField('&nbsp;', [validators.Length(min=1, max=2)])
    birth_year = TextField('&nbsp;', [validators.Length(min=4, max=4)])
    bio = TextAreaField('Personal Description', [
        validators.Length(min=1, max=2000)], widget=TextArea())


class TechPhoneResetForm(Form):
    phone = TextField('Phone', [validators.Required(), validators.EqualTo(
        'confirm', message="Phone numbers must match.")])
    confirm = TextField('Repeat Phone')


class TechPasswordResetForm(Form):
    password = PasswordField('Password', [validators.Required(
    ), validators.EqualTo('confirm', message="Passwords must match.")])
    confirm = PasswordField('Repeat Password')


class TechEmailResetForm(Form):
    email = TextField('Email', [validators.Required(), validators.EqualTo(
        'confirm', message="Emails must match.")])
    confirm = TextField('Repeat Email')


class TechSignatureForm(Form):
    signature = TextField('Signature (Please enter your full name)', [
                          validators.Length(min=2, max=100)])
