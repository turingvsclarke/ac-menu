from abc import abstractmethod

# Base class for Menu Input Commands
class InputCommand (object):
  def __init__ (self):
    object.__init__ (self)

  @abstractmethod
  def execute (self, grid): pass