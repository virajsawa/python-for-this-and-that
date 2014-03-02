def bsort(li):
 itermy = range(len(li))
 itermy.reverse()
 for j in itermy:
  for i in range(j):
   if li[i]>li[i+1]: 
    tup = (li[i+1], li[i])
    li[i], li[i+1] = tup
 return li  
