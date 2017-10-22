from LeftCommand import LeftCommand
from RightCommand import RightCommand
from UpCommand import UpCommand
from DownCommand import DownCommand
from PageLeftCommand import PageLeftCommand
from PageRightCommand import PageRightCommand

# Factory class responsible for instantiating Input Commands
class InputCommandFlyweightFactory (object):
  def __init__ (self):
    object.__init__ (self)

    self.leftCommand = None
    self.rightCommand = None
    self.upCommand = None
    self.downCommand = None
    self.pageLeftCommand = None
    self.pageRightCommand = None

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

  def create_page_left_command (self):
    if self.pageLeftCommand is None:
      self.pageLeftCommand = PageLeftCommand ()

    return self.pageLeftCommand

  def create_page_right_command (self):
    if self.pageRightCommand is None:
      self.pageRightCommand = PageRightCommand ()

    return self.pageRightCommand