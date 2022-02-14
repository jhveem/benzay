from locations.location import Location

#HOME
class Home(Location):
  def __init__(self, game):
    super().__init__(game, "Home")
    self.intro = "You're in your house."
    self.locations = [
      ("outside", "Town")
    ]
    self.objects = [

    ]
    self.set_actions()