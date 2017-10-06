from NavigationCommand import NavigationCommand

class PageEnterCommand (NavigationCommand):
    def __init__(self):
        NavigationCommand.__init__(self)

    def execute(self, grid):
        print(page.get_selected())