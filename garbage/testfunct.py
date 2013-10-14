def read(dat):
 catch = dat.seek(0);
 count = 0;
 for ln in dat :
  print(ln, end='');
  count+=1; 
 print('These many lines are there ');
 print(count);
