number = raw_input('Enter the number here: ');

arr = [];
for iter in str(number):
  arr.append(int(iter));
  
size = len(arr);

if(size%2==0):
  k=size;
  while(k>((size/2)+1)):
    arr[k-1]=arr[size-k];
    k=k-1;
  if(arr[(size/2)]>arr[((size/2)-1)]): 
    arr[(size/2)-1]=arr[size/2];
  elif(arr[(size/2)]<arr[((size/2)-1)]): 
    arr[size/2]=arr[(size/2)-1];
  for itter in arr:
    print itter,

elif(size%2 !=0):
  k=size;
  while(k>((size/2)+1)):
    arr[k-1]=arr[size-k];
    k=k-1;
  newnum = 0;
  indx = size-1;
  for item in arr:
    newnum = newnum + item*(10^indx);
    indx = indx -1;
  if newnum < int(number):
    if(arr[size/2]==9):
      l=0;
      while(arr[(size/2)-l]==9):
        arr[(size/2)-l]=0;
        arr[(size/2)-l-1]+=1;
        arr[size-((size/2)-l)]=arr[(size/2)-l-1];
        l+=1;
    else:
      arr[size/2]+=1;
  for x in arr:
    print x,

         