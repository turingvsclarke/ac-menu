import json
import os

GAMES_DIR = "./games/"

class Game:
  def __init__ (self, metadata):
    self.title = metadata["title"]
    self.command = metadata["command"]

  def launch (self):
    game_dir = "{}{}/".format (GAMES_DIR, self.title)

    # Make sure we chdir back to original working directory
    current_dir = os.getcwd ()
    os.chdir (game_dir)
    os.system (self.command)
    os.chdir (current_dir)

  def get_all ():
    game_dirs = os.listdir (GAMES_DIR)
    games = []

    for game_dir in game_dirs:
      game_dir = "{}{}/".format (GAMES_DIR, game_dir)
      file = open ("{}metadata.json".format (game_dir), "r")
      metadata = json.loads (file.read ())
      file.close ()

      games.append (Game (metadata))

    return games