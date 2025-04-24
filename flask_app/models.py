from flask_login import UserMixin
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(db.Document, UserMixin):
    username = db.StringField(unique=True, required=True, min_length=1, max_length=40)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField()

    def get_id(self):
        return str(self.id)
    
class Comment(db.Document):
    moment = db.ReferenceField('Moment', required=True)
    commenter = db.ReferenceField('User', required=True)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)

    def get_id(self):
        return str(self.id)
    
class Moment(db.Document):
    addressed = db.StringField(required=False, min_length=1, max_length=50)
    date = db.StringField(required=True)
    content = db.StringField(required=True, min_length=5, max_length=500)
    location = db.PointField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField(Comment), default=list)
    creator = db.StringField(required=False, min_length=1, max_length=50)

    def get_id(self):
        return str(self.id)
    