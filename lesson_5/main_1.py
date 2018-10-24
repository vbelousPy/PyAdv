class TempClass(type):
    def __str__(self):
        return "abr"


def my_str(self):
    return str(self.__dict__)


Some_Class = type("Some_Class", (), {"a":1, "b":2})
some_class = Some_Class()
some_class.__str__ = my_str(self=So)
print(some_class)