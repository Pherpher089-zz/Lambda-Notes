# Django

A python frame-work for creating servers. This is much like express for node.js.

## Setting up Django

1. Set up a virtual environment
    1. Run `pipenv --three` to create the env
    2. Enter that env with `pipenv shell`
    3. Reinstall pipenv. It doesn't exist in the virtual env you are now in.
2. Install Django
    1. `pip install django`
3. Create a Django project
    1. `django-admin startprject <project name>`
4. Create a Django app in the project
    1. `django-admin startapp <app name>`
5. Run server

    1. `./manage.py runserver`

### django-admin

this command allows you to do things with your project. Don' t know much about it yet

## Models and Migrations

The glue between Djangos model and the SQLight. These are pieces of software that set up the database.

`./manage.py showmigrations` will show all of the migrations. When you see the `[ ]` with no x, it is indicating migrations that have not been run

`./manage.py sqlmigtations <migration name>` will print out the sql in the cmd line

#### Running Migrations

`./manage.py migrate` - This command will migrate all the the un-migrated migrations...
this will generate the sqlite3 db in the project.

### Models

Models are defined in the `models.py` file.
Classes defined here must inherit from `models.Model` which is imported from `django.db`.

```python
from django.db import models

class Note(models.Models):
# For storing ids
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    # This is a one line input
    title = models.CharField(max_length=200)
    # Multiline input
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)
```

**UID** Unique identifier for db tables. They are 32 bit hexadecimals formatted as such: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx`. You can generate one of these numbers with the `uuidgen` command. The uuid4 value must be imported. This is a function

**CharField** - A single line of text input\
**TextField** - An entire field of input

### Migrating a Model

In order for an app to be migrated it must appear under the `INSTALLED_APPS` field of the settings.py file

Once the model has been created and it's app has been added to settings.py, the migrations must be made before they can be migrated. This is done by running `./manage.py makemigrations`

These migrations will show up as .py files with specific names in the **./app/migrations** folder. These are django generated files

_side note:_
If you ever write code that generates a file, add a header that says so. This will help from confusing developers using your software.

#### Interfacing with the DB via Python

Generating data in the db is as simple as declaring a new object from a model class and saving it with the save() method of the model class

```python
n = note(title='Test Note', description="This is a test")

n.save()
```

Getting data from the database is just as simple. Call the object of the model you are looking to retrieve as if it were static.

```python
Note.objects.all()
```

This returns a query object which is a list of objects. The `all()` method will retrieve all of the objects of type `Note`. This is known as an _ORM method_

