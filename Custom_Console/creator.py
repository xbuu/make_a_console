# Importing

import os
import time
import colorama
import webbrowser as wb
import ctypes
import random

# Variables

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

# Function

def cprint(string):
    print(yellow + ":: " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    - " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "#: " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    #- " + normal + string)
# ---------------------------------------------
def cwarn(string):
    print(yellow + "_! " + normal + string)
# ---------------------------------------------
def scwarn(string):
    print(yellow + "    _! " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "?> " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    ?> " + normal + string)
# ---------------------------------------------
def cnotice(string):
    print(green + "!> " + normal + string)
# ---------------------------------------------
def scnotice(string):
    print(green + "    !> " + normal + string)
# ---------------------------------------------
def cinput(string):
    input(yellow + ":: " + normal + string)
# ---------------------------------------------
def scinput(string):
    input(yellow + "    - " + normal + string)
# ---------------------------------------------
def cmdinput(string):
    input(green + ">> " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)

# Console Variables

intro = '''

'''
commands = ["",
            ""]

# Introduction

os.system("cls")
cinfo("welcome to console creator")
wait(.02)
cinfo("this looks bland, right?")
wait(1)
cinfo("yeah, it does but here you can")
cinfo("edit and create your own console")
cinfo("including commands")
wait(.02)
cinfo("have fun!!")
wait(3)
os.system("cls")

# Creator

# Intro Create

os.system("cls")
cinfo("Enter your text for the intro")
scinfo("This could be anything")
newintro = input("")
intro = newintro
print("##############################")
print(intro)
print("##############################")
cinfo("cool, nice intro bro.")
wait(.002)
cinfo("now lets go to the next step")

wait(1)

# Command Creator

os.system("cls")
cinfo("Enter a command")
newcmd = input("")
cinfo("cool, now call that command")
callcmd = input("> ")
if callcmd == newcmd:
    print("hi this appeared when you called your new command")
    wait(0.2)
    print("that's cool")
else:
    cinfo("hey uh, you spelt it wrong...")
    cinfo("your command is " + newcmd)
    cinfo("lets try again later.")

wait(1)

# Description Creator

os.system("cls")
cinfo("Alright, now create your description for the console.")
desc = input("")
print("##############################")
print(desc)
print("##############################")
cinfo("Nice description")
wait(1)

# View Console

os.system("cls")
cinfo("Alright, lets view your console!")

print(intro)
print("")
print(desc)
print("say " + newcmd + " for a command")
callcmd = input("> ")
if callcmd == newcmd:
    print("yoo so uhh..")
    wait(0.4)
    print("i dont know what to do here")
    wait(1)
else:
    cerror("oops")
    time.sleep(.5)

wait(1)