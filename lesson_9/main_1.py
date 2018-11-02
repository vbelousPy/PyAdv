class SingleTone:
    __instance = None
    a = None

    def __init__(self) -> None:
        if self.a is None:
            self.a = 1

    def __new__(cls):
        if SingleTone.__instance is None:
            SingleTone.__instance = object.__new__(cls)
        return SingleTone.__instance

    def foo(self):
        return self.a * 2


s1 = SingleTone()
print(s1.foo())
s1.a = 2
print(s1.foo())
s1.a=3
s2 = SingleTone()
print(s2.foo())
s2.a = 5
print(s1.foo())