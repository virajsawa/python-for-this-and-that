import os
import sys
import time

#----------------------------- Function Definitions

def chat():
 os.system("nc -l 55555 > buffer")
 rd = open('buffer', 'r')
 msg = str(rd.read()) 
 print("Guest : "+msg)
 mymsg = raw_input("Me    : ")
 if(mymsg == "quit"):
  quit_func();
 writ = open('buffer','w')
 writ.write(mymsg)
 writ.close()
# while(~os.system("nc -z "+ip+" 55555")):
#  print("Connecting to Guest ... ")
#  time.sleep(2)
 os.system("nc "+ip+" 55555 < buffer")
 chat()

def quit_func():
 re = raw_input("Are you sure you want to close this connection ? (y/n) : ")
 if(re=='n'):
  pass;
 else:
  writ = open('buffer','w')
  writ.write("Guest has logged out.")
  writ.close()
  os.system("nc "+ip+" 55555 < buffer")
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
# while(~os.system("nc -z "+ip+" 55555")):
#  print("Connecting to Guest ... ")
#  time.sleep(2)
 os.system("nc "+ip+" 55555 < buffer");
 chat();
else :
 sys.exit("Invalid responce. Exiting.")


