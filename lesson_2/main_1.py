def unpacker(*args):
    my_list = [i for i in args]
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            temp_object = my_list[0:i]
            temp_object.extend(my_list[i])
            temp_object.extend(my_list[i + 1:])
            my_list = unpacker(*temp_object)
    return my_list


print(unpacker(1, 2, 3, [1, 2], [3, 4, [5, [66]], [6]]))
