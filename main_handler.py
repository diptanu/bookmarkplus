import os
import logging 

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from models import Bookmark, Tag

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        
        logout_url = users.create_logout_url(self.request.uri)
        username = user.nickname() if user is not None else ""
        urls_query = Bookmark.all() 
        urls_query.filter('user =', user)
        urls = urls_query.fetch(10)
        logging.error(urls)
        template_values = {'user_name': username, 'logout_url': logout_url, 'urls': urls}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
        
        
    def post(self):
        user = users.get_current_user()
        if user is None:
            self.redirect('/')
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
        self.redirect('/')
        
