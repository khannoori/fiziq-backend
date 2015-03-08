import unittest
import models

from api.default.users import RegisterRequest, RegisterResponse, Users
from google.appengine.ext import ndb


class UsersApiTest(unittest.TestCase):

    def test_registration(self):
        # create the request
        request = RegisterRequest()
        request.name = 'Ismail Faizi'
        request.email = 'kanafghan@gmail.com'

        usersApi = Users()
        response = usersApi.register(request)

        self.assertTrue(None != response.user_key)

        user_key = ndb.Key(urlsafe=response.user_key)
        user = user_key.get()

        self.assertEqual(request.name, user.name)
        self.assertEqual(request.email, user.email)
