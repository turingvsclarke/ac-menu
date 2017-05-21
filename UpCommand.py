from NavigationCommand import NavigationCommand

class UpCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    page = grid.get_current_page ()
    navigation_elements = page.get_navigation_elements ()
    size = len (navigation_elements)
    selected = page.get_selected ()
    row_length = page.get_row_length ()

    # unselect previous grid element
    navigation_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = selected - row_length
    if new_selected < 0:
      rows = size // row_length
      new_selected = (rows * row_length) + selected
      if new_selected >= size:
        new_selected = new_selected - row_length

    page.set_selected (new_selected)

    # select new grid element
    navigation_elements[new_selected].toggle_selected ()