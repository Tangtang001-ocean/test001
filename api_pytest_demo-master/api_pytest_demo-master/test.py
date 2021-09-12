

import json

# a = { "aa":22,"people": [
#
# { "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" },
#
# { "firstName": "Jason", "lastName":"Hunter", "email": "bbbb"},
#
# { "firstName": "Elliotte", "lastName":"Harold", "email": "cccc" }
#
# ],"bb":"nlll"}

# param_dict = json.loads(str(a))
# print(param_dict)
# items = param_dict.items()
# for key,value in items:
#     print(str(value))

#
# inp_strr = '{"k1":123, "k2": [{"22":11}], "k3":"ares"}'
#
#
# # inp_strr = '{ "aa":22,"people": [{ "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" },{ "firstName": "Jason", "lastName":"Hunter", "email": "bbbb"},{ "firstName": "Elliotte", "lastName":"Harold", "email": "cccc" }"],"bb":"nlll"}'
# inp_dict = json.loads(inp_strr)
# # print(inp_dict)
# items = inp_dict.items()
# for key,value in items:
#     # print(str(value))
#     if value == [{"22":11}]:
#         bb  = str(value).split("[")[1].split("]")[0]
#         c = bb.replace("'", "\"")
#         # print(str(c))
#
#         dict11 = json.loads(c)
#         for key,value in dict11.items():
#             print(str(value))
import re
str2 = "@Wg*中国6aSssddd"

print(type(list(str2)))
# for i in range(0,len(list(str2))):
#     print(list(str2)[i])
#     if re.match( '^[-+]?(([0-9]+([.][0-9]*)?)|(([0-9]*[.])?[0-9]+))$',list(str2)[i] ):
#         print("true")
#     else:
#         print("f")

for i in list(str2):
    if re.search("(\d+)",str(i)):
        print("----------------------")
    else:
        print("fffffffffffffffffffffffff")


# i = 0
# while i < len(str2 ):
#     print(str2[i])
#     i = i+1
#     str1 = str(i)
#     print(str1.isdecimal())
#
#     print(str1.isdigit())
#
#     print(str1.isnumeric())

    # if i == [0,9]:
    #     print("True")
    # else:
    #     print("fales")