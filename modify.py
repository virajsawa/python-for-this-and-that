import sys

try:
  stre = open('module1_fun.m', 'r');
  stre.seek(0);
  data = stre.readlines();
  for entry in data:
   if entry == " % All individual species expressions listed here" : 
    print("found");
    stre.tell();
    break;
  stre.close()
  print(data[2067]);
except IOError as e:
  print "I/O error({0}): {1}".format(e.errno, e.strerror)
