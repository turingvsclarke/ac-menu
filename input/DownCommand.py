from input.InputCommand import InputCommand

class DownCommand (InputCommand):
  def __init__ (self):
    InputCommand.__init__ (self)

  def execute (self, grid):
    page = grid.get_current_page ()
    grid_elements = page.get_grid_elements ()
    selected = page.get_selected ()
    row_length = page.get_row_length ()

    # unselect previous grid element
    grid_elements[selected].toggle_selected ()

    # calculate new selected element
    new_selected = selected + row_length
    if new_selected >= len (grid_elements):
      new_selected = selected % row_length

    page.set_selected (new_selected)

    # select new grid element
    grid_elements[new_selected].toggle_selected ()