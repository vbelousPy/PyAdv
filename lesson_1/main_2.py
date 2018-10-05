import random


def foo(x):
    if 0 < x < 1:
        my_dict = dict({"before": [], "after": []})
        my_list = [random.random() for i in range(50)]
        for i in my_list:
            if i < x:
                my_dict.get("before").append(i)
            else:
                my_dict.get("after").append(i)
        return my_dict
    else:
        raise ValueError


print(foo(0.5))
