n = range(1,1000)
x=[]
for i in n:
    if i%3==0 or i%5==0:
        x.append(i)

sum=0
for j in x:
    sum += j
    
print(sum)
