import copy

# A generic Prototype class which is able to clone any object
# Of course, this is very possible in Python due to it being dynamically and weakly typed language
class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name, obj):
        del self._objects[name]

    def clone(self, name, **attr):
        # Deep clones the object, and modify the attributes
        obj = copy.deepcopy( self._objects.get(name) )
        obj.__dict__.update(attr)
        return obj


class Comment:
    def __init__(self, id, username, text):
        self.id = id
        self.username = username
        self.text = text

    def __str__(self):
        return f"{self.id} {self.username} {self.text}"





if __name__ == '__main__':
    # Example comments fetch from database
    comments = [
        {"id": 1, "username": "Bob", "text": "Hi!"},
        {"id": 2, "username": "Adrain", "text": "Yo!"},
        {"id": 3, "username": "James", "text": "HHH!"},
        {"id": 4, "username": "Sam", "text": "Damn!"},
        {"id": 5, "username": "Paul", "text": "Dude!"},
        {"id": 6, "username": "Alex", "text": "Senyour!"},
        {"id": 7, "username": "Zen", "text": "Yoo!"},
        {"id": 8, "username": "Tim", "text": "Yes!"},
    ]

    # Prototypical instance
    prototype_instance = Comment(0, "", "")
    prototype = Prototype()
    prototype.register_object('comment', prototype_instance)

    # Now clone comments
    for comment in comments:
        c = prototype.clone('comment', **comment)
        print(c)