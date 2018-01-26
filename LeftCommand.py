from InputCommand import InputCommand

class LeftCommand (InputCommand):
  def __init__ (self):
    InputCommand.__init__ (self)

  def execute (self, grid):
    page = grid.get_current_page ()
    grid_elements = page.get_grid_elements ()
    selected = page.get_selected ()

    # unselect previous grid element
    grid_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = (selected - 1) % len (grid_elements)

    page.set_selected (new_selected)

    # select new grid element
    grid_elements[new_selected].toggle_selected ()