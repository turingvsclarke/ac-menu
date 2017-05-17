from NavigationCommand import NavigationCommand

class UpCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    sprites = grid.getGridElements ().sprites ()
    size = len (sprites)
    selected = grid.getSelected ()
    row_length = grid.getRowLength ()

    # unselect previous grid element
    sprites[selected].toggle_selected ()

    # calculate new selected element
    newSelected = selected - row_length
    if newSelected < 0:
      rows = (size % row_length) - 1
      newSelected = (rows * row_length) + selected
      if newSelected >= size:
        newSelected = newSelected - row_length

    grid.setSelected (newSelected)

    # select new grid element
    sprites[newSelected].toggle_selected ()