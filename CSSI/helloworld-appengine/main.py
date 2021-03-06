import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        location = self.request.get('location')
        template = env.get_template("templates/hello.html")
        templateVars= {
            "name" : name,
            "location" : location
        }
        self.response.write(template.render(templateVars))

class SecretEntrance(webapp2.RequestHandler):
    def get(self):
        self.response.write("shhhhh this is a secret")

class Goodbye(webapp2.RequestHandler):
    def get(self):
        self.response.write("goodbye")

class About(webapp2.RequestHandler):
    def get(self):
        self.response.write("about")

class Students(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/students.html")
        templateVars= {
            "location" : "MTV" ,
            "students" : ["Kidus", "leo","lily","Phoebe","jenny","elvin" ]
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secret', SecretEntrance),
    ('/goodbye', Goodbye),
    ('/about', About),
    ('/students', Students),


], debug=True)
