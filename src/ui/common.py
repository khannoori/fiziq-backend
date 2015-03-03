'''
Created on 28/02/2015

@author: Ismail Faizi
'''
import jinja2
import os
import webapp2

from google.appengine.api import users
from models import User


ADMINS = [
    'kanafghan@gmail.com',
    'ac@sbin.dk',
    'khanjanherat@gmail.com'
]


JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'])


NAVIGATION = [
    {'caption': 'Home', 'route': '/', 'is_active': True}
]


class AbstractPage(webapp2.RequestHandler):
    """
    Abstraction of a web page
    """
    
    MSG_TYPE_ERROR = 'danger'
    MSG_TYPE_SUCCESS = 'success'
    MSG_TYPE_INFO = 'info'
    

    def __init__(self, template, request, response):
        webapp2.RequestHandler.__init__(self, request, response)
        self.template = template
        self.template_values = {}
        self.messages = []


    def get(self):
        if users.get_current_user():
            self.add_user_values(True)
            self.handle_get_request()
        else:
            self.add_user_values()
        
        self.init_template()


    def init_template(self):
        self.add_template_value('pages', NAVIGATION)
        tmpl = JINJA_ENVIRONMENT.get_template('views/%s' %self.template)
        self.response.write(tmpl.render(self.template_values))


    def add_user_values(self, logged_in=False):
        if logged_in:
            self.add_template_value('authorization_link', users.create_logout_url(self.request.uri))
            self.add_template_value('authorization_link_text', 'Logout')
            self.add_template_value('logged_in', True)
            self.add_template_value('authorized', (users.get_current_user().email().lower() in ADMINS))
        else:
            self.add_template_value('authorization_link', users.create_login_url(self.request.uri))
            self.add_template_value('authorization_link_text', 'Login')
        
        self.add_template_value('messages', self.messages)


    def post(self):
        if users.get_current_user():
            self.add_user_values(True)
            self.handle_post_request()
        else:
            self.add_user_values()

        self.init_template()


    def add_template_value(self, name, value):
        self.template_values[name] = value
    

    def set_active_page(self, page):
        for n in NAVIGATION:
            n['is_active'] = False
            if n['caption'].lower() == page.lower():
                n['is_active'] = True


    def add_message(self, message, msg_type=MSG_TYPE_ERROR):
        self.messages.append({'msg': message, 'type': msgType})


    def clear_messages(self):
        self.messages = []


    def handle_get_request(self):
        raise NotImplementedError('Subclasses should implement this')


    def handle_post_request(self):
        raise NotImplementedError('Subclasses should implement this')
