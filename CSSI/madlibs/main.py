import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)



class Story(webapp2.RequestHandler):
    def post(self):
        template= env.get_template("templates/story.html")
        correct= int(self.request.get('number'))
        total= int(self.request.get('largernumber'))
        templateVars={
            "protagonist": self.request.get('protagonist'),
            "event": self.request.get('event'),
            "pluralNoun":self.request.get('pluralNoun'),
            "skill":self.request.get('skill'),
            "name":self.request.get('name'),
            "number": correct/total * 100
            "adjective":self.request.get('adjective'),
            "place":self.request.get('place'),

        }
        self.response.write(template.render(templateVars))

class CollectInfo(webapp2.RequestHandler):
    def get(self):
        template= env.get_template("templates/collect_form.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', CollectInfo),
    ('/story', Story),



], debug=True)
