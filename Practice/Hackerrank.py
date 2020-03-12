# hackerrank challege question number 2 for CTP
# Not sure if this was quesiton but
# you have double array as logs and you want to find duplicate numbers
# if # of duplicate amount passes threshold count return it
# duplicates dont count if they are within the same array 
# i.e
# [1,2,2], [2,3,4], in the first array there are two 2's present
# it doesnt count as duplicate. 

# My solution is highly unefficient and can be improved upon by using dictionaries
# Even then it could be improved upon. Will do in late date

def processLogs(logs, threshold):
    x2 = logs
    y = set()
    for i in range(len(x2)):
        for j in range(len(x2[i])):
            count = 0
            for k in range(i+1,len(x2)):
                for l in range(len(x2[k])):
                    print(x2[i][j], "compared to", x2[k][l])
                    if(x2[i][j] == x2[k][l]):
                        count += 1
    
                if(count >= threshold):
                    y.add(x2[i][j])  
    
    z = list(y)
    z.sort()
    return z  

test1 = [[1,2,4],[4,0,2],[4,2,8]]
print(processLogs(test1, 2))