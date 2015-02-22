import unittest
import models

from models.factories import ModelFactory


class ModelFactoryTest(unittest.TestCase):
    

    def test_create_training_journal(self):
        # create a journal
        journal = ModelFactory.create_training_journal()
        self.assertTrue(isinstance(journal, models.TrainingJournal))


    def test_create_user(self):
        # create a user
        journal = ModelFactory.create_training_journal()
        journal.put()

        user = ModelFactory.create_user('Iceman', 'if@kanafghan.com', journal)

        # the user should be as expected
        self.assertTrue(isinstance(user, models.User))
        self.assertEqual(user.name, 'Iceman')
        self.assertEqual(user.email, 'if@kanafghan.com')
        self.assertEqual(user.training_journal, journal.key)
