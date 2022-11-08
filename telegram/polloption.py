from App import content


class PollOPtion:
    def __init__(self):
        self.text: str = None
        self.voter_count: str = None

    def set(self, context):
        self.text: str = content(context, 'text')
        self.voter_count: str = content(context, 'voter_count')
