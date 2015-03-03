'''
Created on 1/03/2015

@author: Ismail Faizi
'''
from common import AbstractPage


class HomePage(AbstractPage):
    """
    The Fiziq home page
    """


    def __init__(self, request, response):
        AbstractPage.__init__(self, 'home.html', request, response)


    def handle_get_request(self):
        pass


    def handle_post_request(self):
        pass
