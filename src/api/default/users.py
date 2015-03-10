'''
Created on 08/03/2015

@author: Ismail Faizi
'''
import endpoints

from api.default import defaultApi
from protorpc import messages, remote
from models.factories import ModelFactory


'''
### MESSAGES ###
'''
class RegisterRequest(messages.Message):
    name = messages.StringField(1, required=True)
    email = messages.StringField(2, required=True)


class RegisterResponse(messages.Message):
    user_key = messages.StringField(1, required=True)

'''
### END of MESSAGES ###
'''


@defaultApi.api_class(
    resource_name='users',
    path='users'
)
class Users(remote.Service):
    """
    API for users
    """

    @endpoints.method(
        RegisterRequest,
        RegisterResponse,
        name='register',
        path='register',
        http_method='POST'
    )
    def register(self, request):
        """
        Registers a user based on the given name and E-mail address
        """
        # first create a training journal for the user
        training_journal = ModelFactory.create_training_journal()
        training_journal.put()

        # now, create/register the user
        user = ModelFactory.create_user(
            name=request.name,
            email=request.email,
            training_journal=training_journal
        )
        user.put()

        return RegisterResponse(user_key=user.key.urlsafe())
