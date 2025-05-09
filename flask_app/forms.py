from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    Optional,
)


from .models import User


class LocationSearchForm(FlaskForm):
    search_query = StringField(
        "Query", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Search")


class MomentForm(FlaskForm):
    content = TextAreaField(
        "Content", validators=[InputRequired(), Length(min=5, max=500)]
    )
    location = StringField("Location", validators=[InputRequired(), Length(min=1, max=100)])
    # for public checkbox, will process accordingly in routes.py, if user not logged in username is empty
    public = BooleanField("Public")
    # address to is an optional field
    addressed_to = StringField("Address To", validators=[Optional(), Length(min=1, max=100)])
    submit = SubmitField("Create Moment")
    # no comments or date in the initial create moment form, process in routes.py

class CommentForm(FlaskForm):
    comment = TextAreaField("Comment", validators=[])
    # for public checkbox, will process accordingly in routes.py, if user not logged in username is empty
    public = BooleanField("Public")
    submit = SubmitField("Post Comment")

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")


# TODO: implement fields
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

'''
# TODO: implement
class UpdateUsernameForm(FlaskForm):
    # username = None
    # submit_username = None 
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=40)])
    submit_username = SubmitField('Update')

    # TODO: implement
    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken')

# TODO: implement
class UpdateProfilePicForm(FlaskForm):
    # picture = None
    # submit_picture = None
    picture = FileField('Picture', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images Only!')])
    submit_picture = SubmitField('Update')
'''

