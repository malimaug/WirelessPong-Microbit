test = "{'hello': 0}"
if test[0] == '{':
    print(eval(test))
else:
    print(test)