![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)
<h1 align ="center"> AIR BNB CLONE </h1><br>

# AirBnb Clone Console
A Command Interpreter to Manage AirBnb objects.

## Project Notes
### Environment
Files interpreted/run on Ubuntu 14.04 LTS with Python 3
### Style
All code is written in accordance with Pep8 https://www.python.org/dev/peps/pep-0008/
## How to use the Console
### To start:
* Interactive mode, `$ ./console.py`, and you will prompted with `(hbnb)`
*Non-interactive mode, `$ echo "help" | ./console.py`
### To close:
* Type either `EOF` or `quit`
### Command usage of Console:
* `help`
  * Usage: `help`
  * Documentation/help provided
* `create`
  * Usage: `create BaseModel`
  * Creates a new instance of a class, saves it (to the JSON file) and prints the `id`
* `show`
  * Usage: `show BaseModel 1234-5847-3912`
  * Prints the string representation of an instance based on the class name and `id`
* `destroy`
  * Usage: `destroy BaseModel 1234-5847-3912`
  * Deletes an instance based on the class name and `id` (save the change into the JSON file). 
* `all`
  * Usage: `all`
  * Prints all string representation of all instances based or not on the class name.
* `update`
  * Usage: `update User 1234-5678-9101 email 2109@holbertonschool.com`
  * Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
### Files
### `console.py`
Module for Main Console
* `class HBNBCommand(cmd.Cmd)` includes:
  * `def emptyline(self)` : method to handle empty line 
  * `def do_quit(self, line)` : quit command method to exit console
  * `def do_create(self, arg)` : method to make new instance, saves it, and print id
  * `def do_show(self, arg)` : method to print string representation of an instance based on class name/id
  * `def do_destroy(self, arg)` : method to deletes instance based on class name/id
  * `def do_all(self, arg)` : prints string representation of all instances or all instances of a class
  * ` def do_update(self, arg)` : method to update instance based on class name/id by adding/updating attribute
### `base_model.py`
Module for Base Model
* `class BaseModel` includes:
  * `def __init__(self, *args, **kwargs)` : method to initialize instance
  * `def save(self)` : method to update attributes `updated_at` with current datetime.
  * `def to_json(self)` : method to return dictionary of all key/values of instance and teh class name
  * `def __str__(self)` : method to print dictionary of attributes of the instance.
### `amenity.py`
Module for Amenity Model
* `class Amenity` includes:
  * `def __init__(self, *args, **kwargs) : method to make an instance of amenity
### `city.py`
Module for City Model
* `class City` includes:
  * `def __init__(self, *args, **kwargs) : method to make instance of amenity
### `place.py`
Module for Place Model
* `class Place` includes:
  * `def __init__(self, *args, **kwargs) : method to make an instance of place
### `review.py`
Module for Review Model
* `class Review` includes:
  * `def __init__(self, *args, **kwargs) : method to initialize instance of review
### `state.py`
Module for State Model
* `class State` includes:
  * `def __init__(self, *args, **kwargs) : method to make an instance of state
### `user.py`
Module for User Model
* `class User` includes:
  * `def __init__(self, *args, **kwargs) : method to make instance of user
### `__init__.py`
* initializes package
### `file_storage.py`
Module for serializing and deserializing instances and JSON
* `class FileStorage` includes:
  * `def all(self)` : methods to return __objects
  * `def new(self, obj)` : method to set obj in __objects with key/value pair 
  * `def save(self)` : method to serialize __objects to JSON file
  * `def reload(self)` : method to deserialize the JSON to __objects
## Test Files : Unit Tests for respectively named files
### * [Test Amenity](./tests/models/test_amenity.py)
### * [Test Base Model](./tests/models/test_base_model.py)
### * [Test City](./tests/models/test_city.py)
### * [Test Init](./tests/models/test__init__.py)
### * [Test Place](./tests/models/test_place.py)
### * [Test Review](./tests/models/test_review.py)
### * [Test State](./tests/models/test_state.py)
### * [Test User](./tests/models/test_user.py)

## Authors
* Matias Zappino, <a href='https://github.com/matiaszappino'>Github</a>
* Flavio Orlando, <a href='https://github.com/flaviomco'>Github</a>
