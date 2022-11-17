n=4
lst=['great','hello','hiyo','abc']

for i in range(n):
  for j in range(i+1,n):
    if ord(lst[i][-2])>ord(lst[j][-2]):
      temp=lst[i]
      lst[i]=lst[j]
      lst[j]=temp
print(lst)
