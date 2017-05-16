from abc import abstractmethod

# Base class for Menu Navigation Commands
class NavigationCommand (object):
  def __init__ (self):
    object.__init__ (self)

  @abstractmethod
  def execute (self, grid): pass