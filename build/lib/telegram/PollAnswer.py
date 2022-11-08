from User import User
from App import content
class PollAnswer:
    def __init__(self):
        self.poll_id: str=None
        self.user: User=None
        self.options_id: int=None

    def set(self, context):
        self.poll_id: str = content(context, 'poll_id')
        self.user: User = User().set_data(context['user'])
        self.options_id: int = content(context, 'options_id')