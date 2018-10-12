def foo(hello):
    def internal(name):
        return hello + name
    return internal


some_foo = foo("Hello, ")
print(some_foo("Ivanov"))
print(some_foo("Petrov"))
