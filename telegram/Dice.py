from content import content


class Dice:
    def __init__(self):
        self.emoji: str = None
        self.value: int = None

    def set_data(self, context):
        self.emoji: str = content(context, "emoji")
        self.value: int = content(context, 'value')
