'''
Created on 08/03/2015

@author: Ismail Faizi
'''
import endpoints

from api.default.users import Users
from api.default.muscle_groups import MuscleGroups
from api.default.workouts import Workouts


application = endpoints.api_server([
    Users,
    MuscleGroups,
    Workouts
])
