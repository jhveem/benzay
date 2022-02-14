import sys
from locations.locations import locations
from people import people
from time import sleep
import re
import json


class Game:
  def __init__(self, locations):
    self.locations = locations
    self.location = locations["Home"](self)
    self.player = {
    }
    self.commands = {
    }
  
  def out(self, string, clear=False):
    if clear:
      print("\033[H\033[J", end="")
    string += "\n"
    for char in string:
      sleep(0.01)
      print(char, end='', flush=True)

  def get_cmd(self, ignore_case=True):
    print("->", end='', flush=True)
    cmd = input()
    if ignore_case:
        cmd = cmd.lower()
    return cmd 

  def new_game(self):
    self.player = {
      "name": "",
      "gender": "",
      "location": self.location.name,
      "inventory": [],
      "gold": 0
    }
    self.set_name()
    self.out("Welcome, " + self.player["name"], clear=True)
    self.location.init()

  def set_name(self): 
    self.out("What is your name?")
    name = self.get_cmd(ignore_case=False)
    self.player["name"] = name 


  def run(self):
    self.out("Welcome to Benzay. Would you like to start a <NEW> game or <LOAD> an existing game.", clear=True)
    cmd = self.get_cmd()
    if cmd == "new":
      self.new_game()
    elif cmd == "load":
      self.load_game()
    else:
      self.run()

  def invalid(self, cmd):
    if cmd == "exit":
      sys.exit()
    elif cmd == "save":
      self.save_game()
    elif cmd == "gold":
      self.out("You have " + str(self.player["gold"]) + " gold")
    elif cmd == "restart":
      self.run()
    else:
      self.out("INVALID ACTION")

  def save_game(self):
    self.out("Game Saved")
    with open('player.save', 'w+') as outfile:
      json.dump(self.player, outfile)

  def load_game(self):
    self.out("Loading...")
    with open('player.save') as infile:
      player = json.load(infile)
      self.player = player
    print("\033[H\033[J", end="")
    self.out("Welcome back, " + self.player["name"])
    self.location = locations[player["location"]](self)
    self.location.init()

GAME = Game(locations)
GAME.run()
