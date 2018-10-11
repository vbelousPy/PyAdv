def unpacker(*args):
    my_list = [i for i in args]
    for i in range(len(my_list)):
        if isinstance(my_list[i], (list, tuple, set, frozenset)):
            my_list = unpacker(*(my_list[0:i] + my_list[i] + my_list[i + 1:]))
    return my_list


print(unpacker(1, 2, 3, [1, 2], [3, 4, [5, [66]], [6]]))
