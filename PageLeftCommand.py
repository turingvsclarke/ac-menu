from NavigationCommand import NavigationCommand

class PageLeftCommand (NavigationCommand):
  def __init__ (self):
    NavigationCommand.__init__ (self)

  def execute (self, grid):
    page_index = grid.get_page_index ()
    page_count = grid.get_page_count ()

    new_page = (page_index - 1) % page_count
    grid.set_page_index (new_page)