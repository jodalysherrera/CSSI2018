import webapp2
import jinja2
import os

from google.appengine.ext import ndb


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class ClickCounter(ndb.Model):
    clicks = ndb.IntegerProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        templateVars={
            'click_count':click_counter.clicks,
        }

        template = env.get_template('templates/clicky.html')
        self.response.write(template.render(templateVars))

    def post(self):
        #load click counter from data base
        click_counter=ClickCounter.query().get()
        #check in case this is the first
        if not click_counter:
            click_counter=ClickCounter(clicks=0)

        click_counter.clicks+=1
        click_counter.put()

        templateVars={
            'click_count': click_counter.clicks,
        }
        template = env.get_template('templates/clicky.html')
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)
