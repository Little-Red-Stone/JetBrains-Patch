import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
def run_sh(op):
    return os.popen(op).read().split()
def clear():
    os.system("clear")
def txt_split(txt):
    new=""
    flag=False
    for i in txt:
        if i=="/":
            flag=True
            continue
        if flag:
            flag=False
            continue
        new+=i
    return new

try:
    with open("config", 'r') as f:
        confL=f.readlines()
except:
    confL=None

usrName = run_sh("id -un")[0]
path = "/Users/"+usrName+"/"
clear()
print("What name do you want to use?")
name=input("Name=")
print("What time limit do you want?")
year=input("Year=")
mon=input("Month=")
day=input("Day=")
clear()

print("Operating...")
with open(path+"janf_config.txt", 'w') as f:
    f.write("[DNS]\n")
    f.write("EQUAL,jetbrains.com\n")
    f.write("[URL]\n")
    f.write("PREFIX,https://account.jetbrains.com/lservice/rpc/validateKey.action\n")
    f.write("[MyMap]\n")
    f.write("EQUAL,licenseeName->"+name+"\n")
    f.write("EQUAL,gracePeriodDays->30\n")
    f.write("EQUAL,paidUpTo->"+year+"-"+mon+"-"+day+"\n")
print("Operate successfully")