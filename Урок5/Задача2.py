evaluations = [2,3,4,5,3,4,5,5,5,5,2,2,4]
count = len(evaluations)
count3 = evaluations.count(3)
count4 = evaluations.count(4)
count5 = evaluations.count(5)
countList = [count3,count4,count5]
progress = sum(countList)/count*100
print(evaluations)
print(countList)
print(progress)
