#!/usr/bin/env python3

from GameUtils import GameUtils
from Game import Game

GAMES_DIR = "./games/"

def main ():
  games = GameUtils.get_all (GAMES_DIR)
  games[0].launch ()

if __name__ == "__main__":
  main ()
