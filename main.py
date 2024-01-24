from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=800, height=600, background="white")


#setting all
def setInitialValues():
  global pgNum, score, gameRunning, xMouse, yMouse
  pgNum = 0
  score = 0
  xMouse = 0
  yMouse = 0

  screen.update
  
  gameRunning = True

# introScreen =
objective = screen.create_text(785,585, text="Try to get all the endings!",font = ("lexend", "10", "bold"),fill="gray", anchor = E)
title = screen.create_text(400,300, text="Mini Miki!",font = ("lexend", "30", "bold"),fill="pink")
subTshdw = screen.create_text(405,405,text="~Hikikomori Rehab Sim~",font = ("lexend 15 bold"),fill="light gray")
subtitle = screen.create_text(400,400,text="~Hikikomori Rehab Sim~",font = ("lexend 15 bold"),fill="black")
intro = screen.create_text(400,500,text="Click to Play!", font = ("lexend 10 bold underline"),fill="pink")

#Every time the player clicks the mouse, this procedure gets called. The procedure "flips throough the pages" of the visual novel.
def mouseClickHandler( event ):
  global textbox, pgNum, xMouse, yMouse, score
  xMouse = event.x
  yMouse = event.y
  if pgNum == 6:
    
    if 100 <= xMouse <= 700 and 201 <= yMouse <= 400:
      normEnd()

    elif 100 <= xMouse <= 700 and 0 <= yMouse <= 200:
      for item in screen.find_all(): 
        screen.delete(item)
      textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
      pgNum = pgNum + 1
      pg(pgNum)

  elif pgNum == 23:
    if 100 <= xMouse <= 700 and 201 <= yMouse <= 400:
      for item in screen.find_all(): 
        screen.delete(item)
      textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
      score = score + 1
      pgNum = pgNum + 1
      pg(pgNum)

    elif 100 <= xMouse <= 700 and 0 <= yMouse <= 200:
      for item in screen.find_all(): 
        screen.delete(item)
      textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
      score = score - 1
      pgNum = pgNum + 1
      pg(pgNum)

  elif pgNum == 30:
    if 100 <= xMouse <= 700 and 201 <= yMouse <= 400:
      for item in screen.find_all(): 
        screen.delete(item)
      textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
      score = score - 1
      pgNum = pgNum + 1
      pg(pgNum)

    elif 100 <= xMouse <= 700 and 0 <= yMouse <= 200:
      for item in screen.find_all(): 
        screen.delete(item)
      textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
      score = score + 1
      pgNum = pgNum + 1
      pg(pgNum)

  elif pgNum == 36:
    if 0 <= xMouse <= 800 and 0 <= yMouse <= 600:
      if score > 0:
        happyEnd()
      
      elif score < 0:
        badEnd()

  else:
    for item in screen.find_all(): 
     screen.delete(item)
    textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
    scorekeeper = screen.create_text(700,30,text = f"Score:{score}", font = ("comfortaa 15"),fill="black", anchor = W)
    pgNum = pgNum + 1
    pg(pgNum)

