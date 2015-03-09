# Fiziq Backend

The Google App Engine application used as the Backend for the Fiziq app.

## Getting Started
In order to get started, you must have the following installed on your system:

- [Python 2.7.x](https://www.python.org/downloads/)
- [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)

Start the [development web server](https://cloud.google.com/appengine/docs/python/tools/devserver) as follows:

```bash
$ dev_appserver.py /path/to/fiziq-backend/src
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
datastore through the Interactive Console. You can copy-&-past the code into the Interactive Console and execute
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

However, the prefered way of doing what is shown above is to use the corresponding factory method for each
model, e.g:

```Python
from models.factories import ModelFactory

journal = ModelFactory.create_training_journal()
journal.put()

user = ModelFactory.create_user('Ismail Faizi', 'kanafghan@gmail.com', journal)
user.put()

print 'You just stored some data in the Datastore!'
```

## Google Python Style Guide
Please follow [Google Python Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
when writting code for this project.


## Tests
The following section describes how to run and add tests to this project.

### Running Tests
In order to run the tests, you must first start your development web server. By visiting the following
URL, you run all the tests and the result will be displayed using 
[GAEUnit](https://code.google.com/p/gaeunit/) (Google App Engine Unit Test Framework).

```
http://localhost:8080/tests
```

You can also run a specific test case by specifying the python module name in the URL, e.g.:

```
http://localhost:8080/tests?name=test_factories
```

### Adding Tests
In order to add new tests, you must create a test module for each module you want to test. These test
modules must be created in the `tests` folder which is located in the `src` folder. When naming the 
test modules, prefix the name of the module you want write tests for with `test_`, e.g. if you want
to write tests for the `factories.py` module, then the test module should be called `test_factories.py`.

When naming the test class use the CamelCase style and create the name by sufixing the name of 
the class you want to test with `Test`, e.g. if you want to write tests for the `ModelFactory` class
you should call the test class `ModelFactoryTest`.

When naming the test methods use the snake_case style, e.g. `test_success()`. 


## Extending UI
The Fiziq backend provides a mini UI framework to add pages with specific features/contents for administration
purposes. This framework is based on the `jinja2` template engine.

In order to add a page you must follow the following steps:

### Add Page Handler
The first step is to add the page handler which is the logic that handles request and response. The logic
for initializing the template engine and injecting the template with values has been abstracted away using
the `AbstractPage` class which is located in the `src/ui/common.py` file. You must extend this class and
implement the `handle_post_request()` and `handle_get_request()` methods. In order to inject template
variables into the template of the page, you can use the `add_template_value()` method. It is recommended 
that you study the source code of the `AbstractPage` class.

### Provide the Navigation
In the `src/ui/common.py` file you find the `NAVIGATION` variable which is a list of python dictionaries.
Each element of the list provides a navigation of a page, i.e. the menu caption of the page, the route of
the page, and whether the page is the active page. In the following, an example is presented:

```Python
NAVIGATION = [
    {'caption': 'Home', 'route': '/', 'is_active': True},
    {'caption': 'Workouts', 'route': '/workouts', 'is_active': False},
]
```
You must add the navigation of your page as shown above.

### Add Page Template
All the templates (the html files) of the various pages are found in `src/ui/views` folder. All the
templates must extend the `base.html` template. For an example, see the `home.html` template.

### Add Page Route
You must extend the application in the `main.py` with the route and page handler of your page.
For instance, if we were to add the `/foo` route with `FooPage` as handler, we will extend the 
application as follows:

```Python
app = webapp.WSGIApplication([
    ('/', HomePage),
    ...
    ('/foo', FooPage)
], debug=True)
```


## Technical Documentation
For technical documentation please click [here](doc/README.md).
