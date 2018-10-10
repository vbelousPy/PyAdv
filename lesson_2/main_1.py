# def unpacker(*args):
#     for a in args:
#         try:
#             unpacker(*a)
#         except TypeError:
#             my_list.append(a)
#
#
# my_list = list()
# unpacker(1, 2, 3, [1, 2], [3, 4, [5], [6]])
# print(my_list)

# def unpacker(args, my_list=[]):
#     for a in args:
#         try:
#             unpacker(*a, my_list)
#         except TypeError:
#             my_list.append(a)
#     return my_list
#
# some_args = [1, 2, 3, [1, 2], [3, 4, [5], [6]]]
# print(unpacker(some_args))
# print(my_list)


def unpacker(*args):
    my_list = [i for i in args]
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            temp_object = my_list[i]
            my_list.remove(temp_object)
            my_list.extend(temp_object)
            unpacker(*my_list)
    return my_list


print(unpacker(1, 2, 3, [1, 2], [3, 4, [5], [6]]))
