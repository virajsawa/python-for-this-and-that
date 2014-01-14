import os
import sys
import time

def chat():
 msg = os.system("nc -l 262626 > buffer; cat buffer")
 print("Guest : "+msg+"\n")
 mymsg = raw_input("Me    : ")
 if(mymsg == "quit"):
  quit_func();
 writ = open('buffer','w')  
 writ.write(mymsg)
 writ.close()
 while(~os.system("nc -z "+ip+" 262626")):
  print("Connecting to Guest ... ")
  time.sleep(2)
 os.system("nc "+ip+" 262626 < buffer");
 chat(); 


def quit_func():
 re = raw_input("Are you sure you want to close this connection ? (y/n) : ")
 if(re=='n'):
  pass;
 else: 
  sys.exit("Connection closed\n")
