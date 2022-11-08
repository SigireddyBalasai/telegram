from content import content


class WebAppData:
    def __init__(self):
        self.data: str = None
        self.button_text: str = None

    def set_data(self, context):
        self.data: str = content(context, 'data')
        self.button_text: str = content(context, 'button_text')
