import os

class Game:
  def __init__ (self, metadata, directory):
    self.title = metadata["title"]
    self.author = metadata["author"]
    self.language = metadata["language"]
    self.command = metadata["command"]
    self.directory = directory

  def launch (self):
    # Make sure we chdir back to original working directory
    current_dir = os.getcwd ()
    os.chdir (self.directory)
    os.system (self.command)
    os.chdir (current_dir)