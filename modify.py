import sys

#modifying module1_fun.m
try:
  stre = open('module1_fun.m', 'r');
  stre.seek(0);
  data = stre.readlines();
  stre.close();
  data[2067]='\n';
  try:
    writ = open('module1_fun.m', 'w');
    for lin in data:
     writ.write("%s" % lin);
    writ.close();
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)   
except IOError as e:
  print "I/O error({0}): {1}".format(e.errno, e.strerror)


#modifying module1_guess.m
try:
  stre = open('module1_guess.m', 'r');
  stre.seek(0);
  data = stre.readlines();
  stre.close();
  data[470]='\n';
  data[2573]='\n';
  try:
    writ = open('module1_guess.m', 'w');
    for lin in data:
     writ.write("%s" % lin);
    writ.close();
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)   
except IOError as e:
  print "I/O error({0}): {1}".format(e.errno, e.strerror)


#modifying module1.m
try:
  stre = open('module1.m', 'r');
  stre.seek(0);
  data = stre.readlines();
  stre.close();
  data[2162]='\n';
  try:
    writ = open('module1.m', 'w');
    for lin in data:
     writ.write("%s" % lin);
    writ.close();
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)   
except IOError as e:
  print "I/O error({0}): {1}".format(e.errno, e.strerror)

print("files modified");
