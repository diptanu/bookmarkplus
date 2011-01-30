import logging

from models import Bookmark, Tag
from google.appengine.api import users
from google.appengine.ext import webapp
from django.utils import simplejson

class FormHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Hello World")

    def post(self):
        user = users.get_current_user()
        url = self.request.get('url_text')
        tags = self.request.get('url_tag').split(",")

        usable_tags = []
        for tag_name in tags:
            if len(tag_name) is 0:
                continue
            tag = Tag(name = tag_name)
            tags_query = Tag.all()
            tags_query.filter('name =', tag_name)
            
            if len(tags_query.fetch(1)) is not 0:
                continue
            tag.put()
            usable_tags.append(tag.key())
        
        book_mark = Bookmark(user = user, url = url, tags = usable_tags)
        book_mark.put()
        json_data = simplejson.dumps({'result':True, 'link': url, 'tags': tags})
        self.response.out.write(json_data)
