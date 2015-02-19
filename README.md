# Fiziq Backend

The Google App Engine application used as the Backend for the Fiziq app.

## Getting Started
In order to get started, you must have the following installed on your system:

- [Python 2.7.x](https://www.python.org/downloads/)
- [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

Start the [development web server](https://cloud.google.com/appengine/docs/python/tools/devserver) as follows:

```bash
$ ./dev_appserver.py /path/to/fiziq-backend/src
```

This will start and run the development server where the application can be visited at:

```
http://localhost:8080
``` 

and the [admin application](#admin-application) can be visited at:

```
http://localhost:8000
``` 

### Admin Application
The Google App Engine SDK comes with an admin application and is started whenever your application is started using
the development web server mentioned above. You can access this admin application by 
visiting `http://localhost:8000`. One of the main and usefull feature of the admin panel is 
the **Datastore Viewer** which presents the different kinds and entities belonging to your application datamodel.
It is important to notice that the Datastore Viewer only presents those kinds that has at least one entity.

Another usefull feature of the admin application is the **Interactive Console** which lets you execute some python
code within the context of your application. The following snippet demonstrates how one can add entities to the
datastore through the Interactive Console. You can copy-&-past the code into the Interace Console and execute
it.

```Python
import models

journal = models.TrainingJournal(parent=models.TRAINING_JOURNAL_KEY)
journal.put()

user = models.User(parent=models.USER_KEY)
user.name = 'Ismail Faizi'
user.email = 'kanafghan@gmail.com'
user.training_journal = journal.key
user.put()

print 'You just stored some data in the Datastore!'
```


## Technical Documentation
For technical documentation please click [here](doc/README.md).
