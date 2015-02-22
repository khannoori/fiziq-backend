'''
Created on 22/02/2015

@author: Ismail Faizi
'''
import models


class ModelFactory(object):
    """
    Factory for creating entities of models
    """


    @classmethod
    def create_user(cls, name, email, training_journal):
        """
        Factory method for creating User entity.

        NOTE: you must explicitly call the put() method
        """
        user = models.User(parent=models.USER_KEY)
        user.name = name
        user.email = email
        user.training_journal = training_journal.key
        
        return user


    @classmethod
    def create_training_journal(cls):
        """
        Factory method for creating TrainingJournal entity.

        NOTE: you must explicitly call the put() method
        """
        return models.TrainingJournal(parent=models.TRAINING_JOURNAL_KEY)


    @classmethod
    def create_workout_session(cls, started_at, ended_at, training_journal):
        """
        Factory method for creating WorkoutSession entity.

        NOTE: you must explicitly call the put() method
        """
        workout_session = models.WorkoutSession(parent=models.WORKOUT_SESSION_KEY)
        workout_session.started_at = started_at
        workout_session.ended_at = ended_at
        workout_session.training_journal = training_journal.key
        
        return workout_session
