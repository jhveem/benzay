from object import Object

class Location:
  def __init__(self, game, name):
    self.name = name
    self.intro = ""
    self.actions = {
    }
    self.locations = [] 
    self.objects = [] 
    self.people = {}

    #set after imported into a game
    self.game = game

  def init(self):
    self.game.out(self.intro)
    for action in self.actions:
      self.game.out("\t<" + action.upper() + ">")
    cmd = self.game.get_cmd()
    if cmd in self.actions:
      self.actions[cmd]()
    else:
      self.game.invalid(cmd)
      self.init()

  def set_actions(self):
    if self.locations:
      self.actions["go"] = self.go

    if self.objects:
      self.actions["examine"] = self.examine

  def examine(self):
    self.game.out("What would you like to examine?")
    for object in self.objects:
      self.game.out("\t<" + object.upper() + ">")
    object = self.game.get_cmd()
    if object in self.objects:
      self.objects[object]["action"]()
      if "cmd" in self.objects[object]:
        return self.objects[object]["cmd"]
      else:
        return "location_enter#skip"
    else:
      return object 


  def go(self):
    self.game.out("Where would you like to go?")
    for location in self.locations:
      self.game.out("\t<" + location[0].upper() + ">")
    dest = self.game.get_cmd()
    invalid = True 
    for location in self.locations:
      if dest == location[0].lower():
        self.game.location = self.game.locations[location[1]](self.game)
        self.game.location.init()
        invalid = False 
        break
    if invalid:
      self.game.invalid(dest)
      self.go()
    

# #INFINITY TOWER
# loc = create_location("Infinity High Tower")
# loc.intro = "You see a tower that stretches into the clouds."
# loc.locations = {
#   "east": {
#     "location": "Town"
#   }
# }
# loc.set_actions()

# #CANDY VILLAGE
# loc = create_location("Candy Village")
# loc.intro = "It's brightly colored village with doors good enough to eat... Really!"
# loc.locations = {
#   "west": {
#     "location": "Town"
#   }
# }
# loc.objects = {
#   "tree": {
#     "action": lambda: out("It's covered in delicious purple candy plums!")
#   },
#   "cookie": {
#     "action": lambda: out("It's a cookie named Milk.")
#   }
# }
# loc.people = [
#   "Milk the Cookie"
# ]
# loc.set_actions()