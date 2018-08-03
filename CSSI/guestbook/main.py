import webapp2
import jinja2
import os
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

class Message(ndb.Model):
    email = ndb.StringProperty()
    content = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)



env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    # extensions=['jinja2.ext.autoescape'],
    # autoescape=True)
)



class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('this is the main handler')
        login_url = ''
        logout_url = ''
        # the current user will be a user obeject or none
        current_user = users.get_current_user()
        logging.info(current_user.user_id())
        #if no one is logged in show a login prompt
        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')
        message_query = Message.query()
        message_query = message_query.order(-Message.created_time)
        messages = message_query.fetch()

        templateVars={
            'current_user': current_user,
            'login_url': login_url,
            'logout_url': logout_url,
            'messages':messages,
        }
        template=env.get_template('templates/guestbook.html')
        self.response.write(template.render(templateVars))

    def post(self):
        #1.get info from the RequestHandler
        content = self.request.get('content')
        current_user = users.get_current_user()
        email = current_user.email()
        #2.read/write to the data base
        message=Message(content=content, email=email)
        message.put()
        #3 render a response
        self.redirect('/')






app = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)
