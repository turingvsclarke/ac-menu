from NavigationCommand import NavigationCommand

class RightCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    navigation_elements = grid.get_navigation_elements ()
    selected = grid.get_selected ()

    # unselect previous grid element
    navigation_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = (selected + 1) % len (navigation_elements)

    grid.set_selected (new_selected)

    # select new grid element
    navigation_elements[new_selected].toggle_selected ()