#Program for finding Average of the given data set

from collections import Counter

data = [5,2, 6.5, 8,8,4, 3, 22, 3.5, 66,4, 27,8, 2, 4, 0, 2]

#---------------------------------
if len(data)%2 == 0:
    m = (len(data))/2
    print('Median is',(data[int(m) -1] + data[int(m)])/2) # -1 because indexing starts from zero.
else:
    m = (len(data)+1)/2
    print('Median is', data[int(m) -1 ])

#--------------------------------
sum = 0
for i in range(len(data)) :
    sum += data[i]
print('Mean is', sum/len(data))

#--------------------------------

c = Counter(data)
l = c.most_common()
l.append((0,0))
for i in range(len(l)-1, 0, -1): #it will start checking data from the last but leaving the first element. 
    if l[0][1] == 1:
        print('No mode')
        break
    elif l[0][1] == l[i][1] != 1:
        print('there are more than one modes', end=' - ')
        for n in range(i+1):
            print(l[n][0], end=', ')
        break    
    elif l[0][1] != l[1][1]:
        print('The mode is',l[0][0])
        break
