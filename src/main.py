#!/usr/bin/env python

import webapp2

from ui.home import HomePage
from ui.workouts import WorkoutsPage


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/workouts', WorkoutsPage)
], debug=True)
