#!/usr/bin/python -u
import sys
import signal
import pickle
from random import choice, shuffle

coworkers_list = ['James', 'Nami', 'Luffy', 'Zoro', 'Tony', 'Robin', 'Franky', 'Brook', 'Ace', 'Jinbe', 'Crocodile']
tools_list = ['drill', 'Knife', 'gun', 'spoon', 'book', 'lighter']

works_list = {
'bomb' : "make boooooooomb!!!",
'coworker' : 'Find Coworker For Escape',
'tool' : "Find Any Tool",
'dig' : "Go Deep~",
}

def menu():
    print "################## Work List ##################"
    for cmd, desc in works_list.iteritems():
        print "  %-15s : %s" %(cmd, desc)
    print "###############################################"

class Esacpe_Player:
  def __init__(self, name, day):
    self.name = name
    self.dig_depth = 0
    self.bomb_Perfection = 0
    self.tools = []
    self.coworkers = []
    self.day = day

  def dig(self):
    self.dig_depth += 1
    # never ending digging......
    print " %s : [Dig] depth = %d" %(self.name, self.dig_depth)
    return pickle.dumps(self)

  def bomb(self):
    self.bomb_Perfection += 1
    # your bomb is too powerful. so boom with u......
    print " %s : [Bomb] bomb Perfection = %d" %(self.name, self.bomb_Perfection)
    return pickle.dumps(self)

  def tool(self):
    tt = choice(tools_list)
    print " %s : [Tool] Find : %s !" %(self.name, tt)
    self.tools.append(tt)
    return pickle.dumps(self)

  def coworker(self):
    shuffle(coworkers_list)
    cw = coworkers_list.pop()
    print " %s : [Coworker] Find : %s !" %(self.name, cw)
    self.coworkers.append(cw)
    return pickle.dumps(self)

class Watcher:
  def __init__(self):
    self.name = "Magellan"
    self.dig_risk = 3
    self.bomb_risk = 10
    self.tool_risk = 5
    self.coworker_risk = 5
    self.arrest_min_point = 25

  def Behavior_analysis(self, Player):
    player_info = pickle.loads(Player)
    risk_point = (player_info.dig_depth*self.dig_risk) + (player_info.bomb_Perfection*self.bomb_risk) + (len(player_info.tools)*self.tool_risk) + (len(player_info.coworkers)*self.coworker_risk)

    if risk_point >= self.arrest_min_point:
      sys.stderr.write("you("+ player_info.name +") looks like dangerous !!!\n")
      self.Arrest()

  def Arrest(self):
    sys.stderr.write("you Arrest Again....\n")
    exit()

def handler(signum, frame):
  sys.stderr.write("Time Out....\n")
  exit()

signal.signal(signal.SIGALRM, handler)
signal.alarm(10)

print("""
                    __           
          PyJail   /__\          
       ____________|  |          
       |_|_|_|_|_|_|  |          
       |_|_|_|_|_|_|__|          
      A@\|_|_|_|_|_|/@@Aa        
   aaA@@@@@@@@@@@@@@@@@@@aaaA    
  A@@@@@@@@@@@@@@@@@@@@@@@@@@A   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[!] Rule
1. After 3 day, the Light will be Turned Off then you Cannot see anything.
2. Cannot Use Some Special Characters in PyJail.
3. For 10 days, You can enter 38 characters per day.

Can You Escape from Here ??
""")

del signal
del __builtins__.input
ban_list = ['#', '+', '-', '_', '"']

name = raw_input(" Name : ")
your = Esacpe_Player(name, 1)
watcher = Watcher()

# FLAG is /FLAG_FILE~blahblah (this is only executable.)

while True:
  print "[day-%d] " %(your.day)
  if your.day == 4:
    # Turn off the light
    print "Turn off the Light !!"
    sys.stdout = open('/dev/null', 'w')

  menu()
  work = raw_input()
  invalid_cmd = 0
  for cmd in works_list.keys():
    if cmd in work:
      invalid_cmd = 1

  if not invalid_cmd:
    print "Invalid Work !!"
    continue

  for ww in work:
    if ww in ban_list:
      print "Found unavailable Character !!"
      exit()

  if len(work) > 38:
    print "Too Long !!"
    continue

  result = eval("your."+work+"()")
  watcher.Behavior_analysis(result)

  your.day += 1
  if your.day > 10:
    sys.stderr.write("10 days over...\n")
    exit()