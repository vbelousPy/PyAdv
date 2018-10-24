class Foo:

    def __init__(self, x):
        self.x = x

    def __enter__(self):
        self.my_list = [i * self.x for i in range(100)]
        return self.my_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        for i in self.my_list:
            print(i)


with Foo(17) as f:
    for i in f:
        print(i)
