from input.InputCommand import InputCommand

class PageEnterCommand (InputCommand):
    def __init__(self):
        InputCommand.__init__(self)

    def execute(self, grid):
        print(grid.get_current_page().get_selected())