def foo(s):
    result = list()
    for i in s:
        result.append(ord(i))
    return tuple(result)


def test_script():
    result = foo("xYz")
    if result == (120, 89, 122):
        print("Ok")
    else:
        print("Error")


test_script()
