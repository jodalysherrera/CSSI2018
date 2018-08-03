import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/home.html")
        self.response.write(template.render())

class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("shhhhh this is a secret")

class Goodbye(webapp2.RequestHandler):
    def get(self):
        self.response.write("goodbye")

class About(webapp2.RequestHandler):
    def get(self):
        self.response.write("about")


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secret', SecretEntrance),
    ('/goodbye', Goodbye),
    ('/about', About),

], debug=True)
