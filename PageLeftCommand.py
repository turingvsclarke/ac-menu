from InputCommand import InputCommand

class PageLeftCommand (InputCommand):
  def __init__ (self):
    InputCommand.__init__ (self)

  def execute (self, grid):
    page_index = grid.get_page_index ()
    page_count = grid.get_page_count ()

    new_page = (page_index - 1) % page_count
    grid.set_page_index (new_page)