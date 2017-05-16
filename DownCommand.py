from NavigationCommand import NavigationCommand

class DownCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    sprites = grid.getGridElements ().sprites ()
    selected = grid.getSelected ()
    row_length = grid.getRowLength ()

    # unselect previous grid element
    sprites[selected].toggle_selected ()

    # calculate new selected element
    newSelected = selected + row_length
    if newSelected >= len (sprites):
      newSelected = selected % row_length

    grid.setSelected (newSelected)

    # select new grid element
    sprites[newSelected].toggle_selected ()