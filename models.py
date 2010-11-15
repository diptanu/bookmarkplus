from google.appengine.ext import db
from google.appengine.api import users


class Tag(db.Model):
    name = db.StringProperty()
    

class Bookmark(db.Model):
    user = db.UserProperty()
    url = db.StringProperty()
    description = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add = True)
    tags = db.ListProperty(db.Key)

    
