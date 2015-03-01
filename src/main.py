#!/usr/bin/env python

import webapp2

from ui.home import HomePage


app = webapp2.WSGIApplication([
    ('/', HomePage)
], debug=True)
