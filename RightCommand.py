from NavigationCommand import NavigationCommand

class RightCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    sprites = grid.getGridElements ().sprites ()
    selected = grid.getSelected ()

    # unselect previous grid element
    sprites[selected].toggle_selected ()

    # calculate new selected element
    newSelected = (selected + 1) % len (sprites)

    grid.setSelected (newSelected)

    # select new grid element
    sprites[newSelected].toggle_selected ()