from google.appengine.ext import db
from google.appengine.api import users

class Bookmark(db.Model):
    user = db.UserProperty()
    url = db.StringProperty()
    description = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    