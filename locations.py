from time import sleep

def out(string):
  string += "\n"
  for char in string:
      sleep(0.01)
      print(char, end='', flush=True)

def get_cmd():
  print("->", end='', flush=True)
  cmd = input().lower()
  return cmd 


locations = {}
class Location:
  def __init__(self, name):
    self.name = name
    self.intro = ""
    self.actions = {
      "search": {
        "action": self.search
      },
      "go": {
        "action": self.go 
      } 
    }
    self.go_options = {}
    self.search_options = {}

  def search(self):
    out("What would you like to search?")
    for search_option in self.search_options:
      out("\t<" + search_option.upper() + ">")
    search = get_cmd()
    if search in self.search_options:
      self.search_options[search]["action"]()
      return "location_enter#skip"
    else:
      return search

  def go(self):
    out("Where would you like to go?")
    for go_option in self.go_options:
      out("\t<" + go_option.upper() + ">")
    dest = get_cmd()
    if dest in self.go_options:
      return "location_change#" + dest
    return dest
    

def create_location(name):
  locations[name] = Location(name)
  return locations[name]


#HOME
loc = create_location("Home")
loc.intro = "You're in your house."
loc.go_options = {
  "outside": {
    "location": "Town"
  }
}
loc.search_options = {
  "bed": {
    "action": lambda: out("Your bed. Looks comfy!")
  }

}

#TOWN
loc = create_location("Town")
loc.intro = "You're in a town."
loc.go_options = {
  "home": {
    "location": "Home"
  },
  "west": {
    "location": "Infinity High Tower"
  }
}

loc.search_options = {
  "tree": {
    "action": lambda: out("It's a tree!")
  }
}

#INFINITY TOWER
loc = create_location("Infinity High Tower")
loc.intro = "You see a tower that stretches into the clouds."