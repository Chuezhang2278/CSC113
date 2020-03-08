def nonDivisibleSubset(k, s):
    temp = s
    array = []
    
    while temp:
        for i in range(1,len(temp)):
            if((temp[0] + temp[i])% k != 0):
                print(temp[0]+temp[i])
                array.append(temp[0])
                array.append(temp[i])
            elif((temp[0] + temp[i] % k == 0)):
                array.append
        temp.pop(0)
    
    y = set([x for x in array if array.count(x)>1])
    return list(y)

a = [1,2,7,4]

print(nonDivisibleSubset(8,a))