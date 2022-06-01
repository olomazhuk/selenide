from selene.support.jquery_style_selectors import s


class HomePage(object):
    def __init__(self):
        self.flash_message = s("#flash")

