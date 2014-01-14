import os
import sys
import time

#----------------------------- Function Definitions

def chat():
 msg = str(os.system("nc -l 55555 > buffer; cat buffer"))
 print("Guest : "+msg+"\n")
 mymsg = raw_input("Me    : ")
 if(mymsg == "quit"):
  quit_func();
 writ = open('buffer','w')
 writ.write(mymsg)
 writ.close()
 while(~os.system("nc -z "+ip+" 55555")):
  print("Connecting to Guest ... ")
  time.sleep(2)
 os.system("nc "+ip+" 55555 < buffer");
 chat();

def quit_func():
 re = raw_input("Are you sure you want to close this connection ? (y/n) : ")
 if(re=='n'):
  pass;
 else:
  sys.exit("Connection closed\n")

#----------------------------------------------------------------------------


print("++++++++++ Welcome to pynec ++++++++++\n\n")
ip = str(raw_input("Enter the ip address of the guest : "))

reply = raw_input("\n\nDo you want to begin the chat (y/n) : ")

if(reply == "n"):
 chat()
elif(reply == "y"):
 mymsg = raw_input("Me    : ")
 if(mymsg == "quit"):
  quit_func();
 writ = open('buffer','w')
 writ.write(mymsg)
 writ.close()
 while(~os.system("nc -z "+ip+" 55555")):
  print("Connecting to Guest ... ")
  time.sleep(2)
 os.system("nc "+ip+" 55555 < buffer");
 chat();
else :
 sys.exit("Invalid responce. Exiting.")


