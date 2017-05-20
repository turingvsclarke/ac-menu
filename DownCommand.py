from NavigationCommand import NavigationCommand

class DownCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    navigation_elements = grid.get_navigation_elements ()
    selected = grid.get_selected ()
    row_length = grid.get_row_length ()

    # unselect previous grid element
    navigation_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = selected + row_length
    if new_selected >= len (navigation_elements):
      new_selected = selected % row_length

    grid.set_selected (new_selected)

    # select new grid element
    navigation_elements[new_selected].toggle_selected ()