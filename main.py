import sys
from time import sleep
from locations import locations
import re
import json


def get_cmd():
  print("->", end='', flush=True)
  cmd = input().lower()
  return cmd 

def out(string):
  string += "\n"
  for char in string:
      sleep(0.01)
      print(char, end='', flush=True)


player = {
  "name": "",
  "location": "Home",
  "inventory": []
}


def init():
  cmd = get_cmd()
  if cmd == "new":
    return "new_game"
  return cmd

def invalid():
  out("INVALID ACTION")
  return None


def new_game():
  set_name()
  print("\033[H\033[J", end="")
  out("Welcome, " + player["name"])
  return "location_enter"

def set_name(): 
  out("What is your name?")
  name = get_cmd()
  player["name"] = name 

def location_enter(option=""):
  location = locations[player["location"]]
  if option != "skip":
    out(location.intro)
  out("What would you like to do?")
  for action in location.actions:
    out("\t<" + action.upper() + ">")
  cmd = get_cmd()
  return "location_action#" + cmd

def location_action(action):
  location = locations[player["location"]]

  #either do the action or reenter the room
  if action in location.actions:
    return location.actions[action]["action"]()
  else:
    return action 

def location_change(destination):
  options = locations[player["location"]].go_options
  if destination in options:
    player["location"] = options[destination]["location"]
  return "location_enter"


def save_game():
  out("Game Saved")
  with open('player.save', 'w+') as outfile:
    json.dump(player, outfile)

def load_game():
  with open('player.save') as infile:
    player = json.load(infile)
  print("\033[H\033[J", end="")
  out("Welcome back, " + player["name"])


commands = {
  "init": init,
  "new_game": new_game,
  "load_game": None, 
  "location_change": location_change,
  "location_enter": location_enter,
  "location_action": location_action,
}



def run_command(current_command):
  pieces = current_command.split("#")
  cmd = pieces[0] 
  params = []
  for i in range(0, len(pieces)):
    if i != 0:
      params.append(pieces[i])

  if cmd == "exit":
    return cmd, ""
  elif cmd == "save":
    save_game()
    return "location_enter#skip" 
  elif cmd == "load":
    load_game()
    return "location_enter" 

  else:
    if cmd not in commands:
      invalid()
      return "location_enter" 
    if len(params) == 0:
      next_command = commands[cmd]()
    elif len(params) == 1:
      next_command = commands[cmd](params[0])
    else:
      next_command = commands[cmd] (params)

    if next_command == None:
      invalid()
      next_command = current_command
    return next_command

print("\033[H\033[J", end="")
out("Welcome to Benzay. Would you like to start a <NEW> game or <LOAD> an existing game.")
cmd = "init"
last_cmd = ""
while cmd != "exit":
  cmd = run_command(cmd)
print("\033[H\033[J", end="")
print("Goodbye!")
