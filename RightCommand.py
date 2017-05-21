from NavigationCommand import NavigationCommand

class RightCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    page = grid.get_current_page ()
    navigation_elements = page.get_navigation_elements ()
    selected = page.get_selected ()

    # unselect previous grid element
    navigation_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = (selected + 1) % len (navigation_elements)

    page.set_selected (new_selected)

    # select new grid element
    navigation_elements[new_selected].toggle_selected ()