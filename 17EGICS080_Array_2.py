A=input("enter the number")
ab=[]
count=0
count1=0
ab=ab.append(A)
B = A[:len(A)//2]
C = A[len(A)//2:]
for i in B:
    count=count+int(i)
print(count)
for j in C:
    count1=count1+int(j)
print(count1)
if count>count1:
    print(count)
else:
    print(count1)
    