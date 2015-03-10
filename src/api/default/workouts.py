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


class SessionCreateRequest(messages.Message):
    pass


class SessionCreateResponse(messages.Message):
    pass


class SetCreateRequest(messages.Message):
    pass


class SetCreateResponse(messages.Message):
    pass

'''
### END of MESSAGES ###
'''


@defaultApi.api_class(
    resource_name='workouts',
    path='workouts'
)
class Workouts(remote.Service):
    """
    API for workouts, workout sessions and workout sets
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
        Returns a list of workouts
        """
        pass

    @endpoints.method(
        SessionCreateRequest,
        SessionCreateResponse,
        name='sessions.create',
        path='sessions/create',
        http_method='POST'
    )
    def create_workout_session(self, request):
        """
        Creates a workout session based on the given data
        """
        pass

    @endpoints.method(
        SetCreateRequest,
        SetCreateResponse,
        name='set.create',
        path='set/create',
        http_method='POST'
    )
    def create_workout_set(self, request):
        """
        Creates a workout set based on the given data
        """
        pass
