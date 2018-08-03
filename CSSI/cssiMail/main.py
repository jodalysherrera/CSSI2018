import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class email(object):
    def __init__(self,subject,sender,content,image):
        self.subject = subject
        self.sender = sender
        self.content = content
        self.image = image

emails = [
    email("test","ciera@google.com", "this is a test", "image"),
    email("test2","jody@google.com", "2nd this is a test","image"),
    email("test3","c@google.com", "3rd this is a test","image"),

]


class ListEmails(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/list_emails.html")
        templateVars= {
            "emails": emails,
        }
        self.response.write(template.render(templateVars))


class ViewEmails(webapp2.RequestHandler):
    def get(self):
        subject=self.request.get("subject")
        sender=self.request.get("sender")
        content=self.request.get("content")
        image=self.request.get("image")
        template = env.get_template("templates/view_emails.html")
        templateVars= {
            "subject": subject,
            "sender": sender,
            "content": content,
            "image": image,
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ('/', ListEmails),
    ('/ViewEmails', ViewEmails),


], debug=True)
