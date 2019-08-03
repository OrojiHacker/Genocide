from socket import *


def ip(x,y):
      x = gethostbyname(y)
      print ("ip web",web,"is",x)


web = input ("ip  :")
ip(web,web)