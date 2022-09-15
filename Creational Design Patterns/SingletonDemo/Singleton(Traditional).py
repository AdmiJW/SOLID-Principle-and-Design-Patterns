

class Singleton:
    __creation_key = object()
    _instance = None

    # We cannot have private constructor in Python. Thus, we require a key to allow instance to be created
    def __init__(self, create_key):
        assert(create_key == Singleton.__creation_key), "Singleton class cannot be instantiated"

    # get_instance must be a static method
    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton(Singleton.__create_key)
        return Singleton._instance


if __name__ == '__main__':
    # Check if the instace obtained is same?
    inst1 = Singleton.get_instance()
    inst2 = Singleton.get_instance()

    # Is the instance same?
    print(inst1 is inst2)

    # Try to instantiate a new Singleton - Expect an Error
    Singleton('Invalid key')
