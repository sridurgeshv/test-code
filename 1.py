l=[]
r=0
n=int(input())
while(n>0):
    r=n%3
    l.append(r)
    n=n//3
l.reverse()
for i in range(len(l)):
    print(l[i])
