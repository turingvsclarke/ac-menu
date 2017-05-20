from LeftCommand import LeftCommand
from RightCommand import RightCommand
from UpCommand import UpCommand
from DownCommand import DownCommand

# Factory class responsible for instantiating Navigation Commands
class NavigationCommandFlyweightFactory (object):
  def __init__ (self):
    object.__init__ (self)

    self.leftCommand = None
    self.rightCommand = None
    self.upCommand = None
    self.downCommand = None

  def create_left_command (self):
    if self.leftCommand is None:
      self.leftCommand = LeftCommand ()

    return self.leftCommand

  def create_right_command (self):
    if self.rightCommand is None:
      self.rightCommand = RightCommand ()

    return self.rightCommand

  def create_up_command (self):
    if self.upCommand is None:
      self.upCommand = UpCommand ()

    return self.upCommand

  def create_down_command (self):
    if self.downCommand is None:
      self.downCommand = DownCommand ()

    return self.downCommand