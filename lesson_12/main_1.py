from re import *

email = "test41@my.h5jg.3gmail.cq."
# user_name = search("^[a-zA-Z]+\w*@", email).group(0)[:-1]
# domain = search("@(\w+\.){1,3}[a-zA-Z.]{2,}$", email).group(0)[1:]
# print("user_name = " + user_name)
# print("domain = " + str(domain))

print("Result = ", match("^[a-zA-Z]+\w*@(\w+\.){1,3}[a-zA-Z.]{2,}$", email) is not None)
