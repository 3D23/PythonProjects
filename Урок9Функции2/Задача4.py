def cacluate(*var):
    middle = sum(var) / len(var)
    list = []
    for i in var:
        if (i > middle):
            list.append(i)
    return (middle,list)

print(cacluate(1,2,3,4,5,6,7,8))