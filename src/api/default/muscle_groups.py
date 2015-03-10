'''
Created on 08/03/2015

@author: Ismail Faizi
'''
import endpoints

from api.default import defaultApi
from protorpc import messages, remote, message_types


'''
### MESSAGES ###
'''
class ListResponse(messages.Message):
    pass
'''
### END of MESSAGES ###
'''


@defaultApi.api_class(
    resource_name='muscle.groups',
    path='muscle/groups'
)
class MuscleGroups(remote.Service):
    """
    API for muscle groups
    """

    @endpoints.method(
        message_types.VoidMessage,
        ListResponse,
        name='list',
        path='list',
        http_method='GET'
    )
    def list(self, request):
        """
        Returns a list of all muscle groups
        """
        pass
