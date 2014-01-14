import os
import sys
import time
from chat_func import chat
from chat_func import quit_func

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
 while(~os.system("nc -z "+ip+" 262626")):
  print("Connecting to Guest ... ")
  time.sleep(2)
 os.system("nc "+ip+" 262626 < buffer");
 chat();
else :
 sys.exit("Invalid responce. Exiting.")
