import os
import json
from elements.Game import Game

class GameUtils:

  # Retrieves all Games within a given directory
  @staticmethod
  def get_all (games_dir):
    game_dirs = os.listdir (games_dir)
    games = []

    for game_dir in game_dirs:
      game_dir = "{}{}/".format (games_dir, game_dir)
      file = open ("{}metadata.json".format (game_dir), "r")
      metadata = json.loads (file.read ())
      file.close ()

      games.append (Game (metadata, game_dir))

    return games
