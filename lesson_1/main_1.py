def foo(s):
    return (ord(i) for i in s)


def test_script():
    result = foo("xYz")
    if list(result) == [120, 89, 122]:
        print("Ok")
    else:
        print("Error")


test_script()
