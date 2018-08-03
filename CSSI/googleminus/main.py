import webapp2
import jinja2
import os
import logging
import time

from google.appengine.api import users
from google.appengine.ext import ndb


class Person(ndb.Model):
    name = ndb.StringProperty()
    biography = ndb.StringProperty()
    birthday = ndb.DateProperty()
    email = ndb.StringProperty()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    # extensions=['jinja2.ext.autoescape'],
    # autoescape=True)
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        current_user=users.get_current_user()
        #1. read the Request
        #2 redirecting the database
        people = Person.query().fetch()
        if current_user:
            current_email = current_user.email()
            current_person=Person.query().filter(Person.email == current_email)
        else:
            current_person= None

        logout_url = users.create_logout_url('/')

        login_url = users.create_login_url('/')

        #3. render a response
        templateVars={
            'people': people,
            'current_user': current_user,
            'login_url': login_url,
            'logout_url':logout_url,
            'person': current_person
        }
        template = env.get_template('templates/home.html')
        self.response.write(template.render(templateVars))

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        urlsafe_key = self.request.get('key')
        logging.info(urlsafe_key)

        key = ndb.Key(urlsafe=urlsafe_key)
        logging.info(key)

        person = key.get()
        logging.info(person)

        templateVars={
        'person': person
        }

        template = env.get_template('templates/profile.html')
        self.response.write(template.render(templateVars))

class Create(webapp2.RequestHandler):
    def post(self):
        #get infor from Request#read or write datsbase #render a response
        name = self.request.get('name')
        biography = self.request.get('biography')
        current_user = users.get_current_user()
        email = current_user.email()


        person = Person(name=name, biography=biography, email=email)
        person.put()

        time.sleep(2)
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/profile', ProfilePage),
    ('/create', Create)
], debug=True)
