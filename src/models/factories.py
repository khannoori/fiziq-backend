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
