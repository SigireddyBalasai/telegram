from content import content


class VideoChatScheduled1:
    def __init__(self):
        self.start_date: int = None

    def set_data(self, context):
        self.start_date: int = content(context, 'start_date')
