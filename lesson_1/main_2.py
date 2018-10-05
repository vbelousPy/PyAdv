import random


def foo(x):
    if 0 < x < 1:
        my_dict = dict({"before": [], "after": []})
        for i in [random.random() for i in range(50)]:
            if i < x:
                my_dict.get("before").append(i)
            else:
                my_dict.get("after").append(i)
        return my_dict
    else:
        raise ValueError


print(foo(0.5))