#pages for the visual novel
def pg(pgNum):
  global gmScrn, drawGmScrn
  if pgNum == 1:
    gmScrn = PhotoImage( file="Pg/gamechat.png" )
    drawGmScrn = screen.create_image(400,200,image = gmScrn,anchor = CENTER)
    txt = screen.create_text(25,450,text = "whisper/MiKi350: Haha u suck at dis game quit it already bruh\nwhisper/MiKi350-user123: Wth man u wanna go?\nwhisper/MiKi350:Yeah lets go XXXX **** St come over and fight me\nwhisper/MiKi350-user123:ure ded", font = ("comfortaa 15"),fill="white", anchor = W)
    
  elif pgNum == 2:
    txt = screen.create_text(25,420,text = "My name is Miki.", font = ("comfortaa 20"),fill="white", anchor = W)
    
  elif pgNum == 3:
    txt = screen.create_text(25,420,text = "I just started a real life fight with someone.", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 4:
    txt = screen.create_text(25,450,text = "Why did I even do that?! I shouldn't have doxxed\nmyself even if I was super mad!", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 5:
    txt = screen.create_text(25,450,text = "Welp, it's not like they're actually going to come-\nI guess I'll get some sleep..", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 6:
    txt = screen.create_text(25,450,text = "Go to the address and beat this prick up?", font = ("comfortaa 20"),fill="white", anchor = W)
    chc1Brdr = screen.create_rectangle(100,50,700,150,fill="pink",outline="magenta")
    chc2Brdr = screen.create_rectangle(100,250,700,350,fill="pink",outline="magenta")
    chc1 = screen.create_text(400,100, text = "a) Yes. Confrontation is at need.",font = ("comfortaa 20"),fill="black", anchor = CENTER)
    chc2 = screen.create_text(400,300, text = "b) Nah. I'm too lazy.", font = ("comfortaa 20"),fill="black", anchor = CENTER)

      
  elif pgNum == 7:    
    txt = screen.create_text(25,450,text = "okay I'm here. I'm going to call this guy's username\nout so loud- MIKI350 GET THE HECK OUT HERE!!!!!", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 8:
    txt = screen.create_text(25,450,text = "W-what? Who the heck is that??? Ugh, the landlord lady\ngets super mad when it gets noisy..!",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 9:
    txt = screen.create_text(25,450,text = "MiKi350!!!",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 10:
    txt = screen.create_text(25,450,text = "SHHHHHHH!!! You're going to make the landlord mad!",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 11:
    txt = screen.create_text(25,450,text = "are you MiKi350?",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 12:
    txt = screen.create_text(25,450,text = "Oh shoot. This dude is the dumb player from the game..\nthey actually came to kill me!",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 13:
    txt = screen.create_text(25,450,text = "Uhm.. uh..",fill="white", anchor = W)

  elif pgNum == 14:
    txt = screen.create_text(25,450,text = "'Ah, this is definitely MiKi350.'",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 15:
   txt = screen.create_text(25,450,text = "We have a lot of talking.. to do, don't we?",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 16:
    txt = screen.create_text(25,450,text = "'EEEK! That dude's cracking their knuckles!! I'm dead,\nI'm dead, I'm dead..!'",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 17:
    txt = screen.create_text(25,450,text = "Kidding. You look too much of a wimp. And a basement\ndweller.",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 18:
    txt = screen.create_text(25,450,text = "Wow... That's SO nice. Thanks.",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 19:
    txt = screen.create_text(25,450,text = "Hey, you're the one who insulted me first. Let me have\nthis.",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 20:
    txt = screen.create_text(25,450,text = "Valid. Now can you please leave? I don't want the\nlandlord lady to come.",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 21:
    txt = screen.create_text(25,450,text = "Nah. Let me in that little basement of yours. I'm bored.",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 22:
    txt = screen.create_text(25,450,text = "W-what? No way!",font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 23:
    txt = screen.create_text(25,450,text = "How should I coax this dude?", font = ("comfortaa 20"),fill="white", anchor = W)
    chc1Brdr = screen.create_rectangle(100,50,700,150,fill="pink",outline="magenta")
    chc2Brdr = screen.create_rectangle(100,250,700,350,fill="pink",outline="magenta")
    chc1 = screen.create_text(400,100, text = "a) Threaten Miki with violence.",font = ("comfortaa 20"),fill="black", anchor = CENTER)
    chc2 = screen.create_text(400,300, text = "b) Convince Miki with words.", font = ("comfortaa 20"),fill="black", anchor = CENTER)

  elif pgNum == 24:
    txt = screen.create_text(25,450,text = "After a little bit of argument, I got into MIki's humble\nabode.", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 25:
    txt = screen.create_text(25,450,text = "..Welcome, I guess? Although you did barge in..", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 26:
    txt = screen.create_text(25,450,text = "Ah, don't mind me. Just here to make a new friend.", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 27:
    txt = screen.create_text(25,450,text = "...but why would you want to make friends with\nsomeone like me?", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 28:
    txt = screen.create_text(25,450,text = "Who is someone like you?", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 29:
    txt = screen.create_text(25,450,text = "I mean.. I'm a non-sociable, cooped-up weirdo.. it's odd\nthat you'd even have the idea to try to be friends with\nme.", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 30:
    txt = screen.create_text(25,450,text = "How should I respond to this?", font = ("comfortaa 20"),fill="white", anchor = W)
    chc1Brdr = screen.create_rectangle(100,50,700,150,fill="pink",outline="magenta")
    chc2Brdr = screen.create_rectangle(100,250,700,350,fill="pink",outline="magenta")
    chc1 = screen.create_text(400,100, text = "a) Woah, pump the self-hate breaks, man.\nStaying inside doesn't make you a weirdo.\nPeople have their preferences.",font = ("comfortaa 20"),fill="black", anchor = CENTER)
    chc2 = screen.create_text(400,300, text = "b) *listen to Miki without saying anything*", font = ("comfortaa 20"),fill="black", anchor = CENTER)

  elif pgNum == 31:
    txt = screen.create_text(25,450,text = "A-anyways, what are you going to do?", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 32:
    txt = screen.create_text(25,450,text = "You choose, you're the host.", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 33:
    txt = screen.create_text(25,450,text = "..okay, wanna play games then?", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 34:
    txt = screen.create_text(25,450,text = "Sure, what do you have?", font = ("comfortaa 20"),fill="white", anchor = W)
    
  elif pgNum == 35:
    txt = screen.create_text(25,450,text = "Sure, what do you have?", font = ("comfortaa 20"),fill="white", anchor = W)

  elif pgNum == 36:
    txt = screen.create_text(25,450,text = "We played for a while together, and I went home, having\nmade a new friend.", font = ("comfortaa 20"),fill="white", anchor = W)
    
   

    
#badending


def normEnd():
  for item in screen.find_all(): 
    screen.delete(item)
  textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
  normMsg = screen.create_text(400,200, text = "Normal Ending", font = ("comfortaa 30"),fill="pink", anchor = CENTER)
  txt = screen.create_text(25,450,text = "Congrats! You're a normal dude.", font = ("comfortaa 20"),fill="white", anchor = W)

def happyEnd():
  for item in screen.find_all(): 
    screen.delete(item)
  textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
  happMsg = screen.create_text(400,200, text = "Good Ending", font = ("comfortaa 30"),fill="pink", anchor = CENTER)
  txt = screen.create_text(25,450,text = "I hope they come again.. hehe", font = ("comfortaa 20"),fill="white", anchor = W)

def badEnd():
  for item in screen.find_all(): 
    screen.delete(item)
  textbox = screen.create_rectangle(0,400,800,600, fill = "light blue")
  sadMsg = screen.create_text(400,200, text = "Bad Ending", font = ("comfortaa 30"),fill="pink", anchor = CENTER)
  txt = screen.create_text(25,450,text = "..That was terrible. I hate myself. ugh, it's not like I\nexpected them to understand me.. I'll be\nstuck here forever until I die. Hope they never come again.", font = ("comfortaa 20"),fill="white", anchor = W)


#Updates the position and speed of all objects on screen
def updateObjects():
  global yRocket, ySpeed
  

  yRocket = yRocket + ySpeed  #Updates the rocket's vertical position (negative speed = going up)
  ySpeed = ySpeed + 0.6     #Gravity is constantly increasing the rocket's downward speed


#The main procedure that runs the game.
#It gets called 500 milliseconds after the program starts

  ######
introScreen = True


######


def runGame():       
  setInitialValues()
  
  
  while True:
      
    screen.update()

root.after( 1000, runGame)

screen.bind("<Button-1>", mouseClickHandler) 

screen.pack()
screen.focus_set()
root.mainloop()
