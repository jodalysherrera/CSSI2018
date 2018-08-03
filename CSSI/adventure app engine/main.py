import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/start.html')
        self.response.write(template.render())

class Jump(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/jumping.html')
        self.response.write(template.render())

class Run(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/running.html')
        self.response.write(template.render())

class accept(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/accept.html')
        self.response.write(template.render())

class reject(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/reject.html')
        self.response.write(template.render())

class eject(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/eject.html')
        self.response.write(template.render())

class fly(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/fly.html')
        self.response.write(template.render())

class confront(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/fly.html')
        self.response.write(template.render())

class runagain(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/fly.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/jumping', Jump),
    ('/running',Run ),
    ('/accept', accept),
    ('/reject', reject ),
    ('/eject', eject),
    ('/fly', fly),
    ('/confront', confront),
    ('/runagain', runagain),

], debug=True)
