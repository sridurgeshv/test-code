def fun(num) :
	for i in range(len(num)) :
		if (num[i] == '4' or num[i] == '6' or num[i] == '7') :
			return False
	return True

n=int(input())
c=0
l1=[]
for i in range(1,1000000):
    if (fun(str(i))) :
        c+=1
        l1.append(i)
print(l1[n-1])
