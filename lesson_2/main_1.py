def unpacker(*args):
    my_list = [i for i in args]
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            temp_object = my_list[i]
            my_list.remove(temp_object)
            my_list.extend(temp_object)
            my_list = unpacker(*my_list)
    return my_list


print(unpacker(1, 2, 3, [1, 2], [3, 4, [5], [6]]))
