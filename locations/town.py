from locations.location import Location
from object import Object

class Town(Location):
  def __init__(self, game):
    super().__init__(game, "Home")
    self.intro = "You're in a town."
    self.locations = {
      ("home", "Home"),
      # "west": {
      #   "location": "Infinity High Tower"
      # },
      # "east": {
      #   "location": "Candy Village"
      # }
    }

    self.objects = {
      "tree": {
        "action": lambda: out("It's a tree!"),
        "cmd": "add_gold#10"
      }
    }
    self.set_actions()
