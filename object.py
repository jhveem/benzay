from interface import out, get_cmd

class Object:
  def __init__(self, name):
    #set after imported into a game
    self.game = {}
    self.name = name
    self.description = ""
    #
    ##description
    ##action
    ##one_time
    ##used
    ##alt_description
    self.actions = {}

  def examine(self):
    out(self.description)
    if self.actions:
      for action in self.actions:
        out("\t<" + action + ">")

    cmd = get_cmd()
    self.process_cmd(cmd)
  
  def process_cmd(self, cmd):
    if self.game.process_cmd():
      return

    if cmd in self.actions:
      if "description" in self.actions:
        out(self.actions[cmd]["description"])
      if "action" in self.actions[cmd]:
        self.actions[cmd]["action"]()