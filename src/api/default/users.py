'''
Created on 08/03/2015

@author: Ismail Faizi
'''
import endpoints

from api.default import defaultApi
from protorpc import messages, remote


'''
### MESSAGES ###
'''
class RegisterRequest(messages.Message):
    pass


class RegisterResponse(messages.Message):
    pass
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
        pass
