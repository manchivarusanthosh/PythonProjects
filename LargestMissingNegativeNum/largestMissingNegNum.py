
array1 = input().split()
array1 = [int(x) for x in array1]

negativeArray = []

for num in array1:
    if num<0:
        negativeArray.append(num)

if len(negativeArray)!=0:
    minNum = min(negativeArray)
    maxNum = max(negativeArray)
    
    isMissNumFound = True
    i= -1
    
    while(isMissNumFound):
        if i>minNum:
            if i not in negativeArray:
                isMissNumFound=False
                print(i)
        elif i<maxNum:
            if i not in negativeArray:
                isMissNumFound = False
                print(i)
        i = i - 1
else:
    print(-1)



