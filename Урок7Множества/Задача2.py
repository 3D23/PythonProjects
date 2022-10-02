testList = [1,2,2,[3,4],(1,2,3),'1',{1,2,3}]
testSet = set()
help = True
for i in testList:
    if ((type(i) == set or type(i) == dict or type(i) == list)):
        help = False
        break
for i in testList:
    if (not(type(i) == set or type(i) == dict or type(i) == list)):
        testSet.add(i)
print(help,testSet)