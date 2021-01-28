#json serialisation
import json
person = {"name:": "John", "age": 30, "city": "New York", "hasChildren": False, "title": ["engineer", "programmer"] }

personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON)
with open('person.json', 'w') as file:
    json.dump(person, file) # not json.dumps as 's' is for string


# json desirealization from object

person = {"name:": "John", "age": 30, "city": "New York", "hasChildren": False, "title": ["engineer", "programmer"] }

personJSON = json.dumps(person, indent=4, sort_keys=True)
person = json.loads(personJSON)
print(person)


# json desirealization from file

with open('person.json', 'r') as file:
    person = json.load(file)
print(person)


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)
def encode_json_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Onject of tyype User is not JSON serializable')

userJSON = json.dumps(user, default=encode_json_user)
print(userJSON)


# encode json

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)
userJSON = UserEncoder().encode(user)
print(userJSON)


#decode json


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
