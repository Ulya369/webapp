class Scene(object):

    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.count = 1

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
         self.paths.update(paths)

#create scenes of the game
central_corridor = Scene("Central Corridor", "central_corridor","CENTRAL: Gothons blocking the door to the Armory and about to pull a weapon to blast you.")
laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory","LASER_WEAPON_ARMORY: enter 3-digit code")
the_bridge = Scene("The Bridge", "the_bridge", "THE_BRIDGE: seal breaks and opens. bomb is under your arm")
escape_pod = Scene("Escape Pod", "escape_pod", "ESCAPE_POD: there is 5 pods, which one do you take?")
the_end_winner = Scene("Winner Scene", "the_end_winner","WINNER: you hit the eject button in POD-2. you WON!")
the_end_loser = Scene("Loser Scene", "the_end_loser", "LOSER: you hit eject button in random pod. you LOST!")
generic_death = Scene("Death Scene", "death", "you DIED!")
no_session = Scene("No-Session Scene", "no_session", "game aborted")

#define available actions
central_corridor.add_paths({'shoot':generic_death,'dodge':generic_death, 'joke': laser_weapon_armory})
laser_weapon_armory.add_paths({'132': the_bridge,'231': generic_death})
the_bridge.add_paths({'throw the bomb': generic_death,'slowly place the bomb': escape_pod})
escape_pod.add_paths({'2': the_end_winner,'4': the_end_loser})

# Make useful variables
START = central_corridor
SCENES = {
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death,
    no_session.urlname : no_session
}
