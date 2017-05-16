from LeftCommand import LeftCommand
from RightCommand import RightCommand
from UpCommand import UpCommand
from DownCommand import DownCommand

# Factory class responsible for instantiating Navigation Commands
class NavigationCommandFlyweightFactory (object):
  def __init__ (self):
    object.__init__ (self)

    self.leftCommand_ = None
    self.rightCommand_ = None
    self.upCommand_ = None
    self.downCommand_ = None

  def create_left_command (self):
    if self.leftCommand_ is None:
      self.leftCommand_ = LeftCommand ()

    return self.leftCommand_

  def create_right_command (self):
    if self.rightCommand_ is None:
      self.rightCommand_ = RightCommand ()

    return self.rightCommand_

  def create_up_command (self):
    if self.upCommand_ is None:
      self.upCommand_ = UpCommand ()

    return self.upCommand_

  def create_down_command (self):
    if self.downCommand_ is None:
      self.downCommand_ = DownCommand ()

    return self.downCommand_