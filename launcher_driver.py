#!/usr/bin/env python3

from Game import Game

def main ():
  games = Game.get_all ()
  games[0].launch ()

if __name__ == "__main__":
  main ()