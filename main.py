#savecode python /input
import random
import datetime
from math import *
import os
from glob import *
from urllib.request import urlopen
import hashlib

def md5(str):
  return hashlib.md5(str.encode(encoding='UTF-8')).hexdigest()

userlist=["yemaster","liziheng","Happynewyear","Sopa","yuntianming","bossbaby", "jmoo", "ZnS"]
userDict={
    "yemaster":"[CQ:at,qq=1440169768]",
    "liziheng":"[CQ:at,qq=2213220653]",
    "Happynewyear":"[CQ:at,qq=2717885529]",
    "Sopa":"[CQ:at,qq=245608072]",
    "yuntianming":"[CQ:at,qq=1130807396]",
    "bossbaby":"[CQ:at,qq=3064273390]", 
    "jmoo":"[CQ:at,qq=3252484542]",
    "ZnS":"[CQ:at,qq=1292979572]"
}
a=input().split()
if a[0]=="随便膜":
  for i in range(0, int(a[1])):
    print("%%%"+random.choice(userlist))
elif a[0]=="播报现在时间" or a[0]=="几点了":
  print("现在是："+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
elif a[0]=="全部给我膜拜":
    if len(a)>=1:
      for i in range(0, int(a[1])):
        for user in userlist:
          print("%%%"+userDict[user])
    else:
      for user in userlist:
        print("%%%"+userDict[user])
elif a[0]=="我想膜拜":
  if a[1]=="所有人":
    for user in userlist:
      print("%%%"+user)
  elif a[1] in userlist:
    if len(a)>=2:
      for i in range(0, int(a[2])):
        print("%%%"+userDict[a[1]]+"巨佬")
    else:
      print("%%%"+userDict[a[1]]+"巨佬")
  else:
    print("这个人我不认识，那我还是膜一下吧")
    print("%%%"+a[1])
elif a[0]=="给我说":
  said=""
  for i in range(3, len(a)):
    if a[i] in userlist:
      a[i] = userDict[a[i]]
    said=said+a[i]+" "
  if a[1]=="不停":
    a[1]=1000
    said=a[2]+" "+said
  for i in range(0, int(a[1])):
    print(said)
elif a[0]=="计算":
  print("Result: "+str(eval(a[1])))
elif a[0]=="喊一下" or a[0]=="喊":
  if a[1]=="所有人":
    said=""
    for user in userlist:
      said=said+userDict[user]+" "
  else:
    said=""
    for i in range(1, len(a)-1):
      if a[i] in userlist:
        said=said+userDict[a[i]]+" "
      else:
        said=said+a[i]+" "
  if a[len(a)-1] in userlist:
    said=said+userDict[a[len(a)-1]]
    print(said+" 有人请你喝茶[CQ:face,id=60]")
  else:
    print(said+" "+a[len(a)-1])
else:
  print("不知道你是什么意思欸")
