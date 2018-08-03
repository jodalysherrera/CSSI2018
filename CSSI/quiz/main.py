import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)



class ShowQuiz(webapp2.RequestHandler):
    def get(self):
        template= env.get_template("templates/quiz.html")
        self.response.write(template.render())


class Results(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/results.html")
        result= self.response.get('radio')
        templateVars={
            'result': result
        }
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', ShowQuiz),
    ('/results', Results),




], debug=True)
