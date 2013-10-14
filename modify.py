import sys

#modifying module1_fun.m
try:
  stre = open('module1_fun.m', 'r');
  stre.seek(0);
  data = stre.readlines();
  stre.close();
  data[2067]='';
  try:
    writ = open('module1_fun.m', 'w');
    for lin in data:
     writ.write("%s\n" % lin);
    writ.close();
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)   
except IOError as e:
  print "I/O error({0}): {1}".format(e.errno, e.strerror)
